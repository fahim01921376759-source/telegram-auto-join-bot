import os
import logging
from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ["9269786018:AAHpqcWl7PJUS1N3lA0dR8g4aUbj9Nvl8ww"]

async def approve_request(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    request = update.chat_join_request
    if request:
        try:
            await request.approve()
            logging.info("Join request approved")
        except Exception:
            logging.exception("Could not approve join request")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve_request))
    app.run_polling(allowed_updates=["chat_join_request"])

if __name__ == "__main__":
    main()
  
