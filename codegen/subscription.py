import ast

from typing import Union

from codegen.common import Generator
from codegen.common import to_description
from codegen.function import FunctionGenerator
from codegen.lexicon import Lexicon


class SubscriptionGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

        self.properties, self.required \
            = FunctionGenerator.get_query_properties_and_required(lexicon)
        self.query_params \
            = FunctionGenerator.get_query_params(self.properties)

        self.generator = FunctionGenerator(
            lexicon, self.properties, self.required
        )

    def generate(self) -> ast.FunctionDef:
        return self.generator.generate(
            self._args(), self._body(), ast.Constant(value=None)
        )

    def _args(self) -> ast.arguments:
        self.lexicon.add_module('chitose')
        self.lexicon.add_annotation_module('chitose')
        args = [
            self.generator.get_func_arg('subscribe', 'XrpcSubscribe'),
            ast.arg(
                arg='handler',
                annotation=ast.Attribute(
                    value=ast.Attribute(
                        value=ast.Name(id='chitose', ctx=ast.Load()),
                        attr='xrpc',
                        ctx=ast.Load()
                    ),
                    attr='XrpcHandler',
                    ctx=ast.Load()
                )
            ),
        ] + self.generator.get_property_args()

        self.lexicon.append_function(
            self.generator.get_info(args, 'subscribe')
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
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id='subscribe', ctx=ast.Load()),
                    args=[
                        ast.Constant(value=self.lexicon.get_id()),
                        self.query_params,
                        ast.Name(id='handler', ctx=ast.Load()),
                    ],
                    keywords=[]
                )
            )
        ]
