from taintAnalysis import taintAnalysis
from analysisResultManager import analysisResultManager
from methodPositionLocator import methodPositionLocator


def create_result(flows):
    with open("result.txt", 'w', encoding='utf-8') as file:  # 결과 파일 생성
        for (class_method, var), value in flows.items():
            file.write("Tainted Variable:\n")
            file.write(f"{class_method}, {var}\n")
            file.write("흐름 파악\n")
            for f in value:
                    if isinstance(f[0], list):
                        for sub_f in f:
                            file.write(f"{sub_f}\n")
                    else:
                        file.write(f"{f}\n")
            file.write("\n")
    

def print_result(flows,source):
    for (class_method, var), value in flows.items():
        
        print("Tainted Variable: ")
        print(f"{class_method}, {var}")
        print("흐름 파악")
        for f in value:
                if isinstance(f[0], list):  # 이중 리스트인 경우
                    for sub_f in f:
                        print(sub_f)
                else:
                    print(f)
        print()



def main(java_folder_path, output_folder):
    result = analysisResultManager("/")
    tainted = taintAnalysis(java_folder_path, result)
    print_result(tainted.flows,tainted.source_check)
    create_result(tainted.flows)
   
def __analyze_method(self):
        result = analysisResultManager("/")
        tainted = taintAnalysis(java_folder_path, result)

        result.create_json()
        flows=tainted._priority_flow()

        for flow in flows:
            sensitivity = flow[0]  # 민감도 값
            # 함수 이름 추출 (flow[1]은 전체 메서드 경로이므로, 이를 '.'으로 split 후 함수 이름 가져오기)
            method_name = flow[1].split('.')[-1]
            current_path = "/"  # current_path는 실제 코드에 맞게 설정
            tree_position = methodPositionLocator.visit_FunctionDef(method_name)
            cut_tree = tainted._get_cut_tree(method_name)
            source_code = tainted._extract_method_source_code(method_name)

            # create_flow 함수가 반환하는 값을 flow_data 리스트에 추가
            flow_item = result.create_flow(current_path, method_name, tree_position, cut_tree, sensitivity, source_code)
            result.flow_data.append(flow_item)



if __name__ == "__main__":
    # Specify the folder containing Java files
    java_folder_path = 'christmas'
    main(java_folder_path, java_folder_path)
