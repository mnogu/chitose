from collections import defaultdict
from typing import Union
import ast
import json
import os

from codegen.common import to_snake
from codegen.leaf import LeafInitGenerator
from codegen.main import CodeGenerator
from codegen.non_leaf import NonLeafInitGenerator


def main() -> None:
    warning_message = '# GENERATED CODE - DO NOT MODIFY\n'
    dirs = defaultdict(set)
    counts: defaultdict[str, int] = defaultdict(int)
    functions_dic = defaultdict(list)
    generator: Union[CodeGenerator, NonLeafInitGenerator, LeafInitGenerator]
    for root, _, files in os.walk('atproto/lexicons'):
        names = []
        for file in sorted(files):
            path = os.path.join(root, file)
            with open(path) as in_f:
                json_data = json.load(in_f)
            generator = CodeGenerator(json_data)
            obj = generator.generate()

            ast.fix_missing_locations(obj)

            id_parts = json_data['id'].split('.')
            name = to_snake(id_parts[-1])

            paths = ['chitose'] + id_parts[: -1]

            path = paths[0]
            for level in range(1, len(paths) - 1):
                path = os.path.join(path, paths[level])
                dirs[path].add(paths[level + 1])
                counts[path] += 0

            parent_dir = os.path.join(path, paths[-1])
            os.makedirs(parent_dir, exist_ok=True)
            counts[parent_dir] += 1
            functions_dic[parent_dir].extend(generator.get_functions())

            with open(os.path.join(parent_dir, f'{name}.py'), 'w') as out_f:
                out_f.write(warning_message)
                out_f.write(ast.unparse(obj))

            names.append(name)

    for path in counts:
        with open(os.path.join(path, '__init__.py'), 'w') as out_f:
            out_f.write(warning_message)

            current = os.path.basename(path)
            if counts[path] == 0:
                children = dirs[path]
                generator = NonLeafInitGenerator(current, children)
            else:
                functions = functions_dic[path]
                generator = LeafInitGenerator(current, functions)
            obj = generator.generate()
            ast.fix_missing_locations(obj)
            out_f.write(ast.unparse(obj))


if __name__ == '__main__':
    main()
