import javalang
from collections import defaultdict

source_functions = ['Console.readLine']
methods = defaultdict(list)

def extract_methods_and_find_tainted_variables(trees): #메서드 단위로 AST 노드 저장, Taint 변수 탐색 및 저장
    global methods
    count = 0
    tainted_variables = []

    for file_path, tree in trees:
        current_class = "UnknownClass"
        for path, node in tree:
            count = 0
            if isinstance(node, javalang.tree.ClassDeclaration):
                current_class = node.name
            elif isinstance(node, javalang.tree.MethodDeclaration):
                method_name = node.name
                methods[(current_class, method_name)].append((file_path, node))
                
                for sub_path, sub_node in node:
                    count +=1 # 각각의 taint 변수가 생겨난 지점 식별
                    if isinstance(sub_node, javalang.tree.VariableDeclarator):# 변수 선언 및 정의
                        if isinstance(sub_node.initializer, javalang.tree.MethodInvocation):
                            invoked_method = f"{sub_node.initializer.qualifier}.{sub_node.initializer.member}" if sub_node.initializer.qualifier else sub_node.initializer.member
                            if invoked_method in source_functions:  
                                tainted_variables.append((f"{current_class}.{method_name}", sub_node.name , count))
                    elif isinstance(sub_node, javalang.tree.Assignment): #변수 할당일 때
                        if isinstance(sub_node.value, javalang.tree.MethodInvocation):
                            invoked_method = f"{sub_node.value.qualifier}.{sub_node.value.member}" if sub_node.value.qualifier else sub_node.value.member
                            if invoked_method in source_functions: 
                                tainted_variables.append((f"{current_class}.{method_name}", sub_node.expressionl.member , count))

    
    return tainted_variables