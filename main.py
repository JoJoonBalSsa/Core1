from taintAnalysis import taintAnalysis


def create_result(flows):
    with open("result.txt", 'w', encoding='utf-8') as file:  # 결과 파일 생성
        for (class_method, var), value in flows.items():
            file.write("Tainted Variable:\n")
            file.write(f"{class_method}, {var}\n")
            file.write("흐름 파악\n")
            for f in value:
                file.write(f"{f}\n")
            file.write("\n")
    

def print_result(flows):
    for (class_method, var), value in flows.items():
        print("Tainted Variable: ")
        print(f"{class_method}, {var}")
        print("흐름 파악")
        for f in flows[class_method, var]:
            print(f)
        print()
    

def main(java_folder_path, output_folder):
    tainted = taintAnalysis(java_folder_path)
    print_result(tainted.flows)
    create_result(tainted.flows)


if __name__ == "__main__":
    # Specify the folder containing Java files
    java_folder_path = '/home/namaek_2/java-christmas-6-scienceNH'
    # java_folder_path = 'C:/Users/조준형/Desktop/S개발자_프로젝트/Core1/AST/christmas'  
    main(java_folder_path, java_folder_path)
