import ast

from codegen.common import Generator
from codegen.klass import ClassGenerator
from codegen.lexicon import Lexicon


class ObjectGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

        self.properties = self.lexicon.get_current().get('properties', [])
        self.required = self.lexicon.get_current().get('required', [])
        self.description = self.lexicon.get_current().get('description', '')

        self.properties = self.lexicon.reorder_properties(
            self.properties, self.required
        )

        self.generator = ClassGenerator(
            lexicon, self.properties, self.required, self.description
        )

    def generate(self) -> ast.ClassDef:
        return self.generator.generate()
