import telegram
import time

# ใส่ TOKEN และ CHANNEL ID ตรงนี้
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "@YOUR_CHANNEL_ID"

bot = telegram.Bot(token=BOT_TOKEN)

def send_message(text):
    bot.send_message(chat_id=CHANNEL_ID, text=text)

if __name__ == "__main__":
    while True:
        # ตัวอย่างส่งข้อความทุก 10 วินาที (พี่เอาไปปรับได้ทีหลัง)
        send_message("ข่าวใหม่จาก ENKO!")
        time.sleep(10)
