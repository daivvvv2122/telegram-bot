import telebot
import os
from flask import Flask, request

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك في بوت DavidTalentGate 🎯")

@server.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def index():
    return "البوت يعمل ✅"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{os.environ.get('WEBHOOK_URL')}/{TOKEN}")
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
