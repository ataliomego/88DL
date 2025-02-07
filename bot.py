import os
import logging
from dotenv import load_dotenv
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pytube import YouTube
import yt_dlp as youtube_dl
import requests

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Bot Token and API keys from .env
BOT_TOKEN = os.getenv('BOT_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

# Function to handle /start command
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    lang = update.message.text.split(' ', 1)[-1] if len(update.message.text.split()) > 1 else 'en'
    
    if lang == 'id':
        update.message.reply_text("Selamat datang! Kirimkan link YouTube untuk mengunduh video/audio. Pilih format: MP3 320kbps, MP4 480p, 720p, atau 1080p.")
    else:
        update.message.reply_text("Welcome! Send a YouTube link to download video/audio. Choose format: MP3 320kbps, MP4 480p, 720p, or 1080p.")

# Function to search YouTube for videos
def search_youtube(update: Update, context: CallbackContext):
    query = " ".join(context.args)
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YOUTUBE_API_KEY}"
    
    response = requests.get(search_url).json()
    if 'items' in response:
        videos = response['items']
        message = "Here are the search results:\n"
        for i, video in enumerate(videos[:5]):
            title = video['snippet']['title']
            video_id = video['id']['videoId']
            message += f"{i+1}. {title} - https://youtu.be/{video_id}\n"
        update.message.reply_text(message)
    else:
        update.message.reply_text("No results found.")

# Function to download audio/video
def download(update: Update, context: CallbackContext):
    url = context.args[0]
    format_choice = context.args[1] if len(context.args) > 1 else 'mp3'
    video_info = YouTube(url)

    try:
        if format_choice == 'mp3':
            audio_stream = video_info.streams.filter(only_audio=True).first()
            audio_stream.download(filename='video.mp3')
            with open('video.mp3', 'rb') as f:
                update.message.reply_audio(f, caption="Here's your audio.")
        else:
            video_stream = video_info.streams.get_highest_resolution()
            video_stream.download(filename='video.mp4')
            with open('video.mp4', 'rb') as f:
                update.message.reply_video(f, caption="Here's your video.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Function to request like on Facebook page
def request_like(update: Update, context: CallbackContext):
    with open("support.txt", "r") as file:
        fb_link = file.read().strip()
    update.message.reply_text(f"Please support us by liking our Facebook page: {fb_link}\nThank you for using the bot!")

# Error handling function
def error(update: Update, context: CallbackContext):
    logger.warning(f"Update {update} caused error {context.error}")

# Main function to start the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search_youtube))
    dispatcher.add_handler(CommandHandler("download", download))

    # Text handler for commands
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, request_like))

    # Error handler
    dispatcher.add_error_handler(error)

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 
