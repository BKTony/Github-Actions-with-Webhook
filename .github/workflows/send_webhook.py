import requests
import sys

url = sys.argv[1]  # 从命令行参数中获取 Webhook URL

payload = {
    "text": "今天已收盘!"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Webhook sent successfully!")
else:
    print("Failed to send webhook.")
