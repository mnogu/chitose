import ast
from collections import OrderedDict
from typing import Union

from codegen.common import ANNOTATIONS_IMPORT
from codegen.common import FunctionInfo
from codegen.common import Generator
from codegen.common import to_class_name
from codegen.common import to_constant
from codegen.common import to_snake


class CodeGenerator(Generator):
    def __init__(self, json_data) -> None:
        self.json_data = json_data
        assert json_data['lexicon'] == 1
        self.imports: set[str] = set()
        self.data: Union[ast.Constant, ast.Dict]
        self.functions: list[FunctionInfo] = []

    def get_functions(self) -> list[FunctionInfo]:
        return self.functions

    def generate(self) -> ast.Module:
        body: list[Union[ast.ClassDef, ast.FunctionDef,
                         ast.ImportFrom, ast.Import, ast.Assign]] = []
        for def_id in self.json_data['defs']:
            self.def_id = def_id
            self.current = self.json_data['defs'][def_id]

            type_ = self.current['type']
            elem: Union[ast.ClassDef, ast.FunctionDef, ast.Assign]
            if type_ == 'query':
                self._init_query()
                self._reorder_properties()
                elem = self._generate_function()
            elif type_ == 'procedure':
                self._init_procedure()
                self._reorder_properties()
                elem = self._generate_function()
            elif type_ == 'object':
                self._init_object()
                self._reorder_properties()
                elem = self._generate_class()
            elif type_ == 'record':
                self._init_record()
                self._reorder_properties()
                elem = self._generate_class()
            elif type_ == 'subscription':
                continue  # TODO
            elif type_ == 'string':
                elem = self._generate_enum()
            elif type_ == 'token':
                elem = self._generate_constant()
            else:
                assert False, type_
            body.append(elem)

        body = self._generate_imports() + body

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
                self.properties = {}
                self.required = []

            self.headers = ast.Dict(
                keys=[ast.Constant(value='Content-Type')],
                values=[ast.Constant(value=input_['encoding'])]
            )
        else:
            self.properties = {}
            self.required = []
            self.headers = ast.Dict(keys=[], values=[])

        self.query_params = ast.List(elts=[], ctx=ast.Load())
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

    def _generate_imports(self) -> list[Union[ast.ImportFrom, ast.Import]]:
        imports: list[Union[ast.ImportFrom, ast.Import]] = [
            ANNOTATIONS_IMPORT
        ]
        imports += [
            ast.Import(
                names=[
                    ast.alias(name=module)
                ]
            )
            for module in sorted(list(self.imports))
        ]
        return imports

    def _get_name(self) -> str:
        return self.json_data['id'].rpartition('.')[2]

    def _generate_function(self) -> ast.FunctionDef:
        return ast.FunctionDef(
            name=to_snake(self._get_name()),
            args=self._generate_function_args(),
            body=self._generate_function_body(),
            decorator_list=[]
        )

    def _generate_class(self) -> ast.ClassDef:
        if self.def_id == 'main':
            name = self._get_name()
        else:
            name = self.def_id

        name = to_class_name(name)
        base_name = to_class_name(self.current['type'])
        self.imports.add('chitose')
        return ast.ClassDef(
            name=name,
            bases=[
                ast.Name(id=f'chitose.{base_name}', ctx=ast.Load()),
            ],
            keywords=[],
            body=[
                self._generate_init_function(),
                self._generate_to_dict_function()
            ],
            decorator_list=[]
        )

    def _generate_init_function(self) -> ast.FunctionDef:
        args = [
            ast.arg(arg='self')
        ]
        args += [
            ast.arg(arg=to_snake(property),
                    annotation=self._generate_annotation(property))
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

    def _generate_to_dict_function(self) -> ast.FunctionDef:
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
                        ],
                        values=[
                            ast.Attribute(
                                value=ast.Name(id='self', ctx=ast.Load()),
                                attr=to_snake(property),
                                ctx=ast.Load())
                            for property in self.properties
                        ]
                    )
                )
            ],
            decorator_list=[]
        )

    def _generate_ref_annotations(self, ref: str) -> Union[ast.Name,
                                                           ast.Attribute]:
        if '#' in ref:
            module, _, ref_fragment = ref.partition('#')
            name = to_class_name(ref_fragment)
            if not module or module == self.json_data['id']:
                return ast.Name(id=name, ctx=ast.Load())
        else:
            module, _, name = ref.rpartition('.')
            name = to_class_name(name)
            if module == self.json_data['id']:
                return ast.Name(id=name, ctx=ast.Load())

        ref_parts = module.split('.')
        ref_parts[-1] = to_snake(ref_parts[-1])

        self.imports.add(f'chitose.{".".join(ref_parts)}')
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

    def _generate_primitive_annotation(
            self, detail: dict[str, str],
            property: str) -> Union[ast.Subscript, ast.Name, ast.Attribute]:
        type_ = detail['type']

        if type_ == 'boolean':
            return ast.Name(id='str', ctx=ast.Load())

        if type_ == 'integer':
            return ast.Name(id='int', ctx=ast.Load())

        if type_ == 'string':
            return ast.Name(id='str', ctx=ast.Load())

        if type_ == 'ref':
            ref = detail['ref']
            return self._generate_ref_annotations(ref)

        if type_ == 'union':
            self.imports.add('typing')
            elts = []
            refs = detail['refs']
            if len(refs) == 1:
                return self._generate_ref_annotations(refs[0])

            for ref in refs:
                elts.append(self._generate_ref_annotations(ref))

            return ast.Subscript(
                value=ast.Attribute(
                    value=ast.Name(id='typing', ctx=ast.Load()),
                    attr='Union',
                    ctx=ast.Load()),
                slice=ast.Tuple(
                    elts=elts,
                    ctx=ast.Load()),
                ctx=ast.Load())

        # TODO
        if type_ in ['blob', 'bytes', 'cid-link', 'unknown']:
            self.imports.add('typing')
            return ast.Attribute(
                value=ast.Name(id='typing', ctx=ast.Load()),
                attr='Any',
                ctx=ast.Load())

        assert False, f'{type_} {property}'

    def _generate_annotation_without_optional(
            self, property: str) -> Union[ast.Subscript, ast.Name,
                                          ast.Attribute]:
        detail = self.properties[property]
        type_ = detail['type']

        if type_ == 'array':
            slice = self._generate_primitive_annotation(
                detail['items'], 'items')
            return ast.Subscript(
                value=ast.Name(id='list', ctx=ast.Load()),
                slice=slice,
                ctx=ast.Load())

        return self._generate_primitive_annotation(detail, property)

    def _generate_annotation(
            self, property: str) -> Union[ast.Subscript, ast.Name,
                                          ast.Attribute]:
        annotation_without_optional = \
            self._generate_annotation_without_optional(property)
        if property in self.required:
            return annotation_without_optional

        self.imports.add('typing')
        return ast.Subscript(
            value=ast.Attribute(
                value=ast.Name(id='typing', ctx=ast.Load()),
                attr='Optional',
                ctx=ast.Load()),
            slice=annotation_without_optional,
            ctx=ast.Load())

    def _generate_function_args(self) -> ast.arguments:
        none_count = len(self.properties) - len(self.required)
        args = [
            ast.arg(
                arg=to_snake(property),
                annotation=self._generate_annotation(property)
            )
            for property in self.properties
        ]
        self.functions.append(FunctionInfo(
            to_snake(self._get_name()),
            args,
            none_count
        ))

        args = [
            ast.arg(
                arg='service',
                annotation=ast.Name(id='str', ctx=ast.Load())
            ),
            ast.arg(
                arg='headers',
                annotation=ast.Subscript(
                    value=ast.Name(id='dict', ctx=ast.Load()),
                    slice=ast.Tuple(
                        elts=[
                            ast.Name(id='str', ctx=ast.Load()),
                            ast.Name(id='str', ctx=ast.Load())
                        ],
                        ctx=ast.Load()),
                    ctx=ast.Load()
                )
            )
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

    def _generate_function_body(self) -> list[Union[ast.Expr, ast.Return]]:
        self.imports.add('chitose')
        return [
            ast.Expr(
                value=ast.Constant(
                    value=self.current.get('description', '')
                )
            ),
            ast.Return(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id='chitose', ctx=ast.Load()),
                            attr='xrpc',
                            ctx=ast.Load()),
                        attr='call',
                        ctx=ast.Load()
                    ),
                    args=[
                        ast.Constant(value=self.json_data['id']),
                        self.query_params,
                        self.data,
                        ast.Name(id='service', ctx=ast.Load()),
                        ast.BinOp(
                            left=self.headers,
                            op=ast.BitOr(),
                            right=ast.Name(id='headers', ctx=ast.Load())
                        )
                    ],
                    keywords=[]
                )
            )
        ]

    def _generate_enum(self) -> ast.ClassDef:
        self.imports.add('enum')
        return ast.ClassDef(
            name=to_class_name(self.def_id),
            bases=[
                ast.Attribute(
                    value=ast.Name(id='enum', ctx=ast.Load()),
                    attr='Enum',
                    ctx=ast.Load()
                )
            ],
            keywords=[],
            body=[
                ast.Assign(
                    targets=[
                        ast.Name(id=to_constant(
                            know_value.partition('#')[2]), ctx=ast.Store())
                    ],
                    value=ast.Constant(value=know_value)
                )
                for know_value in self.current['knownValues']
            ],
            decorator_list=[]
        )

    def _generate_constant(self) -> ast.Assign:
        return ast.Assign(
            targets=[
                ast.Name(id=to_constant(self.def_id), ctx=ast.Store())],
            value=ast.Constant(value=f'{self.json_data["id"]}#{self.def_id}')
        )
