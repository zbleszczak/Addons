import os

import telebot

# Create a TeleBot object with your bot token
bot = telebot.TeleBot(token='6004981495:AAEod7VNLoWTjmU-2vg-vX-iQfi7so5GZf8')
group_id = 'Moon_Log'

download_dir = os.path.join(os.path.expanduser('~'), 'downloads')

# Download the file to the specified directory
with open(os.path.join(download_dir, file_name), 'wb') as f:
    f.write(downloaded_file)
# Get the latest file sent in the group chat
@bot.message_handler(content_types=['document'], func=lambda message: message.chat.id == group_id)
def handle_document(message):
    file_id = message.document.file_id
    file_name = message.document.file_name
    bot.send_document(chat_id=message.chat.id, data=file_id, caption='Downloading file...')

    # Download the file to your local machine
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as f:
        f.write(downloaded_file)
    bot.send_message(chat_id=message.chat.id, text='File downloaded successfully.')

# Start the bot
bot.polling()