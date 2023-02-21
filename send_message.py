import requests
import json
import os

webhook_url = os.environ['WEBHOOK_URL']

def send_message(message):
    headers = {'Content-Type': 'application/json'}
    data = {'msgtype': 'text', 'text': {'content': message}}
    r = requests.post(url=webhook_url, headers=headers, data=json.dumps(data))
    print(r.text)

if __name__ == '__main__':
    send_message('Hello from GitHub Actions!')
