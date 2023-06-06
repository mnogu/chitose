from typing import Any
import ast

from codegen.common import Generator
from codegen.common import to_class_name
from codegen.common import to_description
from codegen.common import to_snake
from codegen.lexicon import Lexicon


class ClassGenerator(Generator):
    # for object and record
    def __init__(self, lexicon: Lexicon,
                 properties: dict[str, Any], required: list[str]) -> None:
        self.lexicon = lexicon
        self.properties = properties
        self.required = required

        self.def_id = lexicon.get_def_id()
        self.current = lexicon.get_current()

    def generate(self) -> ast.ClassDef:
        name = self.lexicon.get_name()
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
        self.lexicon.add_module('chitose')
        return ast.ClassDef(
            name=name,
            bases=[
                ast.Name(id=f'chitose.{base_name}', ctx=ast.Load()),
            ],
            keywords=[],
            body=[
                self._class_comment(self.properties),
                self._init_function(self.properties, self.required),
                self._to_dict_function(self.properties)
            ],
            decorator_list=[]
        )

    def _class_comment(self, properties: dict[str, Any]) -> ast.Expr:
        lines = ['']
        for property in properties:
            description = properties[property].get('description')
            if description:
                lines.append(f':param {to_snake(property)}: {description}')

        return ast.Expr(value=ast.Constant(value=to_description(lines, 4)))

    def _init_function(self, properties: dict[str, Any],
                       required: list[str]) -> ast.FunctionDef:
        args = [
            ast.arg(arg='self')
        ]
        args += [
            ast.arg(
                arg=to_snake(property),
                annotation=self.lexicon.get_annotation(
                    properties, required, property
                )
            )
            for property in properties
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
                    for _ in range(len(properties) - len(required))
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
                for property in properties
            ],
            decorator_list=[],
            returns=ast.Constant(value=None))

    def _get_ref(self) -> str:
        ref = self.lexicon.get_id()
        if self.def_id != 'main':
            ref += f'#{self.def_id}'
        return ref

    def _to_dict_function(self,
                          properties: dict[str, Any]) -> ast.FunctionDef:
        self.lexicon.add_module('typing')  # for typing.Any
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
                            for property in properties
                        ] + [
                            ast.Constant(value='$type')
                        ],
                        values=[
                            ast.Attribute(
                                value=ast.Name(id='self', ctx=ast.Load()),
                                attr=to_snake(property),
                                ctx=ast.Load())
                            for property in properties
                        ] + [
                            ast.Constant(value=self._get_ref(), ctx=ast.Load())
                        ]

                    )
                )
            ],
            decorator_list=[],
            returns=ast.Subscript(
                value=ast.Name(id='dict', ctx=ast.Load()),
                slice=ast.Tuple(
                    elts=[
                        ast.Name(id='str', ctx=ast.Load()),
                        ast.Attribute(
                            value=ast.Name(id='typing', ctx=ast.Load()),
                            attr='Any',
                            ctx=ast.Load()
                        )
                    ],
                    ctx=ast.Load()
                ),
                ctx=ast.Load()
            )
        )
