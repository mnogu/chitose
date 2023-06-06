import ast
from collections import OrderedDict
from typing import Any
from typing import Callable
from typing import Union

from codegen.common import FunctionInfo
from codegen.common import to_class_name
from codegen.common import to_snake

NO_SCHEMA_INPUT_PROPERTY = 'input_'
NO_SCHEMA_INPUT_TYPE = '_no_schema'


class Lexicon:
    def __init__(self, id: str, def_id: str, current: dict[str, Any]) -> None:
        self.id = id
        self.def_id = def_id
        self.current = current
        self.modules: set[str] = set()
        self.annotation_modules: set[str] = set()
        self.functions: list[FunctionInfo] = []

    def get_modules(self) -> set[str]:
        return self.modules

    def add_module(self, module: str) -> None:
        self.modules.add(module)

    def get_annotation_modules(self) -> set[str]:
        return self.annotation_modules

    def add_annotation_module(self, module: str) -> None:
        self.annotation_modules.add(module)

    def get_functions(self) -> list[FunctionInfo]:
        return self.functions

    def append_function(self, info: FunctionInfo) -> None:
        self.functions.append(info)

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.get_id().rpartition('.')[2]

    def get_def_id(self) -> str:
        return self.def_id

    def get_current(self) -> dict[str, Any]:
        return self.current

    def reorder_properties(self, properties: dict[str, Any],
                           required: list[str]) -> dict[str, Any]:
        return OrderedDict({
            property: properties[property] for property in properties
            if property in required
        }) | OrderedDict({
            property: properties[property] for property in properties
            if property not in required
        })

    def _ref_annotations(self, ref: str, as_string: bool) \
            -> Union[ast.Name, ast.Attribute, ast.Constant]:
        # ex. ref: "foo.bar.bazQux#quux" or "#quux"
        if '#' in ref:
            # ex.
            #   module: foo.bar.bazQux
            #   ref_fragment: quux
            module, _, ref_fragment = ref.partition('#')

            # ex. ref: "#quux"
            if not module:
                # ex. module: "foo.bar.bazQux"
                module = self.get_id()

            # ex. name: Quux
            name = to_class_name(ref_fragment)

            # ex.
            #    ref: spam.ham.eggs#eggs or #eggs
            #    module: spam.ham.eggs
            #    ref_fragment: eggs
            #    name: Eggs => EggsEggs
            if ref_fragment == module.rpartition('.')[2]:
                name *= 2

        # ex. ref: "foo.bar.bazQux"
        else:
            # ex.
            #   module: foo.bar
            #   name: bazQux
            module, _, name = ref.rpartition('.')
            # ex. name: BazQux
            name = to_class_name(name)
            if module == self.get_id():
                return ast.Name(id=name, ctx=ast.Load())

            # ex. module: foo.bar.bazQux
            module = ref

        # ex.
        #   module: foo.bar.bazQux
        #   ref_parts: ['foo', 'bar', 'bazQux']
        ref_parts = module.split('.')
        # ex. ref_parts: ['foo', 'bar', 'baz_qux']
        ref_parts[-1] = to_snake(ref_parts[-1])

        # ex. chitose.foo.bar.baz_qux
        module = f'chitose.{".".join(ref_parts)}'
        self.modules.add(module)
        self.annotation_modules.add(module)

        if as_string:
            # ex. chitose.foo.bar.baz_qux.BazQux
            return ast.Constant('.'.join(['chitose'] + ref_parts + [name]))

        value: Union[ast.Name, ast.Attribute] = ast.Name(id='chitose',
                                                         ctx=ast.Load())
        for attr in ref_parts:
            value = ast.Attribute(
                value=value,
                attr=attr,
                ctx=ast.Load()
            )
        return ast.Attribute(
            value=value,
            attr=name,
            ctx=ast.Load()
        )

    def _name_annotation(self, type_: str) -> ast.Name:
        return ast.Name(id=type_, ctx=ast.Load())

    def _string_annotation(self, detail: dict[str, str]) -> Union[ast.Subscript, ast.Name]:
        if 'knownValues' not in detail:
            return ast.Name(id='str', ctx=ast.Load())

        self.modules.add('typing')
        self.annotation_modules.add('typing')
        return ast.Subscript(
            value=ast.Attribute(
                value=ast.Name(id='typing', ctx=ast.Load()),
                attr='Literal',
                ctx=ast.Load()
            ),
            slice=ast.Tuple(
                elts=[
                    ast.Constant(value=known_value)
                    for known_value in detail['knownValues']
                ],
                ctx=ast.Load()
            ),
            ctx=ast.Load()
        )

    def _blob_annotation(self) -> ast.Attribute:
        self.modules.add('chitose')
        self.annotation_modules.add('chitose')
        return ast.Attribute(
            value=ast.Name(id='chitose', ctx=ast.Load()),
            attr='Blob',
            ctx=ast.Load()
        )

    def _union_annotation(self, detail: dict[str, str], as_string: bool) \
            -> Union[ast.Name, ast.Attribute, ast.Constant, ast.Subscript]:
        self.modules.add('typing')
        self.annotation_modules.add('typing')
        elts = []
        refs = detail['refs']
        if len(refs) == 1:
            return self._ref_annotations(refs[0], as_string)

        for ref in refs:
            elts.append(self._ref_annotations(ref, as_string))

        return ast.Subscript(
            value=ast.Attribute(
                value=ast.Name(id='typing', ctx=ast.Load()),
                attr='Union',
                ctx=ast.Load()
            ),
            slice=ast.Tuple(
                elts=elts,
                ctx=ast.Load()
            ),
            ctx=ast.Load()
        )

    def _other_type_annotation(self) -> ast.Attribute:
        self.modules.add('typing')
        self.annotation_modules.add('typing')
        return ast.Attribute(
            value=ast.Name(id='typing', ctx=ast.Load()),
            attr='Any',
            ctx=ast.Load()
        )

    def _basic_annotation(self, detail: dict[str, str],
                          property: str, as_string: bool) \
            -> Union[ast.Subscript, ast.Name, ast.Attribute, ast.Constant]:

        generators: dict[str,
                         Callable[[], Union[ast.Subscript, ast.Name,
                                            ast.Attribute, ast.Constant]]] = {
            'boolean': lambda: self._name_annotation('bool'),
            'integer': lambda: self._name_annotation('int'),
            NO_SCHEMA_INPUT_TYPE: lambda: self._name_annotation('bytes'),
            'string': lambda: self._string_annotation(detail),
            'blob': lambda: self._blob_annotation(),
            'ref': lambda: self._ref_annotations(detail['ref'], as_string),
            'union': lambda: self._union_annotation(detail, as_string),
            # TODO
            'bytes': lambda: self._other_type_annotation(),
            # TODO
            'cid-link': lambda: self._other_type_annotation(),
            'unknown': lambda: self._other_type_annotation(),
        }

        type_ = detail['type']
        if type_ in generators:
            return generators[type_]()

        assert False, f'{type_} {property}'

    def get_array_annotation(self, detail: dict[str, Any],
                             as_string: bool) -> ast.Subscript:
        return ast.Subscript(
            value=ast.Name(id='list', ctx=ast.Load()),
            slice=self._basic_annotation(
                detail['items'], 'items', as_string
            ),
            ctx=ast.Load()
        )

    def _annotation_without_optional(self, properties: dict[str, Any],
                                     property: str) \
            -> Union[ast.Subscript, ast.Name, ast.Attribute, ast.Constant]:
        detail = properties[property]
        type_ = detail['type']

        if type_ == 'array':
            return self.get_array_annotation(detail, False)

        return self._basic_annotation(detail, property, False)

    def get_annotation(self, properties: dict[str, Any],
                       required: list[str], property: str) \
            -> Union[ast.Subscript, ast.Name, ast.Attribute, ast.Constant]:
        annotation_without_optional = self._annotation_without_optional(
            properties, property
        )
        if property in required:
            return annotation_without_optional

        self.modules.add('typing')
        self.annotation_modules.add('typing')
        return ast.Subscript(
            value=ast.Attribute(
                value=ast.Name(id='typing', ctx=ast.Load()),
                attr='Optional',
                ctx=ast.Load()
            ),
            slice=annotation_without_optional,
            ctx=ast.Load()
        )
