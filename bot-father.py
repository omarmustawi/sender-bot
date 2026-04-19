from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import Conflict

TOKEN = "7664614115:AAE0PwReqgbfY5qhvx_vRB1lZiRMGLJZ7hE"
PHOTO_PATH = "1.jpg"  # ضع اسم الملف المحلي للصورة هنا

AD_MESSAGE = """
مسا الخير جميعاً، أنا زميلكم بالكلية.

لاحظت كتير طلاب عم يعانوا مع Kaggle وColab بسبب:
❌ انقطاع الجلسات
❌ ذاكرة محدودة
❌ مشاكل توافق الإصدارات

بحثت ولقيت حل عملي ومتاح:
🖥️ GPU RTX 4090 بـ 24GB VRAM على منصة Vast.ai

✅ أسرع بمرتين من Colab
✅ تدريب متواصل (حتى لو طفيت كمبيوترك)
✅ مناسب لـ FLAN-T5 ومشاريع التخرج

📊 مثال توضيحي:
تدريب نموذج محادثات بـ 24,000 سطر بياخد 2-3 ساعات فقط بينما بياخد أكتر من 10 ساعات على gpu collab  أو Kaggle المحدود.

💰 الأسعار (لطلاب الكلية):
- 15,000 ليرة سورية / ساعة
- أو باقة 5 ساعات بـ 60,000 ليرة

💳 الدفع: كاش أو عن طريق شام كاش

📩 للاستفسار والحجز: راسلني خاص حتى أشحن البطاقة واحجز gpu قوي

العدد محدود، عشان هيك إذا حابب تجرب، تواصل معي.

https://t.me/engineer_om
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo=PHOTO_PATH, caption=AD_MESSAGE)

def main():
    try:
        app = Application.builder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))

        app.run_polling()
    except Conflict as e:
        print(f"Conflict error: {e}. Ensure only one bot instance is running.")

if __name__ == "__main__":
    main()