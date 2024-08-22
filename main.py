from taintAnalysis import taintAnalysis
from analysisResultManager import analysisResultManager



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
    json_file_path = "./analysis_result.json" 
    result = analysisResultManager(json_file_path)
    tainted = taintAnalysis(java_folder_path)

    for flow in flows:
        sensitivity = flow[0]  # 민감도 값

        for count in range(1, len(flow)):
            method_full_path = flow[count]
            parts = method_full_path.split('.')
            method_name = parts[1]

            cut_tree = tainted._get_cut_tree(method_name)
            current_path = tainted._file_path
            tree_position = tainted._get_position
            source_code = tainted._extract_method_source_code()

            result.append(sensitivity, current_path, method_name, tree_position, cut_tree, source_code)

    result.save_to_json()  # 결과를 JSON 파일로 저장
    


if __name__ == "__main__":
    # Specify the folder containing Java files
    java_folder_path = 'christmas'
    main(java_folder_path, java_folder_path)