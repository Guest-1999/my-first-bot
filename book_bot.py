from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "8119054853:AAGes2jnytVrIeXMi_Vg-gIhyCE3FT1CLqE"

# File to send
FILE_PATH = "D:/front-end/bot/Roadmap for BOT.pdf"

async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("📂 Get File", callback_data="send_file")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below to get the file:", reply_markup=reply_markup)

async def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "send_file":
        await query.message.reply_document(document=open(FILE_PATH, "rb"), caption="Here is your file!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
