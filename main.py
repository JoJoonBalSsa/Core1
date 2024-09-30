from taintAnalysis import taintAnalysis
from analysisResultManager import analysisResultManager



def create_result(flows):
    with open("result.txt", 'w', encoding='utf-8') as file:  # 결과 파일 생성
        for (class_method, var), value in flows.items():
            file.write("Tainted Variable:\n")
            file.write(f"{var}\n")
            file.write("흐름 파악\n")
            for f in value:
                    if isinstance(f[0], list):
                        for sub_f in f:
                            file.write(f"{sub_f}\n")
                    else:
                        file.write(f"{f}\n")
            file.write("\n")
    


def main(java_folder_path, output_folder):
    tainted = taintAnalysis(java_folder_path)
    f_flow=tainted._priority_flow()

    create_result(tainted.flows)
    __analyze_method(f_flow, tainted)


def __analyze_method(flows, tainted):
    json_file_path = "./analysis_result.json" 
    result = analysisResultManager(json_file_path)

    for flow in flows:
        sensitivity = flow[0]  # 민감도 값

        for count in range(1, len(flow)):
            method_full_path = flow[count]
            big_parts = method_full_path.split(',') 
            if len(big_parts) == 1:
                big_parts.append("")
            parts = big_parts[0].split('.')
            little_method_name = parts[1]

            cut_tree = tainted._get_cut_tree(little_method_name)
            current_path = tainted._file_path
            tree_position = tainted._get_position
            source_code = tainted._extract_method_source_code()
            method_name = method_full_path

            result.append(sensitivity, current_path, method_name, tree_position, cut_tree, source_code)

    result.save_to_json()  # 결과를 JSON 파일로 저장
    


if __name__ == "__main__":
    # Specify the folder containing Java files
    java_folder_path = '박하은_크리스마스'
    main(java_folder_path, java_folder_path)