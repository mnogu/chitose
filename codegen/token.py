from typing import Union
import ast

from codegen.common import Generator
from codegen.common import to_constant
from codegen.lexicon import Lexicon


class TokenGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

    def generate(self) -> Union[ast.Assign, ast.ClassDef, ast.FunctionDef]:
        value = f'{self.lexicon.get_id()}#{self.lexicon.get_def_id()}'
        return ast.Assign(
            targets=[
                ast.Name(
                    id=to_constant(self.lexicon.get_def_id()),
                    ctx=ast.Store()
                )
            ],
            value=ast.Constant(value=value)
        )
