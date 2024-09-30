import os
import javalang

def parse_java_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()
    return javalang.parse.parse(source_code)

def format_node(node, indent=''):
    if isinstance(node, javalang.tree.CompilationUnit):
        return 'CompilationUnit\n' + format_nodes(node.imports, indent + '│   ') + format_node(node.package, indent + '│   ') + format_nodes(node.types, indent + '└── ')
    if isinstance(node, javalang.tree.Import):
        return f"{indent}Import(path={node.path}, static={node.static}, wildcard={node.wildcard})\n"
    if isinstance(node, javalang.tree.PackageDeclaration):
        return f"{indent}PackageDeclaration(name={node.name})\n"
    if isinstance(node, javalang.tree.ClassDeclaration):
        return f"{indent}ClassDeclaration(name={node.name}, modifiers={node.modifiers})\n" + format_nodes(node.body, indent + '├── ')
    if isinstance(node, javalang.tree.ConstructorDeclaration):
        return f"{indent}ConstructorDeclaration(name={node.name})\n" + format_nodes(node.body, indent + '│   ')
    if isinstance(node, javalang.tree.MethodDeclaration):
        return f"{indent}MethodDeclaration(name={node.name}, modifiers={node.modifiers})\n" + format_nodes(node.body, indent + '│   ')
    if isinstance(node, javalang.tree.FormalParameter):
        return f"{indent}FormalParameter(type={node.type.name}, name={node.name})\n"
    if isinstance(node, javalang.tree.LocalVariableDeclaration):
        return f"{indent}LocalVariableDeclaration(type={node.type.name}, name={node.declarators[0].name}, initializer={node.declarators[0].initializer})\n"
    if isinstance(node, javalang.tree.VariableDeclarator):
        initializer = f", initializer={node.initializer}" if node.initializer else ""
        return f"{indent}VariableDeclarator(name={node.name}{initializer})\n"
    if isinstance(node, javalang.tree.MethodInvocation):
        return f"{indent}MethodInvocation(qualifier={node.qualifier}, member={node.member})\n"
    if isinstance(node, javalang.tree.Assignment):
        return f"{indent}Assignment(target={node.expressionl}, value={node.value})\n"
    if isinstance(node, javalang.tree.WhileStatement):
        return f"{indent}WhileStatement(condition={node.condition})\n" + format_nodes(node.body, indent + '│   ')
    if isinstance(node, javalang.tree.TryStatement):
            formatted = f"{indent}TryStatement\n"
            formatted += indent + '│   ' + 'Resources:\n' + format_nodes(node.resources, indent + '│   │   ')
            formatted += indent + '│   ' + 'Block:\n' + format_nodes(node.block, indent + '│   │   ')
            formatted += indent + '│   ' + 'Catches:\n' + format_nodes(node.catches, indent + '│   │   ')
            if node.finally_block is not None:
                formatted += indent + '│   ' + 'Finally:\n' + format_nodes(node.finally_block, indent + '│   │   ')
            return formatted
    if isinstance(node, javalang.tree.CatchClause):
        return f"{indent}CatchClause(parameter={node.parameter.name})\n" + format_nodes(node.block, indent + '│   ')
    if isinstance(node, javalang.tree.ReturnStatement):
        return f"{indent}ReturnStatement({node.expression})\n"
    if isinstance(node, javalang.tree.BlockStatement):
        return format_nodes(node.statements, indent)
    return f"{indent}{node}\n"

def format_nodes(nodes, indent=''):
    if nodes is None:
        return ''
    return ''.join(format_node(node, indent) for node in nodes if node is not None)

def write_ast_to_file(file_path):
    ast = parse_java_file(file_path)
    output_file = file_path + ".txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        formatted_ast = format_node(ast)
        file.write(formatted_ast)

def analyze_java_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.java'):
                file_path = os.path.join(root, file_name)
                print(f"\n파일 파싱 중: {file_path}")
                try:
                    write_ast_to_file(file_path)
                    print(f"AST를 {file_path}.txt에 저장했습니다.")
                except javalang.parser.JavaSyntaxError as e:
                    print(f"구문 오류가 발생한 파일: {file_path}")
                    print(e)
                except javalang.tokenizer.LexerError as e:
                    print(f"토큰화 오류가 발생한 파일: {file_path}")
                    print(e)

def main():
    java_folder_path = '박하은_크리스마스'  # 분석할 자바 폴더 경로
    analyze_java_folder(java_folder_path)

if __name__ == "__main__":
    main()