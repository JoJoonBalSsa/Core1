import javalang
from extractor import methods

flow = []

def call2method(node, arg_index):
    invoked_method = node.member
    for target_class_method, target_method_nodes in methods.items():
        target_class_name, target_method_name = target_class_method
        if target_method_name == invoked_method:  # 문제: 메서드 이름은 같은데 클래스가 다르다면?
            for target_file_path, target_method_node in target_method_nodes:
                if len(target_method_node.parameters) > arg_index:
                    new_var_name = target_method_node.parameters[arg_index].name
                    return f"{target_class_name}.{invoked_method}", new_var_name
    return "UnknownClass." + invoked_method, None  # 만약 소스코드에 정의되지 않은 함수라면

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
                                            flow.append([class_method,var_decl.name])
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