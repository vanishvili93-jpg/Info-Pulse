import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://www.skai.gr", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Ανοίξτε", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📊 Ανοίξτε την πλατφόρμα", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📊 Ανοίξτε την πλατφόρμα", url="https://www.skai.gr")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📊 *Καλώς ήρθατε.*\n\n"
        "Επενδυτικές αναλύσεις, ενημέρωση αγορών "
        "και διαχείριση χαρτοφυλακίου — κάθε μέρα "
        "στο Telegram.\n\n"
        "Τριάντα χρόνια στην ελληνική κεφαλαιαγορά. "
        "Μετοχές, παράγωγα, διαχείριση κεφαλαίων.\n\n"
        "Πατήστε *Θέματα ημέρας* για να ξεκινήσετε.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)
