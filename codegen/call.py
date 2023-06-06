from typing import Any
from typing import Union
import ast

from codegen.common import Generator
from codegen.common import to_description
from codegen.function import FunctionGenerator
from codegen.lexicon import Lexicon


class CallGenerator(Generator):
    # for query and procedure
    def __init__(self, lexicon: Lexicon,
                 properties: dict[str, Any], required: list[str],
                 query_params: ast.List,
                 data: Union[ast.Dict, ast.Constant, ast.Name],
                 headers: ast.Dict) -> None:
        self.lexicon = lexicon
        self.query_params = query_params
        self.data = data
        self.headers = headers

        self.generator = FunctionGenerator(lexicon, properties, required)

    def generate(self) -> ast.FunctionDef:
        return self.generator.generate(
            self._args(), self._body(), ast.Name(id='bytes', ctx=ast.Load())
        )

    def _args(self) -> ast.arguments:
        self.lexicon.add_module('chitose')
        args = [
            self.generator.get_func_arg('call', 'XrpcCall')
        ] + self.generator.get_property_args()

        self.lexicon.append_function(
            self.generator.get_info(args, 'call')
        )

        return self.generator.get_args(args)

    def _body(self) -> list[Union[ast.Expr, ast.Return]]:
        description_lines = self.generator.get_description_lines()
        return [
            ast.Expr(
                value=ast.Constant(
                    value=to_description(description_lines, 4)
                )
            ),
            ast.Return(
                value=ast.Call(
                    func=ast.Name(id='call', ctx=ast.Load()),
                    args=[
                        ast.Constant(value=self.lexicon.get_id()),
                        self.query_params,
                        self.data,
                        self. headers,
                    ],
                    keywords=[]
                )
            )
        ]
