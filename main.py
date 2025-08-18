import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# حط التوكن الخاص بالبوت هنا
TOKEN = os.getenv("8214897188:AAGuM4xCfGiKeQm_9vzT9r0SDXrFMLMUJxI")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا 👋 البوت شغال!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if name == "main":
    main()
