import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import consts as cv
from mytoken import TOKEN
from myfilters import UserJoinedGroupFilter
from myhandlers import NewUserJoinHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
	logger.info('it runs...')

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
	logger.info("Loading handlers for telegram bot")
	updater = Updater(token=TOKEN)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))

	userJoinedGroupFilter = UserJoinedGroupFilter()
	dp.add_handler(MessageHandler((Filters.group & userJoinedGroupFilter), NewUserJoinHandler))

	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
