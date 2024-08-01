from taintAnalysis import taintAnalysis
from Result import Result
    

def main(java_folder_path, output_folder):
    tainted = taintAnalysis(java_folder_path)
    result = Result(tainted.flows)


if __name__ == "__main__":
    # Specify the folder containing Java files
    java_folder_path = './christmas/src/main/java/christmas'
    #java_folder_path = 'C:/Users/조준형/Desktop/S개발자_프로젝트/Core1/christmas'  
    main(java_folder_path, java_folder_path)