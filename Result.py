class Result:
    def __init__(self, flows):
        self.print_result(flows)
        self.create_result(flows)

    
    def print_result(self, flows):
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


    def create_result(self, flows):
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