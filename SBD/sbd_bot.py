import logging
import db_manager
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = "7106761380:AAFmrke2bGjFnK9jiMeCtcrmJcMew3xbCv0"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def selectAll(update:Update, context:ContextTypes.DEFAULT_TYPE):
     resultat = db_manager.select_all()
     await context.bot.send_message(chat_id=update.effective_chat.id, text=resultat)

async def suma(update: Update, context: ContextTypes.DEFAULT_TYPE):
        comanda = update.message.text
        valor1, valor2 = int(comanda.split(" ")[1]), int(comanda.split(" ")[2])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(valor1 + valor2))

async def text_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "hola":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="adeu")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="no t'entenc")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    suma_handler = CommandHandler('suma', suma)
    select_handler = CommandHandler('selectAll', selectAll)
    messageHandler = MessageHandler(filters.BaseFilter(), callback=text_message)
    application.add_handler(start_handler)
    application.add_handler(suma_handler)
    application.add_handler(select_handler)
    application.add_handler(messageHandler)
    application.run_polling()