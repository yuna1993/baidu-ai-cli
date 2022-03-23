
'''
    Commands examples: 
    python3 main.py -i (Scan all files in assets/image/*)
    python3 main.py -t -p assets/image/a.png (Scan file of assets/image/a.png)
'''
import json
import os
import requests
import base64
from com_function.get_local_storage import get_token


class Type():
    image = "image"


# API of image Audit
url_list = {
    Type.image: 'https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined?access_token='
}


def cli_image_audit(args):
    if args.path:
        path = args.path
        output_result_tojson(path, Type.image)

    else:
        for file_path in os.listdir('assets/image'):
            path = 'assets/image/' + file_path
            output_result_tojson(path, Type.image)

# Output json result to json file


def output_result_tojson(path, type: Type):
    token = get_token('Auth')
    url = url_list[type] + token
    file_handler = open(path, 'rb')
    img = base64.b64encode(file_handler.read())
    payload = dict(image=img)
    r = requests.post(url, data=payload)

    resultDict = {}
    resultDict[0] = r.json()
    with open('output/%s-result.json' % path[13:], "w", encoding='utf-8') as outfile:
        outfile.write(json.dumps(resultDict, ensure_ascii=False, indent=4))

    print('Done. Please check jason file!')
