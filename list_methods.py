import argparse
import ast
from pathlib import Path


def parse_file(filepath: str):
    with open(filepath) as file:
        node = ast.parse(file.read())

    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

    if not functions and not classes:
        return

    print("#" * 60)
    print("FILE:", filepath)

    if functions:
        print("\nFUNCTIONS:")

        for i, function in enumerate(functions, 1):
            print(f"  {i}.", function.name)

    if classes:
        print("\nCLASSES AND METHODS:")

        for i, class_ in enumerate(classes, 1):
            print(f"  {i}.", class_.name)
            methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
            for j, method in enumerate(methods, 1):
                print(f"    {i}.{j}.", method.name)

def main():
    parser = argparse.ArgumentParser("Lists all functions and methods defined "
                                     "in Python source files found based on input path.")
    parser.add_argument("input", nargs="?", type=Path, default=Path.cwd(),
                        help="Input directory or file path")
    args = parser.parse_args()

    path: Path = args.input
    if not path.is_dir():
        parse_file(str(path))
    else:
        for file in path.glob("**/*.py"):
            parse_file(str(file))


if __name__ == "__main__":
    main()
