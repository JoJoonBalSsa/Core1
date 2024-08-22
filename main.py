from taintAnalysis import taintAnalysis
from analysisResultManager import analysisResultManager
from MethodPositionLocator import MethodPositionLocator


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
    

def print_result(flows):
    for f in flows:
        print(f)
    print()



def main(java_folder_path, output_folder):
    tainted = taintAnalysis(java_folder_path)
    f_flow=tainted._priority_flow()

    print_result(f_flow)
    create_result(tainted.flows)
    __analyze_method(f_flow)


def __analyze_method(flows):
    json_file_path = "C:/Users/gkds0/OneDrive/바탕 화면/core1/Core1/analysis_result1.json" 
    result = analysisResultManager(json_file_path)  # JSON 파일 경로를 지정
    tainted = taintAnalysis(java_folder_path)


    for flow in flows:
        sensitivity = flow[0]  # 민감도 값

        method_full_path = flow[1]
        # method_name을 추출
        parts = method_full_path.split('.')
        if len(parts) == 2 or 3:
            method_name = parts[1]  # 두 번째 마지막 부분을 method_name으로 설정


        current_path = tainted._get_file_path(method_name)  # current_path는 실제 코드에 맞게 설정

        source_code = tainted._extract_method_source_code(method_name)
        
        # 트리 위치 계산
        tree_position = tainted._get_position
        
        cut_tree = tainted._get_cut_tree(method_name)

        # create_flow 함수가 반환하는 값을 flow_data 리스트에 추가
        result.append(sensitivity, current_path, method_name, tree_position, cut_tree, source_code)



if __name__ == "__main__":
    # Specify the folder containing Java files
    java_folder_path = 'christmas'
    main(java_folder_path, java_folder_path)
