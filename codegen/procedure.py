from typing import Union
import ast

from codegen.call import CallGenerator
from codegen.common import Generator
from codegen.common import to_snake
from codegen.lexicon import Lexicon
from codegen.lexicon import NO_SCHEMA_INPUT_PROPERTY
from codegen.lexicon import NO_SCHEMA_INPUT_TYPE


class ProcedureGenerator(Generator):
    def __init__(self, lexicon: Lexicon) -> None:
        self.lexicon = lexicon

        current = self.lexicon.get_current()
        if 'input' in current:
            input_ = current['input']
            if 'schema' in input_:
                schema = input_['schema']
                assert schema['type'] == 'object'

                self.properties = schema['properties']
                self.required = schema.get('required', [])
            else:
                # com.atproto.repo.uploadBlob has no schema
                self.properties = {
                    NO_SCHEMA_INPUT_PROPERTY: {
                        'type': NO_SCHEMA_INPUT_TYPE,
                        'encoding': input_['encoding']
                    }
                }
                self.required = [NO_SCHEMA_INPUT_PROPERTY]

            self.headers = ast.Dict(
                keys=[ast.Constant(value='Content-Type')],
                values=[ast.Constant(value=input_['encoding'])]
            )
        else:
            self.properties = {}
            self.required = []
            self.headers = ast.Dict(keys=[], values=[])

        self.query_params = ast.List(elts=[], ctx=ast.Load())

        self.data: Union[ast.Constant, ast.Dict, ast.Name]
        if NO_SCHEMA_INPUT_PROPERTY in self.properties:
            self.data = ast.Name(id=NO_SCHEMA_INPUT_PROPERTY, ctx=ast.Load())
        else:
            self.data = ast.Dict(
                keys=[
                    ast.Constant(value=property)
                    for property in self.properties
                ],
                values=[
                    ast.Name(id=to_snake(property), ctx=ast.Load())
                    for property in self.properties
                ]
            )

        self.properties = self.lexicon.reorder_properties(
            self.properties, self.required
        )

        self.generator = CallGenerator(
            self.lexicon, self.properties,
            self.required, self.query_params, self.data, self.headers
        )

    def generate(self) -> ast.FunctionDef:
        return self.generator.generate()
