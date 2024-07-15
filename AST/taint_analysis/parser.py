import javalang
import os

def parse_java_files(folder_path):
    """ Parse all Java files in the given folder and return a list of parsed ASTs. """
    trees = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.java'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    source_code = file.read()
                tree = javalang.parse.parse(source_code)
                trees.append((file_path, tree))
    return trees
