from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# توکن ربات به صورت مستقیم در کد
TOKEN = "7614387323:AAFZZONix73KwdznxcU0DOnout6pWfz_hKw"  # توکن ربات خود را اینجا وارد کنید

# پیام تریگر برای حذف کلیه پیام‌ها
DELETE_TRIGGER = "اه"

# تابع برای حذف تمامی پیام‌ها
async def delete_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    message_id = update.message.message_id
    deleted_count = 0

    # حذف پیام حاوی "حذف همه" (پیام جاری)
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        deleted_count += 1
    except Exception as e:
        print(f"خطا در حذف پیام 'حذف همه': {e}")

    # پیمایش و حذف پیام‌های قبلی
    while True:
        try:
            # تلاش برای حذف پیام قبلی
            message_id -= 1
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            deleted_count += 1
        except Exception as e:
            # اگر پیام قدیمی باشد یا قابل حذف نباشد، حلقه متوقف می‌شود
            print(f"پیام با id={message_id} قابل حذف نیست یا وجود ندارد: {e}")
            break

    # ارسال گزارش نتیجه حذف پیام‌ها
    if deleted_count > 0:
        print(f"{deleted_count} پیام حذف شدند.")
    else:
        print("هیچ پیامی قابل حذف نبود.")

# تابع اصلی اجرا
def main() -> None:
    # ایجاد اپلیکیشن ربات
    app = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلر برای پیام "حذف همه"
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(f'^{DELETE_TRIGGER}$'), delete_all_messages))

    # اجرای ربات
    print("🤖 ربات در حال اجرا است...")
    app.run_polling()

if __name__ == '__main__':
    main()