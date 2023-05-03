import ast
from typing import Union

from codegen.common import ANNOTATIONS_IMPORT
from codegen.common import FunctionInfo
from codegen.common import Generator
from codegen.common import generate_init_function_in_init_file
from codegen.common import to_private_class_name


class LeafInitGenerator(Generator):
    def __init__(self, current: str,
                 modules: list[str], functions: list[FunctionInfo]) -> None:
        self.current = current
        self.modules = modules
        self.functions = functions

    def generate(self) -> ast.Module:
        return ast.Module(
            body=self._generate_imports() + [
                self._generate_class()
            ],
            type_ignores=[]
        )

    def _generate_imports(self) -> list[ast.ImportFrom]:
        return [
            ANNOTATIONS_IMPORT
        ] + [
            ast.ImportFrom(
                module=module,
                names=[
                    ast.alias(name='*')
                ],
                level=1)
            for module in sorted(self.modules)
        ]

    def _generate_class(self) -> ast.ClassDef:
        return ast.ClassDef(
            name=to_private_class_name(self.current),
            bases=[],
            keywords=[],
            body=[
                generate_init_function_in_init_file()
            ] + [
                self._generate_function(function)
                for function in self.functions
            ],
            decorator_list=[]
        )

    def _generate_function(self, function: FunctionInfo) -> ast.FunctionDef:
        return ast.FunctionDef(
            name=function.name,
            args=self._generate_function_args(function),
            body=self._generate_function_body(function),
            decorator_list=[])

    def _generate_function_args(self, function) -> ast.arguments:
        args = [ast.arg(arg='self')]
        args += function.args
        return ast.arguments(
            posonlyargs=[],
            args=args,
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
                ast.Constant(value=None)
                for _ in range(function.none_count)
            ]
        )

    def _generate_function_body(self, function) -> list[ast.Return]:
        args: list[Union[ast.Attribute, ast.Name]] = [
            ast.Attribute(
                value=ast.Name(id='self', ctx=ast.Load()),
                attr='service',
                ctx=ast.Load()
            ),
            ast.Attribute(
                value=ast.Name(id='self', ctx=ast.Load()),
                attr='headers',
                ctx=ast.Load()
            )
        ]
        args += [
            ast.Name(id=arg.arg, ctx=ast.Load())
            for arg in function.args
        ]
        return [
            ast.Return(
                value=ast.Call(
                    func=ast.Name(id=function.name, ctx=ast.Load()),
                    args=args,
                    keywords=[]
                )
            )
        ]
