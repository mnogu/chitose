import ast
from collections import OrderedDict
from typing import Any
from typing import Union

from codegen.common import ANNOTATIONS_IMPORT
from codegen.common import FunctionInfo
from codegen.common import Generator
from codegen.common import to_class_name
from codegen.common import to_constant
from codegen.common import to_description
from codegen.common import to_private_function_name
from codegen.common import to_snake

NO_SCHEMA_INPUT_PROPERTY = 'input_'
NO_SCHEMA_INPUT_TYPE = '_no_schema'


class CodeGenerator(Generator):
    def __init__(self, json_data) -> None:
        self.json_data = json_data
        assert json_data['lexicon'] == 1
        self.modules: set[str] = set()
        self.annotation_modules: set[str] = set()
        self.data: Union[ast.Constant, ast.Dict, ast.Name]
        self.functions: list[FunctionInfo] = []

    def get_functions(self) -> list[FunctionInfo]:
        return self.functions

    def generate(self) -> ast.Module:
        body: list[Union[ast.ClassDef, ast.FunctionDef,
                         ast.ImportFrom, ast.Import, ast.Assign, ast.Expr]] = []
        for def_id in self.json_data['defs']:
            self.def_id = def_id
            self.current = self.json_data['defs'][def_id]

            type_ = self.current['type']
            elem: Union[ast.ClassDef, ast.FunctionDef, ast.Assign]
            if type_ == 'query':
                self._init_query()
                self._reorder_properties()
                elem = self._function()
            elif type_ == 'procedure':
                self._init_procedure()
                self._reorder_properties()
                elem = self._function()
            elif type_ == 'object':
                self._init_object()
                self._reorder_properties()
                elem = self._class()
            elif type_ == 'record':
                self._init_record()
                self._reorder_properties()
                elem = self._class()
            elif type_ == 'subscription':
                continue  # TODO
            elif type_ == 'string':
                elem = self._string()
            elif type_ == 'token':
                elem = self._token()
            elif type_ == 'array':
                elem = self._array()
            else:
                assert False, type_
            body.append(elem)

        body = [self._module_docstring()] \
            + self._imports() \
            + body

        return ast.Module(
            body=body,
            type_ignores=[]
        )

    def _init_query(self) -> None:
        if 'parameters' in self.current:
            parameters = self.current['parameters']
            assert parameters['type'] == 'params'

            self.properties = parameters['properties']
            self.required = parameters.get('required', [])
        else:
            self.properties = {}
            self.required = []

        self.query_params = ast.List(
            elts=[
                ast.Tuple(
                    elts=[
                        ast.Constant(value=property),
                        ast.Name(id=to_snake(property), ctx=ast.Load())
                    ],
                    ctx=ast.Load()
                )
                for property in self.properties
            ]
        )
        self.data = ast.Constant(value=None)
        self.headers = ast.Dict(keys=[], values=[])

    def _init_procedure(self) -> None:
        if 'input' in self.current:
            input_ = self.current['input']
            if 'schema' in input_:
                schema = input_['schema']
                assert schema['type'] == 'object'

                self.properties = schema['properties']
                self.required = schema.get('required', [])
            else:
                # com.atproto.repo.uploadBlob has no schema
                self.properties = {
                    NO_SCHEMA_INPUT_PROPERTY: {
                        'type': NO_SCHEMA_INPUT_TYPE,
                        'encoding': input_['encoding']
                    }
                }
                self.required = [NO_SCHEMA_INPUT_PROPERTY]

            self.headers = ast.Dict(
                keys=[ast.Constant(value='Content-Type')],
                values=[ast.Constant(value=input_['encoding'])]
            )
        else:
            self.properties = {}
            self.required = []
            self.headers = ast.Dict(keys=[], values=[])

        self.query_params = ast.List(elts=[], ctx=ast.Load())
        if NO_SCHEMA_INPUT_PROPERTY in self.properties:
            self.data = ast.Name(id=NO_SCHEMA_INPUT_PROPERTY, ctx=ast.Load())
            return

        self.data = ast.Dict(
            keys=[
                ast.Constant(value=property)
                for property in self.properties
            ],
            values=[
                ast.Name(id=to_snake(property), ctx=ast.Load())
                for property in self.properties
            ]
        )

    def _init_object(self) -> None:
        self.properties = self.current['properties']
        self.required = self.current.get('required', [])

    def _init_record(self) -> None:
        self.properties = self.current['record']['properties']
        self.required = self.current['record'].get('required', [])

    def _reorder_properties(self):
        self.properties = OrderedDict({
            property: self.properties[property] for property in self.properties
            if property in self.required
        }) | OrderedDict({
            property: self.properties[property] for property in self.properties
            if property not in self.required
        })

    def _module_docstring(self) -> ast.Expr:
        return ast.Expr(
            value=ast.Constant(value=self.json_data.get('description', ''))
        )

    def _imports(self) -> list[Union[ast.ImportFrom, ast.Import]]:
        imports: list[Union[ast.ImportFrom, ast.Import]] = [
            ANNOTATIONS_IMPORT
        ]
        imports += [
            ast.Import(
                names=[
                    ast.alias(name=module)
                ]
            )
            for module in sorted(list(self.modules))
        ]
        return imports

    def _get_name(self) -> str:
        return self.json_data['id'].rpartition('.')[2]

    def _function(self) -> ast.FunctionDef:
        return ast.FunctionDef(
            name=to_private_function_name(self._get_name()),
            args=self._function_args(),
            body=self._function_body(),
            decorator_list=[],
            returns=ast.Name(id='bytes', ctx=ast.Load())
        )

    def _class(self) -> ast.ClassDef:
        name = self._get_name()
        if self.def_id != 'main':
            if self.def_id == name:
                # ex.
                #    id: spam.ham.eggs
                #    name: eggs
                #    def_id: eggs
                #    => name: EggsEggs
                name = to_class_name(name) * 2
            else:
                name = self.def_id

        name = to_class_name(name)
        base_name = to_class_name(self.current['type'])
        self.modules.add('chitose')
        return ast.ClassDef(
            name=name,
            bases=[
                ast.Name(id=f'chitose.{base_name}', ctx=ast.Load()),
            ],
            keywords=[],
            body=[
                self._class_comment(),
                self._init_function(),
                self._to_dict_function()
            ],
            decorator_list=[]
        )

    def _class_comment(self) -> ast.Expr:
        lines = ['']
        for property in self.properties:
            description = self.properties[property].get('description')
            if description:
                lines.append(f':param {to_snake(property)}: {description}')

        return ast.Expr(value=ast.Constant(value=to_description(lines, 4)))

    def _init_function(self) -> ast.FunctionDef:
        args = [
            ast.arg(arg='self')
        ]
        args += [
            ast.arg(arg=to_snake(property),
                    annotation=self._annotation(property))
            for property in self.properties
        ]
        return ast.FunctionDef(
            name='__init__',
            args=ast.arguments(
                posonlyargs=[],
                args=args,
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[
                    ast.Constant(value=None)
                    for _ in range(len(self.properties) - len(self.required))
                ]),
            body=[
                ast.Assign(
                    targets=[
                        ast.Attribute(
                            value=ast.Name(id='self', ctx=ast.Load()),
                            attr=to_snake(property),
                            ctx=ast.Store())
                    ],
                    value=ast.Name(id=to_snake(property), ctx=ast.Load())
                )
                for property in self.properties
            ],
            decorator_list=[],
            returns=ast.Constant(value=None))

    def _get_ref(self):
        ref = self.json_data['id']
        if self.def_id != 'main':
            ref += f'#{self.def_id}'
        return ref

    def _to_dict_function(self) -> ast.FunctionDef:
        return ast.FunctionDef(
            name='to_dict',
            args=ast.arguments(
                posonlyargs=[],
                args=[
                    ast.arg(arg='self')],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                ast.Return(
                    value=ast.Dict(
                        keys=[
                            ast.Constant(value=property)
                            for property in self.properties
                        ] + [
                            ast.Constant(value='$type')
                        ],
                        values=[
                            ast.Attribute(
                                value=ast.Name(id='self', ctx=ast.Load()),
                                attr=to_snake(property),
                                ctx=ast.Load())
                            for property in self.properties
                        ] + [
                            ast.Constant(value=self._get_ref(), ctx=ast.Load())
                        ]

                    )
                )
            ],
            decorator_list=[],
            returns=ast.Name(id='dict', ctx=ast.Load())
        )

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
                module = self.json_data['id']

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
            if module == self.json_data['id']:
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
            ctx=ast.Load())

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
                ctx=ast.Load()),
            slice=ast.Tuple(
                elts=elts,
                ctx=ast.Load()),
            ctx=ast.Load())

    def _other_type_annotation(self) -> ast.Attribute:
        self.modules.add('typing')
        self.annotation_modules.add('typing')
        return ast.Attribute(
            value=ast.Name(id='typing', ctx=ast.Load()),
            attr='Any',
            ctx=ast.Load())

    def _basic_annotation(self, detail: dict[str, str],
                          property: str, as_string: bool) \
            -> Union[ast.Subscript, ast.Name, ast.Attribute, ast.Constant]:

        generators = {
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

    def _array_annotation(self, detail: dict[str, Any], as_string: bool) -> ast.Subscript:
        return ast.Subscript(
            value=ast.Name(id='list', ctx=ast.Load()),
            slice=self._basic_annotation(
                detail['items'], 'items', as_string
            ),
            ctx=ast.Load())

    def _annotation_without_optional(self, property: str) \
            -> Union[ast.Subscript, ast.Name, ast.Attribute, ast.Constant]:
        detail = self.properties[property]
        type_ = detail['type']

        if type_ == 'array':
            return self._array_annotation(detail, False)

        return self._basic_annotation(detail, property, False)

    def _annotation(self, property: str) \
            -> Union[ast.Subscript, ast.Name, ast.Attribute, ast.Constant]:
        annotation_without_optional = self._annotation_without_optional(
            property)
        if property in self.required:
            return annotation_without_optional

        self.modules.add('typing')
        self.annotation_modules.add('typing')
        return ast.Subscript(
            value=ast.Attribute(
                value=ast.Name(id='typing', ctx=ast.Load()),
                attr='Optional',
                ctx=ast.Load()),
            slice=annotation_without_optional,
            ctx=ast.Load())

    def _get_description_lines(self) -> list[str]:
        lines = [self.current.get('description', '')]
        for property, detail in self.properties.items():
            if 'description' not in detail:
                continue

            params = f':param {to_snake(property)}: {detail["description"]}'
            lines.append(params)
        return lines

    def _function_args(self) -> ast.arguments:
        none_count = len(self.properties) - len(self.required)
        args = [
            ast.arg(
                arg=to_snake(property),
                annotation=self._annotation(property)
            )
            for property in self.properties
        ]
        self.functions.append(FunctionInfo(
            name=to_snake(self._get_name()),
            description_lines=self._get_description_lines(),
            args=args,
            none_count=none_count,
            modules=self.annotation_modules,
        ))

        self.modules.add('chitose')
        args = [
            ast.arg(
                arg='call',
                annotation=ast.Attribute(
                    value=ast.Attribute(
                        value=ast.Name(id='chitose', ctx=ast.Load()),
                        attr='xrpc',
                        ctx=ast.Load()
                    ),
                    attr='XrpcCallable',
                    ctx=ast.Load()
                ),
            ),
        ] + args
        return ast.arguments(
            posonlyargs=[],
            args=args,
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
                ast.Constant(value=None)
                for _ in range(none_count)
            ]
        )

    def _function_body(self) -> list[Union[ast.Expr, ast.Return]]:
        return [
            ast.Expr(
                value=ast.Constant(
                    value=to_description(self._get_description_lines(), 4)
                )
            ),
            ast.Return(
                value=ast.Call(
                    func=ast.Name(id='call', ctx=ast.Load()),
                    args=[
                        ast.Constant(value=self.json_data['id']),
                        self.query_params,
                        self.data,
                        self.headers,
                    ],
                    keywords=[]
                )
            )
        ]

    def _string(self) -> ast.Assign:
        self.modules.add('typing')
        return ast.Assign(
            targets=[
                ast.Name(id=to_class_name(self.def_id), ctx=ast.Store())
            ],
            value=ast.Subscript(
                value=ast.Attribute(
                    value=ast.Name(id='typing', ctx=ast.Load()),
                    attr='Literal',
                    ctx=ast.Load()),
                slice=ast.Tuple(
                    elts=[
                        ast.Constant(value=known_value)
                        for known_value in self.current['knownValues']
                    ],
                    ctx=ast.Load()),
                ctx=ast.Load()
            )
        )

    def _token(self) -> ast.Assign:
        return ast.Assign(
            targets=[
                ast.Name(id=to_constant(self.def_id), ctx=ast.Store())],
            value=ast.Constant(value=f'{self.json_data["id"]}#{self.def_id}')
        )

    def _array(self) -> ast.Assign:
        return ast.Assign(
            targets=[
                ast.Name(id=to_class_name(self.def_id), ctx=ast.Store())
            ],
            value=self._array_annotation(self.current, True)
        )
