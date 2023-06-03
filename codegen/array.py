import ast

from codegen.common import Generator
from codegen.common import to_class_name
from codegen.lexicon import Lexicon


class ArrayGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

    def generate(self) -> ast.Assign:
        return ast.Assign(
            targets=[
                ast.Name(
                    id=to_class_name(self.lexicon.get_def_id()),
                    ctx=ast.Store()
                )
            ],
            value=self.lexicon.get_array_annotation(
                self.lexicon.current, True
            )
        )
