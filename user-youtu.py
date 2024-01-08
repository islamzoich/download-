import requests
import random
from telebot import TeleBot
from user_agent import generate_user_agent
headers = {}
id = str(input("Enter the Telegram ID : "))
token = str(input("Enter the Telegram bot token : "))
def main():
    username = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for _ in range(4))
    url = "https://www.youtube.com/@{}".format(username)
    headers.update({"user-agent":str(generate_user_agent())})
    req = int(requests.get(url,headers=headers).status_code)
    if req == 404:
        print(f"{req} : {username}")
        TeleBot(token=token).send_message(chat_id=id,text=f"يوزر يوتيوب متاح : {username} ✅")
        return True
    else:
        print(f"{req} : {username}")
        return False

while True:
    main()
