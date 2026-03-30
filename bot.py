from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7549112095:AAF8jPURDtwBjGkW3qijgAEEFIbnQoSj-wE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["/tambahakun", "/settoko", "/isikeranjang"],
        ["/checkout", "/tutorial"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("Pilih menu:", reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()