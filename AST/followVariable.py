# count 신경쓰기!


import javalang
import os
from collections import defaultdict

methods = []
flow = []

# 예제 Source 함수 배열, 나중에 변경 가능
source_functions = ['Console.readLine']


def call2method(node,arg_index):
    invoked_method = node.member
    for target_class_method, target_method_nodes in methods.items():
        target_class_name, target_method_name = target_class_method
        if target_method_name == invoked_method: # 문제 : 메서드이름은 같은데 클래스가 다르다면??
            for target_file_path, target_method_node in target_method_nodes:
                if len(target_method_node.parameters) > arg_index: 
                    new_var_name = target_method_node.parameters[arg_index].name
                    return f"{target_class_name}.{invoked_method}", new_var_name
    return "UnknownClass."+invoked_method,None #만약 소스코드에 정의되지 않은 함수라면


def parse_java_files(folder_path):
    trees = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.java'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r',encoding='utf-8') as file:
                    source_code = file.read()
                tree = javalang.parse.parse(source_code)
                trees.append((file_path, tree))
    return trees

def extract_methods_and_find_tainted_variables(trees): #메서드 단위로 AST 노드 저장, Taint 변수 탐색 및 저장
    global methods
    count = 0
    methods = defaultdict(list)
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


def track_variable_flow(class_method, var_name, count=0): #변수 흐름 추적. (계속 추가 가능)
        global flow
        current_count=0
        # if (class_method == None): #예외처리
        #     flow.append(class_method,var_name)
        #     return
        

        class_name, method_name = class_method.split('.')
        flow.append([class_method,var_name]) # 흐름 추가

        method_nodes = methods.get((class_name, method_name), []) #메서드 단위로 저장해둔 노드로 바로바로 접근가능
        for file_path, method_node in method_nodes:
            for path, node in method_node: #노드 내부 탐색
                current_count +=1



                #######################################################################



                if isinstance(node, javalang.tree.Assignment): #변수 할당일 때
                    if isinstance(node.value, javalang.tree.MethodInvocation): # 2-2
                        if node.value.arguments:
                            for arg_index, arg in enumerate(node.value.arguments):
                                if isinstance(arg, javalang.tree.MemberReference) and arg.member == var_name and (count<current_count):
                                    flow.append([node.value.member,var_name])
                                    track_variable_flow(class_method,node.expressionl.member,current_count) # 같은 메서드에서 추적
                
                    if isinstance(node.value, javalang.tree.MethodInvocation) and (node.value.qualifier == var_name) and (count<current_count):
                        flow.append([node.value.member,var_name])
                        track_variable_flow(class_method,var_decl.name,current_count) # 같은 메서드에서 추적


                    if isinstance(node.expressionl, javalang.tree.MemberReference) and node.value.member == var_name and (count<current_count) : # 1-1
                        track_variable_flow(class_method,node.expressionl.member,current_count)

                    if isinstance(node.expressionl, javalang.tree.MemberReference) and node.expressionl.member == var_name and (count<current_count) : # 1-2
                        #초기화 값이 Source 함수일 경우 추가 필요
                        if count<current_count :
                            return
                



                #######################################################################




                elif isinstance(node, javalang.tree.LocalVariableDeclaration):  # 지역변수 선언
                        for var_decl in node.declarators:

                            if isinstance(var_decl.initializer, javalang.tree.MethodInvocation): # 2-2
                                if var_decl.initializer.arguments:
                                    for arg_index, arg in enumerate(var_decl.initializer.arguments):
                                        if isinstance(arg, javalang.tree.MemberReference) and arg.member == var_name and (count<current_count):
                                            #flow.append([class_method,var_name]) 이건 MethodInvocation 노드에서 추가할 듯
                                            track_variable_flow(class_method,var_decl.name,current_count) # 같은 메서드에서 추적

                            if isinstance(var_decl.initializer, javalang.tree.MethodInvocation):
                                if (var_decl.initializer.qualifier == var_name) and (count<current_count) : # 2-1
                                    flow.append([var_decl.initializer.member,var_name])
                                    track_variable_flow(class_method,var_decl.name,current_count) # 같은 메서드에서 추적

                            if isinstance(var_decl.initializer, javalang.tree.MemberReference) and var_decl.initializer.member == var_name and (count<current_count) :  # 1-1
                                track_variable_flow(class_method, var_decl.name,current_count)
                



                #######################################################################




                elif isinstance(node, javalang.tree.MethodInvocation): #메서드 호출일 때
                    if node.arguments: 
                        for arg_index, arg in enumerate(node.arguments):
                            if isinstance(arg, javalang.tree.MemberReference) and arg.member == var_name and (count<current_count) : # 4-1                       

                                class_method_2, var_name_2 = call2method(node,arg_index)
                                var_name_2 = var_name if var_name_2 == None else var_name_2 # 소스코드에 없는 메서드 호출시 var_name_2 가 None 이 되는경우 방지
                                flow.append([class_method_2,var_name_2])
                                track_variable_flow(class_method_2,var_name_2)




                #######################################################################                




                elif isinstance(node, javalang.tree.ForStatement): #for
                    if isinstance(node.control, javalang.tree.EnhancedForControl):
                        EFC = node.control
                        if EFC.iterable.member == var_name:
                            for var_decl in EFC.var.declarators:
                                if isinstance(var_decl, javalang.tree.VariableDeclarator) and (count<current_count) :
                                    var_name_2 = var_decl.name
                                    flow.append([class_method,var_name_2])
                                    track_variable_flow(class_method, var_name_2,current_count) # for 문 끝날때 까지만 추적하도록 수정 필요


                                

def numbering(d, key_tuple, value):
    if key_tuple in d:
        base_key1, base_key2 = key_tuple
        i = 1
        new_key = (base_key1, f"{base_key2}_{i}")
        while new_key in d:
            i += 1
            new_key = (base_key1, f"{base_key2}_{i}")
        d[new_key] = value
    else:
        d[key_tuple] = value


def main():
    global flow

    java_folder_path = 'C:/Users/조준형/Desktop/S개발자_프로젝트/Core1/AST/christmas'  # Specify the folder containing Java files
    
    # Step 1: Parse all Java files
    trees = parse_java_files(java_folder_path)
    # Step 2: Extract methods and find tainted variables
    tainted_variables = extract_methods_and_find_tainted_variables(trees)
    flows = {}
    for class_method, var , count in tainted_variables:
        flow = []
        track_variable_flow(class_method,var,count)
        numbering(flows,(class_method,var),flow) # 같은 메서드에 같은 이름의 taint 변수가 생길 경우
        # flows[class_method,var] = flow # 다른 클래스의 같은이름의 메서드가 있을수 있기 때문에 key값은 두 키워드(클래스,메서드) 사용


    for (class_method, var), value in flows.items():
        print("Tainted Variable: ")
        print(f"{class_method}, {var}")
        print("흐름 파악")
        for f in flows[class_method,var]:
            print(f)

        print()

    with open("result.txt", 'w', encoding='utf-8') as file: # 결과 파일 생성
        for class_method, var,count in tainted_variables:
            file.write("Tainted Variable:\n")
            file.write(f"{class_method}, {var}\n")
            file.write("흐름 파악\n")
            for f in flows[class_method, var]:
                file.write(f"{f}\n")
            file.write("\n")


if __name__ == "__main__":
    main()
