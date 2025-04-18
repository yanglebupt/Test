import argparse
from tools import crew_template_code
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将生成的json转成文件夹')
    parser.add_argument('--json_filename', help='输入生成的json文件名')
    parser.add_argument('--project_name', default=None, help='crewai 项目名称')
    args = parser.parse_args()
    json_filename = args.json_filename

    res = json.load(open(f"generates/{json_filename}.json", encoding="utf8"))
    crew_template_code(res, args.project_name)
    