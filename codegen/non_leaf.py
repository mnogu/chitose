import ast

from codegen.common import ANNOTATIONS_IMPORT
from codegen.common import XRPC_CALLABLE_IMPORT
from codegen.common import Generator
from codegen.common import generate_common_body_in_init_file
from codegen.common import to_internal_class_name


class NonLeafInitGenerator(Generator):
    def __init__(self, current: str, children: set[str]) -> None:
        self.current = current
        self.children = sorted(children)

    def generate(self) -> ast.Module:
        return ast.Module(
            body=self._imports() + [
                self._class(),
            ],
            type_ignores=[]
        )

    def _imports(self) -> list[ast.ImportFrom]:
        return [
            ANNOTATIONS_IMPORT,
            XRPC_CALLABLE_IMPORT,
        ] + [
            ast.ImportFrom(
                module=child,
                names=[
                    ast.alias(name=to_internal_class_name(child))
                ],
                level=1
            )
            for child in self.children
        ]

    def _class(self) -> ast.ClassDef:
        return ast.ClassDef(
            name=to_internal_class_name(self.current),
            bases=[],
            keywords=[],
            body=generate_common_body_in_init_file()
            + self._property(),
            decorator_list=[]
        )

    def _property(self) -> list[ast.FunctionDef]:
        return [
            ast.FunctionDef(
                name=child,
                args=ast.arguments(
                    posonlyargs=[],
                    args=[
                        ast.arg(arg='self')],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[]),
                body=[
                    ast.Return(
                        value=ast.Call(
                            func=ast.Name(id=to_internal_class_name(
                                child), ctx=ast.Load()),
                            args=[
                                ast.Attribute(
                                    value=ast.Name(id='self', ctx=ast.Load()),
                                    attr='call',
                                    ctx=ast.Load())
                            ],
                            keywords=[]
                        )
                    )
                ],
                decorator_list=[
                    ast.Name(id='property', ctx=ast.Load())
                ]
            )
            for child in self.children
        ]
