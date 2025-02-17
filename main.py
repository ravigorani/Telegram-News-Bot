import telegram.ext
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler, ConversationHandler, CallbackContext
from telegram import Update
from WebScrap import Scrapper
import time
import asyncio

Token = <Token>

async def start(update : Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!, Thanks for chating with me")
    
async def news(update: Update, context: CallbackContext) -> None:
    # Ensure chat_id is correctly defined
    if update.message:
        chat_id = update.message.chat_id
    elif update.callback_query:
        chat_id = update.callback_query.message.chat_id
    else:
        print("⚠️ Unable to determine chat_id!")
        return
    
    """Send all news articles to the user"""
    print("Scrapping News...")
    context.bot.send_message(chat_id=chat_id, text="Wait for some moment...")
    chat_id = update.message.chat_id
    news_dict = await Scrapper()
    if not news_dict:
        await context.bot.send_message(chat_id=chat_id, text="No news available at the moment.")
        return

    for link, news in news_dict.items():
        message = f"📰 <b>{news}</b>\n🔗 <a href='{link}'>Read More</a>"
        await context.bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
        await asyncio.sleep(1)    # Avoid rate limits

    print("✅ All news sent!")
    
async def help(update : Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
"""How may I help you?
/start -> Start the bot
/news -> For Latest News
/help -> Help section """)
    
    
if __name__=='__main__':
    print("Starting Programe")
    app = ApplicationBuilder().token(Token).build()
    
    app.add_handler(CommandHandler('start',start))
    app.add_handler(CommandHandler('news',news))
    app.add_handler(CommandHandler('help',help))
    
    print("Polling")
    app.run_polling()
    
