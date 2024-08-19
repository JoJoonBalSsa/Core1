import json
import os

class analysisResultManager:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.data = self.load_json()

    def load_json(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, 'r') as f:
                return json.load(f)
        else:
            print(f"{self.json_path} 파일이 존재하지 않아 새로 생성합니다!")
            with open(self.json_path, 'w') as f:
                json.dump({}, f, indent=4)
        return {}

    def save_json(self):
        with open(self.json_file_path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def update_method_info(self, file_path, method_name, tree_position, cut_tree, sensitivity, source_code):
        if file_path not in self.data:
            self.data[file_path] = {}
        
        if method_name not in self.data[file_path] or self.data[file_path][method_name]['sensitivity'] < sensitivity:
            self.data[file_path][method_name] = {
                "tree_position": tree_position,
                "cut_tree": cut_tree,
                "sensitivity": sensitivity,
                "source_code": source_code
            }
            return True
        return False

    def method_exists(self, file_path, method_name):
        return file_path in self.data and method_name in self.data[file_path]