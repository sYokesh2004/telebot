from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Dictionary to store movie information
movie_database = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Movie Bot! Send /addmovie [name] [details] to add a movie.')

def add_movie(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 2:
        update.message.reply_text('Please provide both movie name and details.')
        return

    name = args[0]
    details = ' '.join(args[1:])
    
    # Add the movie to the database
    movie_database[name] = details

    update.message.reply_text(f'Movie "{name}" added successfully.')

def get_movie(update: Update, context: CallbackContext) -> None:
    args = context.args
    if not args:
        update.message.reply_text('Please provide the name of the movie.')
        return

    name = ' '.join(args)

    # Check if the movie is in the database
    if name in movie_database:
        details = movie_database[name]
        update.message.reply_text(f'Movie: {name}\nDetails: {details}')
    else:
        update.message.reply_text('Movie not found in the database.')

def main() -> None:
    updater = Updater('YOUR_TELEGRAM_BOT_TOKEN')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("addmovie", add_movie))
    dp.add_handler(CommandHandler("getmovie", get_movie))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
