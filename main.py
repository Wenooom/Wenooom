Numberssyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# ========================================================
# 🎛️ تنظیمات اصلی 
START_LINE = 1        # شروع ارسال از این خط (قابل تغییر)
END_LINE = 100        # پایان ارسال در این خط (قابل تغییر)

# اطلاعات ای پی آی شما
API_ID = 33092137
API_HASH = "26652482c63447b25771ec724eebe67e"

# رشته سشن شما
SESSION_STRING = "1BJWap1wBu3hfCyKb4Y6OtJRD9sN5_GP_Y9u0oxIANdwNnjVrqcXWCIl3cXyhGESq1W_b_A_UbX2ZLOdDX97e_dcUZD6S0S60RY2nElMqbT49C3CT-Fv_6mI72nYYnP4PVlR0b4ccYNmOuJrqI5VX8ZREZwzcv6-GLdzdplOnh0zOKVf7vsGlvA5rjz8rdRBlkDOd3GBqz6woGs9fafugMBe4jwdrWmEjQwsZeCv9XTRBsy38FYst2hN1--mw3-stLvFozocKY0zi1OMQa7z8x5Tt6tyYfCLZ5D9q7d8RmYLngJRzBwRLn_zb-RCYPQ666-T6pyx_Iq_1WvBCNECAzseV-5SBBKg="

# نام فایل متنی لیست اعداد که در گیت‌هاب آپلود کرده‌اید
TEXT_FILE_PATH = "Number.txt" 

# ربات یا مقصدی که باید پیام‌ها به آن فرستاده شوند (مثلاً "Havij_robot" یا "me")
TARGET_CHAT = "Havij_robot"
# ========================================================

async def send_messages():
    # اتصال به تلگرام با استفاده از StringSession
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    print("⏳ در حال اتصال به تلگرام روی Render...")
    await client.start()
    
    print("🔓 یوزربات با موفقیت متصل شد و آماده ارسال است!")
    
    # خواندن فایل متنی و ارسال
    try:
        if not os.path.exists(TEXT_FILE_PATH):
            print(f"❌ خطا: فایل متنی '{TEXT_FILE_PATH}' پیدا نشد! لطفاً مطمئن شوید آن را در گیت‌هاب آپلود کرده‌اید.")
            await client.disconnect()
            return

        with open(TEXT_FILE_PATH, "r", encoding="utf-8") as f:
            print(f"🚀 شروع ارسال از خط {START_LINE} تا {END_LINE} به مقصد {TARGET_CHAT}...")
            
            for line_number, line in enumerate(f, start=1):
                if line_number < START_LINE:
                    continue
                if line_number > END_LINE:
                    print(f"🛑 به خط {END_LINE} رسیدیم. توقف ارسال.")
                    break
                    
                text = line.strip()
                if text:
                    try:
                        await client.send_message(TARGET_CHAT, text)
                        print(f"✅ [خط {line_number}] ارسال شد: {text}")
                    except Exception as e:
                        print(f"❌ خطا در ارسال خط {line_number}: {e}")
                        
                    # فاصله زمانی ۲ ثانیه بین هر ارسال
                    await asyncio.sleep(2)
                    
        print("🏁 ارسال تمام خطوط با موفقیت تمام شد.")
        
    except Exception as e:
        print(f"❌ خطای ناخواسته در خواندن فایل: {e}")
        
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(send_messages())
