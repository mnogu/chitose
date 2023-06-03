import ast
from typing import Union

from codegen.array import ArrayGenerator
from codegen.common import ANNOTATIONS_IMPORT
from codegen.common import FunctionInfo
from codegen.common import Generator
from codegen.lexicon import Lexicon
from codegen.object import ObjectGenerator
from codegen.procedure import ProcedureGenerator
from codegen.query import QueryGenerator
from codegen.record import RecordGenerator
from codegen.string import StringGenerator
from codegen.subscription import SubscriptionGenerator
from codegen.token import TokenGenerator


class CodeGenerator(Generator):
    def __init__(self, json_data) -> None:
        self.json_data = json_data
        assert json_data['lexicon'] == 1
        self.modules: set[str] = set()
        self.functions: list[FunctionInfo] = []

    def get_functions(self) -> list[FunctionInfo]:
        return self.functions

    def generate(self) -> ast.Module:
        body: list[Union[ast.ClassDef, ast.FunctionDef,
                         ast.ImportFrom, ast.Import, ast.Assign, ast.Expr]] = []
        for def_id in self.json_data['defs']:
            self.def_id = def_id
            self.current = self.json_data['defs'][def_id]

            lexicon = Lexicon(self.json_data['id'], def_id, self.current)
            type_ = self.current['type']
            elem: Union[ast.ClassDef, ast.FunctionDef, ast.Assign]
            generator: Generator
            if type_ == 'query':
                generator = QueryGenerator(lexicon)
            elif type_ == 'procedure':
                generator = ProcedureGenerator(lexicon)
            elif type_ == 'object':
                generator = ObjectGenerator(lexicon)
            elif type_ == 'record':
                generator = RecordGenerator(lexicon)
            elif type_ == 'subscription':
                generator = SubscriptionGenerator(lexicon)
            elif type_ == 'string':
                generator = StringGenerator(lexicon)
            elif type_ == 'token':
                generator = TokenGenerator(lexicon)
            elif type_ == 'array':
                generator = ArrayGenerator(lexicon)
            else:
                assert False, type_

            elem = generator.generate()

            self.modules |= lexicon.get_modules()
            self.functions += lexicon.get_functions()

            body.append(elem)

        body = [self._module_docstring()] \
            + self._imports() \
            + body

        return ast.Module(
            body=body,
            type_ignores=[]
        )

    def _module_docstring(self) -> ast.Expr:
        return ast.Expr(
            value=ast.Constant(value=self.json_data.get('description', ''))
        )

    def _imports(self) -> list[Union[ast.ImportFrom, ast.Import]]:
        imports: list[Union[ast.ImportFrom, ast.Import]] = [
            ANNOTATIONS_IMPORT
        ]
        imports += [
            ast.Import(
                names=[
                    ast.alias(name=module)
                ]
            )
            for module in sorted(list(self.modules))
        ]
        return imports
