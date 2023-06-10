from typing import Any
from typing import Union
import ast

from codegen.common import to_private_function_name
from codegen.common import to_snake
from codegen.common import FunctionInfo
from codegen.lexicon import Lexicon


class FunctionGenerator:
    # for query, procedure and subscription
    def __init__(self, lexicon: Lexicon,
                 properties: dict[str, Any], required: list[str]) -> None:
        self.lexicon = lexicon
        self.properties = properties
        self.required = required

    def generate(self, args: ast.arguments,
                 body: list[Union[ast.Expr, ast.Return]],
                 returns: Union[ast.Constant, ast.Name]) -> ast.FunctionDef:
        return ast.FunctionDef(
            name=to_private_function_name(self.lexicon.get_name()),
            args=args,
            body=body,
            decorator_list=[],
            returns=returns,
        )

    @staticmethod
    def get_query_properties_and_required(lexicon: Lexicon) \
            -> tuple[dict[str, Any], list[str]]:
        if 'parameters' not in lexicon.get_current():
            return {}, []

        parameters = lexicon.get_current()['parameters']
        assert parameters['type'] == 'params'

        properties = parameters['properties']
        required = parameters.get('required', [])

        properties = lexicon.reorder_properties(properties, required)
        return properties, required

    @staticmethod
    def get_query_params(properties: dict[str, Any]) -> ast.List:
        return ast.List(
            elts=[
                ast.Tuple(
                    elts=[
                        ast.Constant(value=property),
                        ast.Name(id=to_snake(property), ctx=ast.Load())
                    ],
                    ctx=ast.Load()
                )
                for property in properties
            ]
        )

    def get_func_arg(self, func: str, attr: str) -> ast.arg:
        return ast.arg(
            arg=func,
            annotation=ast.Attribute(
                value=ast.Attribute(
                    value=ast.Name(id='chitose', ctx=ast.Load()),
                    attr='xrpc',
                    ctx=ast.Load()
                ),
                attr=attr,
                ctx=ast.Load()
            ),
        )

    def get_property_args(self) -> list[ast.arg]:
        return [
            ast.arg(
                arg=to_snake(property),
                annotation=self.lexicon.get_annotation(
                    self.properties, self.required, property)
            )
            for property in self.properties
        ]

    def _none_count(self) -> int:
        return len(self.properties) - len(self.required)

    def get_args(self, args: list[ast.arg]) -> ast.arguments:
        none_count = self._none_count()
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

    def get_description_lines(self) -> list[str]:
        lines = [self.lexicon.get_current().get('description', '')]
        for property, detail in self.properties.items():
            if 'description' not in detail:
                continue

            params = f':param {to_snake(property)}: {detail["description"]}'
            lines.append(params)
        return lines

    def get_info(self, args: list[ast.arg], func: str) -> FunctionInfo:
        none_count = self._none_count()
        return FunctionInfo(
            name=to_snake(self.lexicon.get_name()),
            description_lines=self.get_description_lines(),
            args=args[1:],
            none_count=none_count,
            modules=self.lexicon.get_annotation_modules(),
            func=func,
        )
