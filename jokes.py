from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
import requests, random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

updater = Updater(token="768254014:AAFXh3nYCXKR9dP1_0EbxHXURifb-oYeXQ4")

dispatcher = updater.dispatcher

def choices(bot, update):
	options = [
		[InlineKeyboardButton("Reddit Jokes", callback_data = "redditjokes"),
		 InlineKeyboardButton("Stupid Stuff", callback_data = "stupidstuff"),
		 InlineKeyboardButton("Wocka", callback_data = "wocka")
		]

	]

	reply = InlineKeyboardMarkup(options)
	bot.send_message(chat_id = update.message.chat_id,
					text = "Choose A Type Of Joke:",
					reply_markup = reply)

dispatcher.add_handler(CommandHandler("jokes", choices))

def jokes(bot, update):
	data = update.callback_query.data
	joke = ""

	if (data == "redditjokes"):
		req = requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/reddit_jokes.json")
		rand = random.randint(0,195000)
		joke = req.json()[rand]["title"] +"\n"+req.json()[rand]["body"]
	elif (data == "stupidstuff"):
		req = requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json")
		rand = random.randint(0,3770)
		joke = req.json()[rand]["title"] +"\n"+req.json()[rand]["body"]
	elif (data == "wocka"):
		req = requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/wocka.json")
		rand = random.randint(0,10000)
		joke = req.json()[rand]["title"] +"\n"+req.json()[rand]["body"]


	bot.edit_message_text(chat_id = update.callback_query.message.chat_id,
		text = joke,
		message_id = update.callback_query.message.message_id)

dispatcher.add_handler(CallbackQueryHandler(jokes))


updater.start_polling()
updater.idle()
