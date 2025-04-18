import json
import os
import argparse

def create_files_from_json_config(
        file_dict: dict = None, 
        json_path: str = None, 
        encoding: str = 'utf-8', 
        path_prefix = "src", 
        project_name = None) -> None:

    if file_dict is None:
        if json_path is not None:
            # 读取 JSON 文件
            with open(json_path, 'r', encoding=encoding) as f:
                file_dict = json.load(f)
        else:
            raise ValueError("file_dict 和 json_path 必须要传入一个")

    path_prefix = os.path.join(path_prefix, file_dict["crew_name"] if project_name is None else project_name)
    file_dict = file_dict["generate_codes"]
    
    if not isinstance(file_dict, dict):
        raise ValueError("JSON 内容必须是一个字典，格式为 {文件路径: 文件内容}")

    # 遍历字典创建文件
    for file_path, content in file_dict.items():
        file_path = os.path.join(path_prefix, file_path)
        try:
            # 创建目录（如果不存在）
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # 确定写入模式
            mode = 'w'
            if isinstance(content, bytes):
                mode = 'wb'
                encoding_param = None
            else:
                encoding_param = encoding
            
            # 写入文件
            with open(file_path, mode, encoding=encoding_param) as f:
                if isinstance(content, (dict, list)):
                    json.dump(content, f, ensure_ascii=False, indent=4)
                else:
                    f.write(str(content))
            
            print(f"✅ 成功创建文件: {file_path}")
        
        except Exception as e:
            raise ValueError(f"❌ 创建文件 {file_path} 失败: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将生成的json转成文件夹')
    parser.add_argument('--json_filename', help='输入生成的json文件名')
    parser.add_argument('--project_name', default=None, help='crewai 项目名称')
    args = parser.parse_args()
    json_filename = args.json_filename
    
    create_files_from_json_config(json_path=f"generates/{json_filename}.json", project_name=args.project_name)