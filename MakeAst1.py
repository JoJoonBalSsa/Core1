import javalang
import os

import javalang.tree

def parse_java_files(folder_path):
    trees = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.java'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    source_code = file.read()
                tree = javalang.parse.parse(source_code)
                trees.append(tree)
    return trees

def track_variable_flow(trees, variable_name, method_name):
    # 변수 흐름을 저장할 리스트를 초기화합니다.
    variable_flows = []
    # 추적해야 할 변수와 메서드의 초기 리스트를 설정합니다.
    methods_to_check = [(variable_name, method_name)]
    # 모든 트리에서 메서드 선언을 수집하여 이름을 키로 갖는 사전을 생성합니다.
    method_nodes = {node.name: node for tree in trees for path, node in tree.filter(javalang.tree.MethodDeclaration)}

    # 추적할 변수가 있는 동안 반복합니다.
    while methods_to_check:
        # 리스트에서 변수와 메서드를 꺼냅니다.
        current_variable, current_method = methods_to_check.pop()
        # 현재 메서드 이름이 사전에 있는지 확인합니다.
        if current_method in method_nodes:
            # 사전에서 메서드 노드를 가져옵니다.
            method_node = method_nodes[current_method]
            # 메서드 노드를 처리하여 변수 흐름을 추적합니다.
            process_method_node(method_node, current_variable, current_method, variable_flows, methods_to_check)
    
    # 변수 흐름을 반환합니다.
    return variable_flows

def process_method_node(method_node, current_variable, current_method, variable_flows, methods_to_check):
    # 메서드 내부의 모든 노드를 순회합니다.
    for sub_path, sub_node in method_node:
        # 노드가 변수 할당인 경우
        if isinstance(sub_node, javalang.tree.Assignment):
            # 변수 할당을 처리합니다.
            process_assignment(sub_node, current_variable, current_method, variable_flows, methods_to_check)
        # 노드가 메서드 호출인 경우
        elif isinstance(sub_node, javalang.tree.MethodInvocation):
            # 메서드 호출을 처리합니다.
            process_method_invocation(sub_node, current_variable, current_method, variable_flows, methods_to_check)

def process_assignment(sub_node, current_variable, current_method, variable_flows, methods_to_check):
    # 변수 할당의 좌변이 추적 중인 변수인 경우
    if (isinstance(sub_node.expressionl, javalang.tree.MemberReference) and 
        sub_node.expressionl.member == current_variable):
        # 할당의 우변이 다른 변수인 경우
        if isinstance(sub_node.value, javalang.tree.MemberReference):
            # 변수 흐름을 저장하고, 우변 변수를 추적 리스트에 추가합니다.
            variable_flows.append((current_method, sub_node.expressionl.member, sub_node.value.member))
            methods_to_check.append((sub_node.value.member, current_method))
        # 할당의 우변이 리터럴인 경우
        elif isinstance(sub_node.value, javalang.tree.Literal):
            # 변수 흐름을 저장합니다.
            variable_flows.append((current_method, sub_node.expressionl.member, sub_node.value.value))
    
    # 할당의 좌변이 추적 중인 변수인 경우 (새로운 값으로 대체됨)
    if (isinstance(sub_node.expressionl, javalang.tree.MemberReference) and 
        sub_node.expressionl.member == current_variable):
        # 추적 리스트에서 해당 변수를 삭제합니다.
        methods_to_check = [(var, method) for var, method in methods_to_check if var != current_variable]

def process_method_invocation(sub_node, current_variable, current_method, variable_flows, methods_to_check):
    # 메서드 호출의 모든 인자를 순회합니다.
    for arg in sub_node.arguments:
        # 인자가 추적 중인 변수인 경우
        if isinstance(arg, javalang.tree.MemberReference) and arg.member == current_variable:
            # 변수 흐름을 저장하고, 호출된 메서드를 추적 리스트에 추가합니다.
            variable_flows.append((current_method, current_variable, sub_node.member))
            methods_to_check.append((arg.member, sub_node.member))
    
    # 메서드 호출의 주체가 추적 중인 변수인 경우
    if isinstance(sub_node.qualifier, javalang.tree.MemberReference) and sub_node.qualifier.member == current_variable:
        # 변수 흐름을 저장하고, 반환된 값을 추적 리스트에 추가합니다.
        variable_flows.append((current_method, current_variable, sub_node.member))
        methods_to_check.append((sub_node.member, sub_node.member))

def find_readline_variables(trees):
    # Console.readLine()으로 초기화된 변수를 저장할 리스트를 초기화합니다.
    readline_variables = []
    
    # 각 파싱된 자바 소스 코드 트리를 순회합니다.
    for tree in trees:
        # 트리에서 모든 MethodInvocation 노드를 필터링하여 순회합니다.
        for path, node in tree.filter(javalang.tree.MethodInvocation):
            # MethodInvocation 노드가 readLine 메서드를 호출하고, 그 주체가 Console인 경우를 찾습니다.
            if node.member == 'readLine' and node.qualifier == 'Console':
                # readLine 호출이 포함된 메서드 선언을 찾습니다.
                method_decl = next((n for n in path if isinstance(n, javalang.tree.MethodDeclaration)), None)
                if method_decl:
                    # 해당 메서드에서 Console.readLine()을 사용하여 초기화된 변수를 찾습니다.
                    readline_variables.extend(find_variables_with_readline(tree, method_decl))
    
    # Console.readLine()으로 초기화된 변수를 반환합니다.
    return readline_variables

def find_variables_with_readline(tree, method_decl):
    # 초기화된 변수를 저장할 리스트를 초기화합니다.
    variables = []
    # 트리에서 모든 VariableDeclarator 노드를 필터링하여 순회합니다.
    for path_assignment, node_assignment in tree.filter(javalang.tree.VariableDeclarator):
        # 초기화 구문이 readLine 메서드를 호출하고, 그 주체가 Console인 경우를 찾습니다.
        if (isinstance(node_assignment.initializer, javalang.tree.MethodInvocation) and 
            node_assignment.initializer.member == 'readLine' and 
            node_assignment.initializer.qualifier == 'Console' and 
            method_decl in path_assignment):
            # 변수를 리스트에 추가합니다.
            variables.append((node_assignment.name, method_decl.name))
    # 초기화된 변수 리스트를 반환합니다.
    return variables


def track_all_readline_variables(trees, readline_variables):
    all_variable_flows = {}
    
    for variable_name, method_name in readline_variables:
        all_variable_flows[variable_name] = track_variable_flow(trees, variable_name, method_name)
    
    return all_variable_flows

def main():
    java_folder_path = './christmas/src/main/java/christmas'  # Specify the folder containing Java files
    
    # Step 1: Parse all Java files
    trees = parse_java_files(java_folder_path)
    
    # Step 2: Find all variables initialized by Console.readLine()
    readline_variables = find_readline_variables(trees)
    
    # Step 3: Track the flow of each readline-initialized variable
    variable_flows = track_all_readline_variables(trees, readline_variables)
    
    # Step 4: Print the flows for each variable
    print(f"Variables storing Console.readLine() data are used in the following flows:")
    for var, flows in variable_flows.items():
        print(f"\nVariable: {var}")
        for method_name, from_var, to_var in flows:
            print(f"  Method: {method_name}, From: {from_var}, To: {to_var}")

if __name__ == "__main__":
    main()
