import ast
from codegen.call import CallGenerator

from codegen.common import Generator
from codegen.function import FunctionGenerator
from codegen.lexicon import Lexicon


class QueryGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

        self.properties, self.required \
            = FunctionGenerator.get_query_properties_and_required(lexicon)
        self.query_params \
            = FunctionGenerator.get_query_params(self.properties)
        self.data = ast.Constant(value=None)
        self.headers = ast.Dict(keys=[], values=[])

        self.generator = CallGenerator(
            lexicon, self.properties, self.required,
            self.query_params, self.data, self.headers
        )

    def generate(self) -> ast.FunctionDef:
        return self.generator.generate()
