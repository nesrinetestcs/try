import ast
import sys

def extract_prints(file_path):
    prints = []

    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_name = node.name
                for statement in node.body:
                    if isinstance(statement, ast.Expr):
                        if isinstance(statement.value, ast.Call):
                            call_func = statement.value.func
                            if isinstance(call_func, ast.Name):
                                func_name = call_func.id
                                if func_name in ['print', 'write', 'display', 'pprint']:
                                    print_value = ast.literal_eval(ast.Str(statement.value.args[0].s))
                                    prints.append((func_name, print_value))

    return prints

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_to_check.py>")
        sys.exit(1)

    file_path = sys.argv[1]
    prints = extract_prints(file_path)

    if prints:
        print("Found prints:")
        for func, value in prints:
            print(f"{func}: {value}")
    else:
        print("No prints found.")
