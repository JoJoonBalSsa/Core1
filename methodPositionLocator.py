import javalang

class methodPositionLocator:
    def __init__(self, method_name):
        self.method_name = method_name
        self.start_position = None
        self.end_position = None

    def visit(self, tree):
        for path, node in tree.filter(javalang.tree.MethodDeclaration):
            if node.name == self.method_name:
                self.start_position = node.position
                # 메소드의 끝 위치를 찾기 위해 바디의 마지막 위치를 사용
                self.end_position = node.body[-1].position if node.body else node.position
                break

def find_method_position(source_code, method_name):
    try:
        tree = javalang.parse.parse(source_code)
        locator = methodPositionLocator(method_name)
        locator.visit(tree)
        return {
            "start_line": locator.start_position.line if locator.start_position else None,
            "end_line": locator.end_position.line if locator.end_position else None
        }
    except javalang.parser.JavaSyntaxError as e:
        print(f"Java 구문 오류: {e}")
        return None