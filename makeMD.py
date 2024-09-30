import os
import matplotlib.pyplot as plt
import networkx as nx
import datetime
import math
import re

class MakeMD:
    def __init__(self, input_file='result.txt', output_file='analysis_result.md'):
        self.input_file = input_file
        self.output_file = output_file
        self.graph_dir = 'call_graphs'
        if not os.path.exists(self.graph_dir):
            os.makedirs(self.graph_dir)

    def parse_result_file(self):
        tainted_variables = []
        if not os.path.exists(self.input_file):
            print(f"Error: Input file '{self.input_file}' not found.")
            return tainted_variables
        
        with open(self.input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("Tainted Variable:"):
                variable_name = lines[i + 1].strip()
                flow = []
                i += 3  # 'Tainted Variable:' 줄과 변수 이름 줄을 건너뜁니다
                while i < len(lines) and lines[i].strip().startswith('['):
                    try:
                        clean_line = self.clean_flow(lines[i].strip())
                        for flow_node in clean_line:
                            print(flow_node)
                            flow.append(flow_node)
                    except ValueError:
                        print(f"Warning: Unable to parse line: {lines[i].strip()}")
                    i += 1
                tainted_variables.append({"variable": variable_name, "flow": flow})
                continue
            i += 1
        
        return tainted_variables

    def clean_flow(self, flow_string):
        # 대괄호 제거
        cleaned_string = flow_string.strip()[1:-1]

        # 정규 표현식을 사용하여 원하는 항목 추출
        items = re.findall(r"'([^']+)'", cleaned_string)

        # 각 항목에서 쉼표 제거 및 앞뒤 공백 제거
        cleaned_items = [item.replace(',', '').strip() for item in items]

        # 클래스명만 추출
        class_only_items = [item.split('.')[0] for item in cleaned_items]

        return class_only_items
    
    def create_call_graph_image(self, flow, variable_name):
        if len(flow) < 2:
            print(f"Warning: Not enough nodes to create a graph for variable '{variable_name}'.")
            return None

        G = nx.DiGraph()
        for i in range(len(flow) - 1):
            G.add_edge(flow[i], flow[i+1])

        node_count = len(G.nodes())

        # 이미지 크기 조정
        base_size = 12  
        size_factor = math.sqrt(node_count) * 0.5 + 1
        fig_size = (base_size * size_factor, base_size * size_factor / 2)

        # 노드 크기 조정
        max_node_size = 7000
        min_node_size = 3000
        node_size = max(min_node_size, max_node_size - (node_count * 200))

        # 폰트 크기 조정
        max_font_size = 10
        min_font_size = 6
        font_size = max(min_font_size, max_font_size - (node_count * 0.2))

        # 그래프 레이아웃 설정
        pos = nx.spring_layout(G, k=0.5, iterations=100)

        # 노드 위치 조정 (y 좌표만 사용)
        y_coords = [coord[1] for coord in pos.values()]
        y_min, y_max = min(y_coords), max(y_coords)

        if y_max - y_min == 0:
            y_max = y_min + 1

        for node, (x, y) in pos.items():
            pos[node] = (x, (y - y_min) / (y_max - y_min))

        # 그래프 크기 설정
        plt.figure(figsize=fig_size)

        # 엣지 그리기 (화살표가 노드 위로 오도록)
        nx.draw_networkx_edges(
            G, pos, edge_color='black', arrows=True, arrowsize=20, width=2,
            connectionstyle='arc3,rad=0.1'
        )

        # 노드 그리기 
        nx.draw_networkx_nodes(
            G, pos, node_color='lightblue', edgecolors='black', node_size=node_size,
            alpha=0.6, linewidths=1
        )

        # 시작 노드 (테두리 파란색)
        nx.draw_networkx_nodes(
            G, pos, nodelist=[flow[0]], node_color='lightblue', edgecolors='blue',
            node_size=node_size, alpha=0.6, linewidths=3
        )

        # 끝 노드 (테두리 빨간색)
        nx.draw_networkx_nodes(
            G, pos, nodelist=[flow[-1]], node_color='lightblue', edgecolors='red',
            node_size=node_size, alpha=0.6, linewidths=3
        )

        # 레이블 그리기 (노드 위에 오도록)
        label_pos = {k: (v[0], v[1] + 0.02) for k, v in pos.items()}
        nx.draw_networkx_labels(
            G, label_pos, font_size=font_size, font_weight='bold'
        )

        # 그래프 여백 조정
        plt.margins(0.2)

        # 축 제거
        plt.axis('off')

        # 타이틀 설정
        plt.title(f"Call Graph for {variable_name}", fontsize=16)

        # 이미지 저장
        plt.tight_layout()
        image_filename = f'{variable_name}_call_graph.png'  # 변수명으로 파일 이름 설정
        image_path = os.path.abspath(os.path.join(self.graph_dir, image_filename))

        os.makedirs(os.path.dirname(image_path), exist_ok=True)

        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()

        relative_path = "./call_graphs/" + image_filename
        return relative_path




    def make_md_file(self):
        tainted_variables = self.parse_result_file()
        if not tainted_variables:
            print("Error: No tainted variables found. The markdown file will not be created.")
            return

        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            # Write file header
            md_file.write(f"# 결과 보고서\n")
            md_file.write(f"**생성일:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            md_file.write(f"**생성 도구:** Taint Bomb\n\n")
            
            # Write table of contents
            md_file.write("## 목차\n")
            md_file.write("- [개요](#개요)\n")
            md_file.write("- [콜 그래프](#콜-그래프)\n")
            md_file.write("- [상세 분석](#상세-분석)\n\n")
            
            # Write overview
            md_file.write("## 개요\n")
            md_file.write("이 보고서는 코드베이스에 대한 분석 결과를 제공하며, 잠재적인 보안 위험과 취약점을 식별합니다.\n")
            md_file.write("다음 섹션에는 코드 내에서 오염된 데이터의 흐름을 시각화한 콜 그래프와, 각 오염된 변수에 대한 자세한 정보가 포함되어 있습니다.\n\n")
            
            # Write call graph section
            md_file.write("## 콜 그래프\n")
            md_file.write("아래는 애플리케이션에서 오염된 데이터의 흐름을 나타내는 콜 그래프입니다. 각 그래프 뒤에는 관련된 오염된 변수에 대한 상세 분석이 이어집니다.\n\n")
            
            for var_info in tainted_variables:
                image_path = self.create_call_graph_image(var_info['flow'], var_info['variable'])
                print(f"Graph saved to: {image_path}")
                print(f"var_info : {var_info}")
                if image_path:
                    md_file.write(f"### 콜 그래프: `{var_info['variable']}`\n")
                    md_file.write(f"![콜 그래프]({image_path})\n\n")
                    
                    # Write flow description
                    md_file.write(f"**오염된 데이터의 흐름:**\n")
                    md_file.write("```text\n")
                    md_file.write(" -> ".join(var_info['flow']))
                    md_file.write("\n```\n\n")
            
            # Write detailed analysis section
            md_file.write("## 상세 분석\n")
            md_file.write("다음 섹션에서는 각 오염된 변수에 대한 자세한 정보와 잠재적인 영향, 권장 완화 방법을 제공합니다.\n\n")
        
        print(f"Markdown 보고서가 생성되었습니다: {self.output_file}")


# Example execution
if __name__ == "__main__":
    maker = MakeMD(input_file='result.txt')
    maker.make_md_file()
