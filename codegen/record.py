import ast

from codegen.common import Generator
from codegen.klass import ClassGenerator
from codegen.lexicon import Lexicon


class RecordGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

        current_record = self.lexicon.get_current()['record']
        self.properties = current_record['properties']
        self.required = current_record.get('required', [])
        self.description = current_record.get('description', '')

        self.properties = self.lexicon.reorder_properties(
            self.properties, self.required
        )

        self.generator = ClassGenerator(
            lexicon, self.properties, self.required, self.description
        )

    def generate(self) -> ast.ClassDef:
        return self.generator.generate()
