import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# اطلاعات ای پی آی تلگرام خود را اینجا وارد کنید (یا از متغیرهای محیطی بخوانید)
API_ID = 1234567  # api_id خود را اینجا بگذارید
API_HASH = "your_api_hash"  # api_hash خود را اینجا بگذارید

# لیست سشن‌های StringSession برای یوزربات‌های مختلف
SESSION_STRINGS = [
    "STRING_SESSION_1_HERE",
    "STRING_SESSION_2_HERE"
]

async def start_client(session_str, index):
    client = TelegramClient(StringSession(session_str), API_ID, API_HASH)
    await client.start()
    print(f"Userbot {index} is running successfully!")
    await client.run_until_disconnected()

async def main():
    if not SESSION_STRINGS or SESSION_STRINGS[0] == "STRING_SESSION_1_HERE":
        print("لطفاً سشن‌های خود را در کد وارد کنید!")
        return
    
    tasks = [start_client(sess, i+1) for i, sess in enumerate(SESSION_STRINGS)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
