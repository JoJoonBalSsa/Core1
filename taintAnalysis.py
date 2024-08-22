import javalang
import os
from collections import defaultdict
from analysisResultManager import analysisResultManager
from methodPositionLocator import methodPositionLocator

class taintAnalysis:
    __methods = defaultdict(list)
    __source_functions = {
        # 사용자 입력
        'next': 1,
        'nextLine': 1,
        'nextInt': 1,
        'nextDouble': 1,
        'readLine': 1,
        'nextBoolean': 1,
        'nextFloat': 1,
        'nextLong': 1,
        'nextByte': 1,
        'nextShort': 1,

        # 네트워크 입력
        'getInputStream': 1.5,
        'getParameter': 1,
        'getParameterMap': 1.5,
        'getHeader': 1,
        'getCookies': 1,
        'getQueryString': 1,
        'getRemoteAddr': 1,
        'getRemoteHost': 1,
        'getRequestURI': 1,
        'getRequestURL': 1,
        'getMethod': 0.5,
        'getContentType': 0.5,
        'getContextPath': 0.5,
        'getServerName': 0.5,

        # 환경 변수
        'getProperty': 1.5,
        'getenv': 1.5,
        'getProperties': 1,
        'getSecurityManager': 1,

        # 데이터베이스 입력
        'getString': 1.5,
        'getInt': 1.5,
        'getDouble': 1.5,
        'executeQuery': 1.5,
        'queryForObject': 1.5,
        'queryForList': 1.5,
        'getBlob': 1.5,
        'getClob': 1.5,
        'getDate': 1.5,
        'getTime': 1.5,
        'getTimestamp': 1.5,
        'getBoolean': 1.5,
        'getByte': 1.5,
        'getShort': 1.5,
        'getLong': 1.5,
        'getFloat': 1.5,

        # API 및 라이브러리 호출
        'getData': 1,
        'sendRequest': 1,
        'getApiResponse': 1,
        'executeMethod': 1,
        'invokeMethod': 1,
        'callService': 1,

        # 세션 데이터
        'getAttribute': 1.5,
        'getCreationTime': 1,
        'getLastAccessedTime': 1,
        'getMaxInactiveInterval': 1,
        'isNew': 1,
        'getId': 1,

        # 파일 입력
        'readAllBytes': 1,
        'readObject': 1,
        'read': 1,
        'readLine': 1,
        'readAllLines': 1,
        'readString': 1,
        'readFully': 1,
        'readUTF': 1,

        # XML 처리
        'parse': 0.5,
        'getElementsByTagName': 0.5,
        'getChildNodes': 0.5,
        'getNodeValue': 0.5,
        'getAttributes': 0.5,

        # JSON 처리
        'getJSONObject': 1,
        'getJSONArray': 1,
        'getString': 1,
        'getInt': 1,
        'getBoolean': 1,

        # 시스템 및 런타임
        'getRuntime': 0.5,
        'getProcessors': 0.5,
        'getFreeMemory': 0.5,
        'getTotalMemory': 0.5,
        'getMaxMemory': 0.5,

        # 리플렉션
        'getMethod': 0.5,
        'getField': 0.5,
        'getConstructor': 0.5,
        'getAnnotation': 0.5,

        # 로깅
        'getLogger': 0.5,
        'getLevel': 0.5,
        'getName': 0.5,

        # 기타 소스
        'getResourceBundle': 0.5,
        'getRequestParameter': 0.5,
        'getResource': 0.5,
        'getResourceAsStream': 0.5,
        'getClassLoader': 0.5,
        'getSystemClassLoader': 0.5,
        'getParent': 0.5,
        'getPackage': 0.5,
        'getImplementationVersion': 0.5,

        # 파일 시스템 작업
        'listFiles': 0.5,
        'getAbsolutePath': 0.5,
        'getCanonicalPath': 0.5,
        'getParentFile': 0.5,
        'isDirectory': 0.5,
        'isFile': 0.5,
        'exists': 0.5,
        'lastModified': 0.5,
        'length': 0.5,

        # NIO 작업
        'readAttributes': 0.5,
        'newDirectoryStream': 0.5,
        'newBufferedReader': 0.5,
        'newBufferedWriter': 0.5,
        'readSymbolicLink': 0.5,
        'getFileStore': 0.5,

        # 네트워크 및 URL
        'openConnection': 1,
        'getResponseCode': 1,
        'getContentLength': 1,
        'getHeaderFields': 1,
        'getProtocol': 0.5,
        'getHost': 0.5,
        'getPort': 0.5,
        'getPath': 0.5,

        # 암호화 및 보안
        'getEncoded': 1.5,
        'getAlgorithm': 1.5,
        'getPublic': 1.5,
        'getPrivate': 1.5,
        'getModulus': 1.5,
        'getExponent': 1.5,

        # 날짜 및 시간
        'getYear': 0.5,
        'getMonth': 0.5,
        'getDayOfMonth': 0.5,
        'getHour': 0.5,
        'getMinute': 0.5,
        'getSecond': 0.5,
        'getZone': 0.5,
        'toEpochMilli': 0.5,

        # JDBC 확장
        'getMetaData': 1,
        'getColumnCount': 1,
        'getColumnName': 1,
        'getColumnType': 1,
        'getFetchSize': 1,
        'getWarnings': 1,

        # Java Beans
        'getPropertyDescriptors': 0.5,
        'getReadMethod': 0.5,
        'getWriteMethod': 0.5,
        'getPropertyType': 0.5,

        # 국제화
        'getLocale': 0.5,
        'getCountry': 0.5,
        'getLanguage': 0.5,
        'getDisplayName': 0.5,
        'getAvailableLocales': 0.5,

        # 자바 관리 확장 (JMX)
        'getMBeanInfo': 1,
        'getAttributes': 1,
        'getOperations': 1,
        'getNotifications': 1,

        # JNDI
        'getNameInNamespace': 0.5,
        'getNameParser': 0.5,
        'getInitialContext': 0.5,

        # AWT 및 Swing
        'getGraphics': 0.5,
        'getFontMetrics': 0.5,
        'getPreferredSize': 0.5,
        'getBackground': 0.5,
        'getForeground': 0.5,

        # RMI
        'getRegistry': 1,
        'lookup': 1,
        'getClientHost': 1,

        # 애노테이션 처리
        'getAnnotationsByType': 0.5,
        'getDeclaredAnnotations': 0.5,
        'getAnnotationMirrors': 0.5,

        # JAX-WS 및 웹 서비스
        'getPort': 1,
        'getPortName': 1,
        'getServiceName': 1,
        'getWsdlLocation': 1,

        # JPA
        'getPersistenceContext': 1,
        'getFlushMode': 1,
        'getLockMode': 1,
        'getReference': 1,

        # Java 가상 머신
        'getThreadInfo': 1,
        'getHeapMemoryUsage': 1,
        'getNonHeapMemoryUsage': 1,
        'getThreadCpuTime': 1,
    }

    __sink_functions = {
        # 콘솔 출력
        'print': 0.5,
        'println': 0.5,
        'printf': 0.5,
        'write': 0.5,

        # 파일 출력
        'FileOutputStream': 1,
        'FileWriter': 1,
        'BufferedWriter': 1,
        'PrintWriter': 1,
        'OutputStreamWriter': 1,
        'DataOutputStream': 1,
        'writeBytes': 1,
        'writeChars': 1,
        'writeUTF': 1,

        # 네트워크 출력
        'getOutputStream': 1.5,
        'write': 1.5,

        # 데이터베이스 업데이트
        'executeUpdate': 1.5,
        'execute': 1.5,

        # 로그 출력
        'log': 0.5,
        'info': 0.5,
        'warn': 0.5,
        'error': 0.5,

        # API 응답
        'getWriter': 1.5,
        'getOutputStream': 1.5,
        'write': 1.5,
        'sendRedirect': 1,
        'addHeader': 1,
        'setHeader': 1,
        'setStatus': 1,
        'setContentType': 1,

        # GUI 출력
        'setText': 0.5
    }   


    __tainted_variables = []
    __flow = []
    flows = defaultdict(list)
    source_check = []
    

    #메서드 단위로 AST 노드 저장, Taint 변수 탐색 및 저장
    def __init__(self, java_folder_path, analysis_result_manager):
        self.java_folder_path = java_folder_path
        self.analysis_result_manager = analysis_result_manager
        self.current_path = None
        self.current_source_code = None
        self.json_path = "resultData.json"

        # Step 1: Parse all Java files
        trees = self.__parse_java_files()

        # Step 2: Extract methods and find tainted variables
        self.__taint_analysis(trees)

        # Step 3: Append flow
        self.__append_flow()



    def _priority_flow(self):
        prioritized_flows = []
        
        for (class_method, var), value in self.flows.items():
            for flow in self.flows[(class_method, var)]:
                # 흐름에서 첫 번째 항목 (source)와 마지막 항목 (sink)을 가져옴
                source_full = flow[0][0] 
                sink_full = flow[-1][0]  

                # 'a.b.c'에서 'c' 부분 추출
                source = source_full.split('.')[-1]
                sink = sink_full.split('.')[-1]

                # source와 sink의 민감도 값을 가져옴
                source_sensitivity = self.__source_functions.get(source, 0)  
                sink_sensitivity = self.__sink_functions.get(sink, 0)       

                total_sensitivity = source_sensitivity + sink_sensitivity

                # 민감도를 0.5 단위로 반올림하여 1, 2, 3 중 하나로 설정
                rounded_sensitivity = round(total_sensitivity / 1.5) * 1.5

                # 민감도를 흐름 앞에 삽입
                prioritized_flow = [int(round(rounded_sensitivity))] + flow
                prioritized_flows.append(prioritized_flow)

        # 우선순위에 따라 flows를 정렬
        prioritized_flows.sort(reverse=True, key=lambda x: x[0])
        '''
        # 최종 결과 출력 (필요에 따라 반환하거나 다른 용도로 사용)
        for flow in prioritized_flows:
            print(flow)
        '''
        return prioritized_flows



    def __parse_java_files(self):
        """ Parse all Java files in the given folder and return a list of parsed ASTs. """
        trees = []
        for root, _, files in os.walk(self.java_folder_path):
            for file_name in files:
                if file_name.endswith('.java'):
                    file_path = os.path.join(root, file_name)
                    with open(self.current_path, 'r', encoding='utf-8') as file:
                        self.current_source_code = file.read()
                    tree = javalang.parse.parse(self.current_source_code)
                    trees.append((file_path, tree))
        return trees


    def __taint_analysis(self, trees):
        for file_path, tree in trees:
            current_class = "UnknownClass"
            for path, node in tree:
                if isinstance(node, javalang.tree.ClassDeclaration):
                    current_class = node.name

                elif isinstance(node, javalang.tree.MethodDeclaration):
                    self.__extract_methods(node, current_class, file_path)
                
                elif isinstance(node, javalang.tree.ConstructorDeclaration):
                    self.__extract_methods(node, current_class, file_path)


    def __extract_methods(self, node, current_class, file_path):
        method_name = node.name
        self.__methods[(current_class, method_name)].append((file_path, node))

        count = 0
        for sub_path, sub_node in node:
            count +=1 # 각각의 taint 변수가 생겨난 지점 식별
            self.__extract_variables(sub_node, current_class, method_name, count)
            
    
    def __extract_variables(self, sub_node, current_class, method_name, count):
        # 변수 선언 및 정의일 때
        if isinstance(sub_node, javalang.tree.VariableDeclarator): 
            if isinstance(sub_node.initializer, javalang.tree.MethodInvocation):
                if sub_node.initializer.member in self.__source_functions:
                    self.__tainted_variables.append((f"{current_class}.{method_name}.{sub_node.initializer.member}", sub_node.name , count))
                    self.source_check.append((sub_node.name,sub_node.initializer.member,sub_node.initializer.qualifier))
                
            elif isinstance(sub_node.initializer, javalang.tree.ClassCreator):
                for arg in sub_node.initializer.arguments:
                    if isinstance(arg, javalang.tree.ClassCreator):
                        for inner_arg in arg.arguments:
                            if isinstance(inner_arg, javalang.tree.MethodInvocation):
                                if inner_arg.member in self.__source_functions:
                                    self.__tainted_variables.append((f"{current_class}.{method_name}.{inner_arg.member}", sub_node.name, count))
                                    self.source_check.append((sub_node.name, inner_arg.member, inner_arg.qualifier))

        #변수 할당일 때
        elif isinstance(sub_node, javalang.tree.Assignment): 
            if isinstance(sub_node.value, javalang.tree.MethodInvocation):
                if sub_node.value.member in self.__source_functions: 
                    self.__tainted_variables.append((f"{current_class}.{method_name}.{sub_node.value.member}", sub_node.expressionl.member , count))
                    self.source_check.append((sub_node.expressionl.member,sub_node.value.member,sub_node.value.qualifier))

        #TRY문 
        elif isinstance(sub_node, javalang.tree.TryResource):
            if isinstance(sub_node.value, javalang.tree.ClassCreator):
                for arg in sub_node.value.arguments:
                    if isinstance(arg, javalang.tree.ClassCreator):
                        for inner_arg in arg.arguments:
                            if isinstance(inner_arg, javalang.tree.MethodInvocation):
                                if inner_arg.member in self.__source_functions:
                                    self.__tainted_variables.append((f"{current_class}.{method_name}.{inner_arg.member}", sub_node.name, count))
        

        
    def __append_flow(self):
        for class_method, var, count in self.__tainted_variables:
            self.__flow.clear()
            self.__track_variable_flow(class_method, var, count)


    def __numbering(self, d, key_tuple):
        if key_tuple in d:
            base_key1, base_key2 = key_tuple
            i = 1
            new_key = (base_key1, f"{base_key2}_{i}")
            while new_key in d:
                i += 1
                new_key = (base_key1, f"{base_key2}_{i}")
            return new_key
        else:
            return key_tuple
        

    






    def _get_cut_tree(self, method_name):
        # ... 메서드의 AST를 자른 값을 반환하는 로직 ...
        for path, node in self.__methods:
            if isinstance(node, javalang.tree.MethodDeclaration) and node == method_name:
                return node





    def _extract_method_source_code(self, method_node):
        start_position = method_node.position
        end_position = self.find_method_end_position(method_node)
        method_lines = self.current_source_code.splitlines()[start_position.line - 1:end_position.line]
        return '\n'.join(method_lines)

 
    def __track_variable_flow(self, tree, class_method, var_name, count=0): #변수 흐름 추적. (계속 추가 가능)
        class_name, method_name = class_method.split('.')
        self.__flow.append(class_method) # 흐름 추가

        method_nodes = self.__methods.get((class_name, method_name), []) #메서드 단위로 저장해둔 노드로 바로바로 접근가능
        
        current_count=0
        for file_path, method_node in method_nodes:
            for path, node in method_node: #노드 내부 탐색
                current_count +=1

                # sink 탐색
                if isinstance(node, javalang.tree.MethodInvocation):
                    self.__if_find_sink(node, class_method, var_name, count, current_count)
                    print(node)

                #변수 할당일 때
                if isinstance(node, javalang.tree.Assignment): 
                    self.__if_variable_assignment(node, class_method, var_name, count, current_count)

                # 지역변수 선언일 때
                elif isinstance(node, javalang.tree.LocalVariableDeclaration):  
                    self.__if_local_variable_declaration(node, class_method, var_name, count, current_count)

                # 메서드 호출일 때
                elif isinstance(node, javalang.tree.MethodInvocation):
                    self.__if_call_method(node, var_name, count, current_count)

                # for 문일 때
                elif isinstance(node, javalang.tree.ForStatement): 
                    self.__if_for_statement(node, class_method, var_name, count, current_count)

        if self.__flow:
            self.__flow.pop()
            
        
    def __if_find_sink(self, node, class_method, var_name, count, current_count):
        parts = class_method.split('.')
        class_name = parts[0]  
        method_name = parts[1] 
        
        if count>current_count:
                return
        
        if node.member in self.__sink_functions and node.arguments:
            flow_added = False
            
            for arg in node.arguments:
                # 인자가 하나일 때
                if isinstance(arg, javalang.tree.MemberReference):
                    if arg.member == var_name:
                        flow_added = True
                        break
                # 인자가 피연산자 중 하나일 때
                else:
                    flow_added = self.__judge_binary_operation(arg, flow_added, var_name)
                    if flow_added == True:
                       break

            if flow_added:
                self.__flow.append(f"{method_name}.{node.member}")
                # 새로운 키를 생성하고, 기존 키가 존재하면 새 키를 사용
                existing_key = (class_method, var_name)
                new_key = self.__numbering(self.flows, existing_key)
                if new_key not in self.flows:
                    self.flows[new_key] = []
                # flows에 __flow 복사
                self.flows[new_key].append(self.__flow[:])
                self.__flow.pop()      


    def __judge_binary_operation(self, arg, flow_added, var_name):
        if isinstance(arg, javalang.tree.BinaryOperation):
            if isinstance(arg.operandl, javalang.tree.MemberReference):
                if arg.operandl.member == var_name:
                    flow_added = True
                    return  flow_added# 하나의 인자만 확인하면 충분
            elif isinstance(arg.operandr, javalang.tree.MemberReference):
                if arg.operandr.member == var_name:
                    flow_added = True
                    return  flow_added# 하나의 인자만 확인하면 충분
            elif isinstance(arg.operandl, javalang.tree.BinaryOperation):
                flow_added = self.__judge_binary_operation(arg.operandl, flow_added, var_name)
                return flow_added


    def __if_variable_assignment(self, node, class_method, var_name, count, current_count):
        if isinstance(node.value, javalang.tree.MethodInvocation): # 2-2
            if node.value.arguments:
                for arg_index, arg in enumerate(node.value.arguments):
                    if isinstance(arg, javalang.tree.MemberReference) and arg.member == var_name and (count<current_count):      
                        #self.__flow.append([node.value.member,var_name])
                        self.__track_variable_flow(class_method,node.expressionl.member,current_count) # 같은 메서드에서 추적

        if isinstance(node.value, javalang.tree.MethodInvocation) and (node.value.qualifier == var_name) and (count<current_count):
            #self.__flow.append([node.value.member,var_name])
            self.__track_variable_flow(class_method,node.expressionl.member,current_count) # 같은 메서드에서 추적

        if isinstance(node.expressionl, javalang.tree.MemberReference) and node.value.member == var_name and (count<current_count) : # 1-1
            self.__track_variable_flow(class_method,node.expressionl.member,current_count)

        if isinstance(node.expressionl, javalang.tree.MemberReference) and node.expressionl.member == var_name and (count<current_count) : # 1-2
            #초기화 값이 Source 함수일 경우 추가 필요
            if count<current_count :
                return
    

    def __if_local_variable_declaration(self, node, class_method, var_name, count, current_count):
        for var_decl in node.declarators:
            if isinstance(var_decl.initializer, javalang.tree.MethodInvocation): # 2-2
                if var_decl.initializer.arguments:
                    for arg_index, arg in enumerate(var_decl.initializer.arguments):
                        if isinstance(arg, javalang.tree.MemberReference) and arg.member == var_name and (count<current_count):
                            #flow.append([class_method,var_name]) 이건 MethodInvocation 노드에서 추가할 듯
                            self.__track_variable_flow(class_method,var_decl.name,current_count) # 같은 메서드에서 추적

            if isinstance(var_decl.initializer, javalang.tree.MethodInvocation):
                if (var_decl.initializer.qualifier == var_name) and (count<current_count) : # 2-1
                    #self.__flow.append([var_decl.initializer.member,var_name])
                    self.__track_variable_flow(class_method,var_decl.name,current_count) # 같은 메서드에서 추적

            if isinstance(var_decl.initializer, javalang.tree.MemberReference) and var_decl.initializer.member == var_name and (count<current_count) :  # 1-1
                self.__track_variable_flow(class_method, var_decl.name,current_count)


    def __if_call_method(self, node, var_name, count, current_count):
       if node.arguments: 
            for arg_index, arg in enumerate(node.arguments):
                if isinstance(arg, javalang.tree.MemberReference):
                    if arg.member == var_name and (count<current_count) : # 4-1                                            
                        class_method_2, var_name_2 = self.__call2method(node,arg_index)
                        var_name_2 = var_name if var_name_2 == None else var_name_2 # 소스코드에 없는 메서드 호출시 var_name_2 가 None 이 되는경우 방지
                        self.__track_variable_flow(class_method_2,var_name_2)
                        
                elif isinstance(arg, javalang.tree.BinaryOperation):
                    self.__process_binary_operation(arg, node, var_name, count, current_count)


    def __process_binary_operation(self, binary_op, node, var_name, count, current_count):
        # 재귀적으로 BinaryOperation을 탐색하여 모든 오퍼랜드를 처리
        if isinstance(binary_op.operandl, javalang.tree.BinaryOperation):
            self.__process_binary_operation(binary_op.operandl, node, var_name, count, current_count)
        elif isinstance(binary_op.operandl, javalang.tree.MemberReference):
            if binary_op.operandl.member == var_name:
                self.__track_variable_flow(f"{type(node).__name__}.{node.member}", binary_op.operandl.member)

        if isinstance(binary_op.operandr, javalang.tree.BinaryOperation):
            self.__process_binary_operation(binary_op.operandr, node, var_name, count, current_count)
        elif isinstance(binary_op.operandr, javalang.tree.MemberReference):
            if binary_op.operandr.member == var_name:
                self.__track_variable_flow(f"{type(node).__name__}.{node.member}", binary_op.operandr.member)
    
    def __call2method(self, node, arg_index):
        invoked_method = node.member
        for target_class_method, target_method_nodes in self.__methods.items():
            target_class_name, target_method_name = target_class_method
            if target_method_name == invoked_method:  # 문제: 메서드 이름은 같은데 클래스가 다르다면?
                for target_file_path, target_method_node in target_method_nodes:
                    if len(target_method_node.parameters) > arg_index:
                        new_var_name = target_method_node.parameters[arg_index].name
                        return f"{target_class_name}.{invoked_method}", new_var_name
        return "UnknownClass." + invoked_method, None  # 만약 소스코드에 정의되지 않은 함수라면


    def __if_for_statement(self, node, class_method, var_name, count, current_count):
        if isinstance(node.control, javalang.tree.EnhancedForControl):
            EFC = node.control
            if EFC.iterable.member == var_name:
                for var_decl in EFC.var.declarators:
                    if isinstance(var_decl, javalang.tree.VariableDeclarator) and (count<current_count) :
                        var_name_2 = var_decl.name
                        self.__track_variable_flow(class_method, var_name_2,current_count) # for 문 끝날때 까지만 추적하도록 수정 필요
