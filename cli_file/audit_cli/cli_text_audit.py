'''
    Commands examples: 
    python3 main.py -t (Scan all files in assets/text/*)
    python3 main.py -t -p assets/text/a.txt (Scan file of assets/text/a.txt)
'''
import json
import os
import requests
from com_function.get_local_storage import get_token


class Type():
    text = "text"


# API of Text Audit
url_list = {
    Type.text: 'https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined?access_token='
}

# Check text audit


def cli_text_audit(args):
    if args.path:
        path = args.path
        output_result_tojson(path, Type.text)

    else:
        for file_path in os.listdir('assets/text'):
            path = 'assets/text/' + file_path
            output_result_tojson(path, Type.text)


# Output json result to json file
def output_result_tojson(path, type: Type):
    token = get_token('Auth')
    url = url_list[type] + token
    file_handler = open(path, 'r')
    list_of_lines = file_handler.readlines()
    resultDict = {}
    for index, line in enumerate(list_of_lines):
        meta_data = line.strip()
        para = {"text": meta_data}
        r = requests.post(url, data=para)
        resultDict[meta_data] = r.json()
        print('all %s, current' % len(list_of_lines), index+1)
    with open('output/%s-result.json' % path[-5], "w", encoding='utf-8') as outfile:
        outfile.write(json.dumps(resultDict, ensure_ascii=False, indent=4))

    print('Done. Please check jason file!')
