from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
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


def generate_init_function_in_init_file():
    return ast.FunctionDef(
        name='__init__',
        args=ast.arguments(
            posonlyargs=[],
            args=[
                ast.arg(arg='self'),
                ast.arg(
                    arg='service',
                    annotation=ast.Name(id='str', ctx=ast.Load())
                ),
                ast.arg(
                    arg='headers',
                    annotation=ast.Subscript(
                        value=ast.Name(id='dict', ctx=ast.Load()),
                        slice=ast.Tuple(
                            elts=[
                                ast.Name(id='str', ctx=ast.Load()),
                                ast.Name(id='str', ctx=ast.Load())
                            ],
                            ctx=ast.Load()
                        ),
                        ctx=ast.Load()
                    )
                )
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
            for attr in ['service', 'headers']
        ],
        decorator_list=[])


ANNOTATIONS_IMPORT = ast.ImportFrom(
    module='__future__',
    names=[
        ast.alias(name='annotations')
    ],
    level=0
)


class Generator(ABC):
    @abstractmethod
    def generate(self):
        pass


@dataclass
class FunctionInfo:
    name: str
    description_lines: list[str]
    args: list[ast.arg]
    none_count: int
