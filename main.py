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

    for i,j,k in source:
        print(i,j,k)
        print()


def main(java_folder_path, output_folder):
    result = analysisResultManager(".")
    tainted = taintAnalysis(java_folder_path, result)
    print_result(tainted.flows,tainted.source_check)
    create_result(tainted.flows)
   


if __name__ == "__main__":
    # Specify the folder containing Java files
    java_folder_path = 'christmas'
    main(java_folder_path, java_folder_path)
