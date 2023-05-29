#!/bin/env python
#-*-coding:UTF-8-*-
#
# Made by LoboGuardian
# Follow me on https://github.com/LoboGuardian

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from config.auth import TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Started"
    )
    
if __name__ == '__main__':
  application = ApplicationBuilder().token(TOKEN).build()

#Handler
  start_handler = CommandHandler('start', start)

#Action
  application.add_handler(start_handler)

  application.run_polling()
