import json
import os
import MethodPositionLocator

class analysisResultManager:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.data = self.load_json()

    def load_json(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, 'r') as f:
                return json.load(f)
        else:
            print(f"{self.json_file_path} 파일이 존재하지 않아 새로 생성합니다!")
            with open(self.json_file_path, 'w') as f:
                json.dump([], f, indent=4)  # 빈 리스트로 초기화
        return []

    def save_json(self):
        with open(self.json_file_path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def append(self, sensitivity, file_path, method_name, tree_position, cut_tree, source_code):
        flow_data = {
            "sensitivity": sensitivity,
            "file_path": file_path,
            "method_name": method_name,
            "tree_position": tree_position,
            "cut_tree": cut_tree,
            "source_code": source_code
        }
        self.data.append(flow_data)  # 데이터를 리스트에 추가
        self.save_json()  # 파일에 저장
