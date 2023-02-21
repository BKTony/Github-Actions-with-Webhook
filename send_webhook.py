import requests
import os

url = os.environ['WEBHOOK_URL']  # 从命令行参数中获取 Webhook URL

# payload = {"text": "今日已收盘!"}

# response = requests.post(url, json=payload)

# if response.status_code == 200:
#   print("Webhook sent successfully!")
# else:
#   print("Failed to send webhook.")

def send_message():
    message = '今日已收盘!'
    data = {
        'text': message
    }
    response = requests.post(url, json=data)
    if response.ok:
        print('Message sent!')
    else:
        print('Message failed!')
