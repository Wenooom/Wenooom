import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# اطلاعات ای پی آی تلگرام خود را اینجا وارد کنید (یا از متغیرهای محیطی بخوانید)
API_ID = 33092137  # api_id خود را اینجا بگذارید
API_HASH = "26652482c63447b25771ec724eebe67e"  # api_hash خود را اینجا بگذارید

# لیست سشن‌های StringSession برای یوزربات‌های مختلف
SESSION_STRINGS = [
    "1BJWap1wBu3hfCyKb4Y6OtJRD9sN5_GP_Y9u0oxIANdwNnjVrqcXWCIl3cXyhGESq1W_b_A_UbX2ZLOdDX97e_dcUZD6S0S60RY2nElMqbT49C3CT-Fv_6mI72nYYnP4PVlR0b4ccYNmOuJrqI5VX8ZREZwzcv6-GLdzdplOnh0zOKVf7vsGlvA5rjz8rdRBlkDOd3GBqz6woGs9fafugMBe4jwdrWmEjQwsZeCv9XTRBsy38FYst2hN1--mw3-stLvFozocKY0zi1OMQa7z8x5Tt6tyYfCLZ5D9q7d8RmYLngJRzBwRLn_zb-RCYPQ666-T6pyx_Iq_1WvBCNECAzseV-5SBBKg="] 

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
