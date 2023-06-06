from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import Union
import ast


def to_snake(name: str) -> str:
    return ''.join(f'_{ch.lower()}' if ch.isupper()
                   else ch for ch in name)


def to_class_name(name: str) -> str:
    return f'{name[0].upper()}{name[1:]}'


# not private
def to_internal_class_name(name: str) -> str:
    return f'{to_class_name(name)}_'


def to_private_function_name(name: str) -> str:
    return f'_{to_snake(name)}'


def to_constant(name: str) -> str:
    return ''.join(f'_{ch}' if ch.isupper()
                   else ch.upper() for ch in name)


def to_description(lines: list[str], indent: int) -> str:
    if len(lines) == 1:
        return lines[0]

    prefix = '\n' + ' ' * indent
    description = ''
    for idx, line in enumerate(lines):
        if idx == 1:
            description += '\n'

        if idx != 0:
            description += prefix

        description += f'{line}\n'

    description += ' ' * indent

    return description


def generate_common_body_in_init_file() -> list[Union[ast.Expr, ast.FunctionDef]]:
    return [
        _class_docstring_in_init_file(),
        _init_function_in_init_file()

    ]


def _class_docstring_in_init_file() -> ast.Expr:
    value = ('We recommend calling methods in this class '
             'via the :doc:`chitose.BskyAgent <chitose>` class '
             'instead of creating instances of this class directly.')
    return ast.Expr(
        value=ast.Constant(value=value)
    )


def _init_function_in_init_file() -> ast.FunctionDef:
    return ast.FunctionDef(
        name='__init__',
        args=ast.arguments(
            posonlyargs=[],
            args=[
                ast.arg(arg='self'),
            ] + [
                ast.arg(
                    arg=arg,
                    annotation=ast.Name(id=name_id, ctx=ast.Load())
                )
                for arg, name_id in [
                    ('call', 'XrpcCall'),
                    ('subscribe', 'XrpcSubscribe')
                ]
            ],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
        body=[
            ast.Assign(
                targets=[
                    ast.Attribute(
                        value=ast.Name(id='self', ctx=ast.Load()),
                        attr=attr,
                        ctx=ast.Store()
                    )
                ],
                value=ast.Name(id=attr, ctx=ast.Load())
            )
            for attr in ['call', 'subscribe']
        ],
        decorator_list=[],
        returns=ast.Constant(value=None)
    )


ANNOTATIONS_IMPORT = ast.ImportFrom(
    module='__future__',
    names=[
        ast.alias(name='annotations')
    ],
    level=0
)

IMPORTS_IN_INIT_FILE = [
    ANNOTATIONS_IMPORT
] + [
    ast.ImportFrom(
        module='chitose.xrpc',
        names=[
            ast.alias(name=name)
        ],
        level=0
    )
    for name in ['XrpcCall', 'XrpcSubscribe']
]


class Generator(ABC):
    @abstractmethod
    def generate(self) -> Union[ast.Assign, ast.ClassDef,
                                ast.FunctionDef, ast.Module]:
        pass


@dataclass
class FunctionInfo:
    name: str
    description_lines: list[str]
    args: list[ast.arg]
    none_count: int
    modules: set[str]
    func: str  # call or subscribe
