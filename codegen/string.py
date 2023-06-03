import ast

from codegen.common import Generator
from codegen.common import to_class_name
from codegen.lexicon import Lexicon


class StringGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

    def generate(self) -> ast.Assign:
        self.lexicon.add_module('typing')
        return ast.Assign(
            targets=[
                ast.Name(
                    id=to_class_name(
                        self.lexicon.get_def_id()
                    ), ctx=ast.Store()
                )
            ],
            value=ast.Subscript(
                value=ast.Attribute(
                    value=ast.Name(id='typing', ctx=ast.Load()),
                    attr='Literal',
                    ctx=ast.Load()
                ),
                slice=ast.Tuple(
                    elts=[
                        ast.Constant(value=known_value)
                        for known_value
                        in self.lexicon.get_current()['knownValues']
                    ],
                    ctx=ast.Load()
                ),
                ctx=ast.Load()
            )
        )
