from parser import parse_java_files
from extractor import extract_methods_and_find_tainted_variables
from flow_tracker import track_variable_flow, flow
from utils import numbering 
from collections import defaultdict


def main():
    java_folder_path = 'C:/Users/조준형/Desktop/S개발자_프로젝트/Core1/AST/christmas'  # Specify the folder containing Java files

    # Step 1: Parse all Java files
    trees = parse_java_files(java_folder_path)

    # Step 2: Extract methods and find tainted variables
    tainted_variables = extract_methods_and_find_tainted_variables(trees)
    flows = defaultdict(list)
    
    for class_method, var, count in tainted_variables:
        flow.clear()
        track_variable_flow(class_method, var, count)
        
        # 새로운 키를 생성하고, 기존 키가 존재하면 새 키를 사용
        existing_key = (class_method, var)
        new_key = numbering(flows, existing_key)

        # 만약 이미 해당 키가 있다면 기존 값에 flow를 추가
        flows[new_key].extend(flow)

        
    for (class_method, var), value in flows.items():
        print("Tainted Variable: ")
        print(f"{class_method}, {var}")
        print("흐름 파악")
        for f in flows[class_method, var]:
            print(f)

        print()

    with open("result.txt", 'w', encoding='utf-8') as file:  # 결과 파일 생성
        for (class_method, var), value in flows.items():
            file.write("Tainted Variable:\n")
            file.write(f"{class_method}, {var}\n")
            file.write("흐름 파악\n")
            for f in value:
                file.write(f"{f}\n")
            file.write("\n")

if __name__ == "__main__":
    main()
