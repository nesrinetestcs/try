import ast
import sys

def find_print_statements(filename):
    print_statements = []

    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for statement in node.body:
                if isinstance(statement, ast.Expr):
                    if isinstance(statement.value, ast.Call):
                        if isinstance(statement.value.func, ast.Name):
                            if statement.value.func.id in ['print', 'display', 'pprint']:
                                print_statements.append((node.name, ast.unparse(statement).strip()))
                        elif isinstance(statement.value.func, ast.Attribute):
                            if statement.value.func.attr in ['write']:
                                if hasattr(statement.value.func.value, 'id'):
                                    if statement.value.func.value.id == 'sys':
                                        if hasattr(statement.value.func.value, 'attr'):
                                            if statement.value.func.value.attr in ['stdout', 'stderr']:
                                                print_statements.append((node.name, ast.unparse(statement).strip()))

    return print_statements

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    print_statements = find_print_statements(filename)

    for function_name, statement in print_statements:
        print(f"In function '{function_name}': {statement}")
