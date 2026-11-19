import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# ========================================================
# 🎛️ تنظیمات اصلی و اختصاصی
START_LINE = 10000
END_LINE = 20000

# تعداد دقیق پیامی که بعد از رسیدن به آن، همه چیز متوقف می‌شود
MAX_MESSAGES = 10000

API_ID = 33092137
API_HASH = "26652482c63447b25771ec724eebe67e"

# خواندن رشته سشن از فایل متنی مخصوص هر اکانت
SESSION_FILE = "Session.text"

TEXT_FILE_PATH = "numbers.text"
TARGET_CHAT = "Havij_robot"
# ========================================================


async def send_messages():
    try:
        with open(SESSION_FILE, "r", encoding="utf-8") as sf:
            session_string = sf.read().strip()
    except FileNotFoundError:
        print(f"❌ خطا: فایل سشن '{SESSION_FILE}' پیدا نشد!")
        return

    client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
    print("⏳ در حال اتصال به تلگرام روی Render...")
    await client.start()
    print("🔓 یوزربات با موفقیت متصل شد و آماده ارسال است!")

    sent_count = 0
    reached_limit = False

    try:
        if not os.path.exists(TEXT_FILE_PATH):
            print(f"❌ خطا: فایل متنی '{TEXT_FILE_PATH}' پیدا نشد!")
            await client.disconnect()
            return

        with open(TEXT_FILE_PATH, "r", encoding="utf-8") as f:
            print(
                f"🚀 شروع ارسال از خط {START_LINE} تا {END_LINE} "
                f"(سقف: {MAX_MESSAGES} پیام) به مقصد {TARGET_CHAT} (با وقفه دقیق ۳ ثانیه)..."
            )

            for line_number, line in enumerate(f, start=1):
                if sent_count >= MAX_MESSAGES:
                    reached_limit = True
                    print(f"🛑 به مقدار تعیین‌شده ({MAX_MESSAGES} پیام) رسیدیم. توقف کامل ارسال!")
                    break

                if line_number < START_LINE:
                    continue
                if line_number > END_LINE:
                    reached_limit = True
                    print(f"🛑 به خط پایانی ({END_LINE}) رسیدیم. توقف ارسال.")
                    break

                text = line.strip()
                if text:
                    try:
                        await client.send_message(TARGET_CHAT, text)
                        sent_count += 1
                        print(f"✅ [{sent_count}/{MAX_MESSAGES}] [خط {line_number}] ارسال شد: {text}")
                    except Exception as e:
                        print(f"❌ خطا در ارسال خط {line_number}: {e}")

                    if sent_count >= MAX_MESSAGES:
                        reached_limit = True
                        print(f"🛑 به مقدار تعیین‌شده ({MAX_MESSAGES} پیام) رسیدیم. توقف کامل ارسال!")
                        break

                    # وقفه دقیق ۳ ثانیه بین هر ارسال
                    await asyncio.sleep(3)

        print(f"🏁 کار تمام شد. مجموع پیام‌های ارسال‌شده: {sent_count}")
    except Exception as e:
        print(f"❌ خطای ناخواسته: {e}")
    finally:
        await client.disconnect()
        print("🔌 اتصال تلگرام قطع شد.")

    # اگر به سقف رسید یا کار تمام شد، برنامه را نگه می‌داریم تا Render ری‌استارت نکند و از اول نفرستد
    if reached_limit:
        print("💤 در حالت توقف کامل منتظر می‌مانم تا هیچ پیام اضافه‌ای ارسال نشود...")
        while True:
            await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(send_messages())
