import requests
import yaml

# Get token from Baidu


def get_token(modle_for_check):
    result = read_auth_data_from_yaml()
    AK = result[modle_for_check]['AK']
    SK = result[modle_for_check]['SK']
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
        AK+'&client_secret='+SK
    response = requests.get(host)
    if response:
        token = response.json()['access_token']
        return token
    else:
        print("No response for access token, please verify AK/SK")

# Read AK/SK from yaml


def read_auth_data_from_yaml():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    if result:
        return result
    else:
        return wirte_auth_data_to_yaml()

# Write AK/SK to yaml when there is no AK/SK provided


def wirte_auth_data_to_yaml():
    print("You do't put any Auth information. Please input:")
    AK = input("input AK:")
    SK = input("input SK:")
    names_yaml = {
        'Auth': {"AK": AK, "SK": SK}
    }
    with open("./config.yaml", "w", encoding="utf-8") as f:
        yaml.dump(names_yaml, f)
    return names_yaml
