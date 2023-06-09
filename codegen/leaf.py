import ast
from typing import Union

from codegen.common import IMPORTS_IN_INIT_FILE
from codegen.common import FunctionInfo
from codegen.common import Generator
from codegen.common import generate_common_body_in_init_file
from codegen.common import to_description
from codegen.common import to_internal_class_name
from codegen.common import to_private_function_name


class LeafInitGenerator(Generator):
    def __init__(self, current: str, functions: list[FunctionInfo]) -> None:
        self.current = current
        self.functions = functions

    def generate(self) -> ast.Module:
        return ast.Module(
            body=self._imports() + [
                self._class()
            ],
            type_ignores=[]
        )

    def _imports(self) -> list[Union[ast.ImportFrom, ast.Import]]:
        modules = set()
        for function in self.functions:
            modules |= function.modules

        return IMPORTS_IN_INIT_FILE + [
            ast.ImportFrom(
                module=function.name,
                names=[
                    ast.alias(name=to_private_function_name(function.name))
                ],
                level=1)
            for function in sorted(self.functions, key=lambda f: f.name)
        ] + [
            ast.Import(
                names=[
                    ast.alias(name=module)
                ]
            )
            for module in sorted(list(modules))
        ]

    def _class(self) -> ast.ClassDef:
        return ast.ClassDef(
            name=to_internal_class_name(self.current),
            bases=[],
            keywords=[],
            body=generate_common_body_in_init_file() + [
                self._function(function)
                for function in self.functions
            ],
            decorator_list=[]
        )

    def _is_subscription(self, function: FunctionInfo) -> bool:
        return function.func == 'subscribe'

    def _function(self, function: FunctionInfo) -> ast.FunctionDef:
        returns: Union[ast.Constant, ast.Name]
        if self._is_subscription(function):
            returns = ast.Constant(value=None)
        else:
            returns = ast.Name(id='bytes', ctx=ast.Load())

        return ast.FunctionDef(
            name=function.name,
            args=self._function_args(function),
            body=self._function_body(function),
            decorator_list=[],
            returns=returns
        )

    def _function_args(self, function: FunctionInfo) -> ast.arguments:
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

    def _function_body(self, function: FunctionInfo) \
            -> list[Union[ast.Expr, ast.Return]]:
        args: list[Union[ast.Attribute, ast.Name]] = [
            ast.Attribute(
                value=ast.Name(id='self', ctx=ast.Load()),
                attr=function.func,
                ctx=ast.Load()
            ),
        ]
        args += [
            ast.Name(id=arg.arg, ctx=ast.Load())
            for arg in function.args
        ]
        description = ast.Expr(
            value=ast.Constant(
                value=to_description(function.description_lines, 8),
            )
        )
        value = ast.Call(
            func=ast.Name(id=to_private_function_name(
                function.name), ctx=ast.Load()),
            args=args,
            keywords=[]
        )
        if self._is_subscription(function):
            return [
                description,
                ast.Expr(value=value)
            ]

        return [
            description,
            ast.Return(
                value=value
            )
        ]
