import requests
import json
import os

webhook_url = os.environ['WEBHOOK_URL']
# url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=591a4378-8d1c-4944-83b9-60162b434f20"
# webhook_url = requests.get(url)
    
def send_message(message):
    headers = {'Content-Type': 'application/json'}
    data = {'msgtype': 'text', 'text': {'content': message}}
    r = requests.post(url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=591a4378-8d1c-4944-83b9-60162b434f20", headers=headers, data=json.dumps(data))
    print(r.text)

if __name__ == '__main__':
    send_message('Hello from GitHub Actions!')
