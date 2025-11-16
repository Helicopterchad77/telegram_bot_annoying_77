import random
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

token: Final = "8585416166:AAHXMYXciEarfgpSKj8dsaKRsv4SCoCx6oM"
BOT_USERNAME = Final = "@Annoyingly_annoying_bot"

riddles = ["I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
           "The more you take, the more you leave behind. What am I?",
           ]
async def start_command(udate: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, i am an annoying bot!(reply with a 'hello')")

async def help_command(udate: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I caN HELP you by passing time chatting with me!(reply with a 'hello')")


async def custom_command(udate: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I have no custom command yet, but i will have one soon after more testng! :)")


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if "hello" in processed:
        return "Hi, how are you? Please ask me 'how are you' back so i can respond! "
    
    if "how are you" in processed:
        return "I am doing fine!"
    
    if "i am fine" in processed:
        return "That is good!"
    
    if "i am mama" in  processed:
        return "I send love from Jonah through Annoyingbot"
    
    if "why are you called annoyingbot?" in processed:
        return "because i am annoying :)"
    if "start game" in processed:
        return "lets start the game! guess 5-letter words until you guess the one i am thinking of!"
    if "apple" in processed:
        return "you are correct! you win!"
    if "what is your favourite food" in processed:
        return "people that are easily upset"
    if "what is your favourite drink" in processed:
        return "the tears of annoyed people"
    
    if "riddle time" in processed:
        
        [0]
    
    
    
    else:
        return "I cannot understand you unless you write something i can respond to using my in-built responses!"
    
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"user ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")



if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

app.add_handler(MessageHandler(filters.TEXT, handle_message))



app.add_error_handler(error)

print("Polling...")
app.run_polling(poll_interval = 3)

