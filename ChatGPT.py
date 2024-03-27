import configparser
import requests


import configparser

class HKBU_ChatGPT:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.telegram_token = config.get('TELEGRAM', 'ACCESS_TOKEN')
        self.basic_url = config.get('CHATGPT', 'BASICURL')
        self.model_name = config.get('CHATGPT', 'MODELNAME')
        self.api_version = config.get('CHATGPT', 'APIVERSION')
        self.access_token = config.get('CHATGPT', 'ACCESS_TOKEN')
        self.telegram_token = config.get('TELEGRAM', 'ACCESS_TOKEN')

        # rest of your code

    def submit(self, message):
        conversation = [{"role": "user", "content": message}]
        url = self.basic_url + "/deployments/" + self.model_name + "/chat/completions/?api-version=" + self.api_version
        headers = {'Content-Type': 'application/json', 'api-key': self.access_token}
        payload = {'messages': conversation}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response


if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)