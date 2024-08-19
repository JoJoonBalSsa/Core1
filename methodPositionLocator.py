import ast

class methodPositionLocator(ast.NodeVisitor):
    def __init__(self, method_name):
        self.method_name = method_name
        self.start_lineno = None
        self.end_lineno = None

    def visit_FunctionDef(self, node):
        if node.name == self.method_name:
            # 메소드의 시작 위치 (FunctionDef 노드의 시작 위치)
            self.start_lineno = node.lineno

            # 메소드의 끝 위치 (마지막 본문 노드의 끝 위치)
            last_node = node.body[-1]
            while hasattr(last_node, 'body'):
                last_node = last_node.body[-1]
            
            self.end_lineno = last_node.end_lineno

        # 자식 노드 방문을 계속
        self.generic_visit(node)

def find_method_position(source_code, method_name):
    tree = ast.parse(source_code)
    locator = methodPositionLocator(method_name)
    locator.visit(tree)
    return {
        "start_line": locator.start_lineno,
        "end_line": locator.end_lineno
    }