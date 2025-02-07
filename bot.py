import os
import logging
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters, CallbackContext
)
from yt_dlp import YoutubeDL

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Load API Keys from .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing in .env file!")

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY is missing in .env file!")

# Function to handle /start command
async def start(update: Update, context: CallbackContext):
    lang = update.message.text.split(' ', 1)[-1] if len(update.message.text.split()) > 1 else 'en'
    
    if lang == 'id':
        await update.message.reply_text("Selamat datang! Kirimkan link YouTube untuk mengunduh video/audio. Pilih format: MP3 320kbps, MP4 480p, 720p, atau 1080p.")
    else:
        await update.message.reply_text("Welcome! Send a YouTube link to download video/audio. Choose format: MP3 320kbps, MP4 480p, 720p, or 1080p.")

# Function to search YouTube for videos
async def search_youtube(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("Please provide a search query. Example: /search lo-fi music")
        return

    query = " ".join(context.args)
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YOUTUBE_API_KEY}"
    
    response = requests.get(search_url).json()
    if 'items' in response:
        videos = response['items']
        message = "🔍 *Here are the search results:*\n\n"
        for i, video in enumerate(videos[:5]):
            title = video['snippet']['title']
            video_id = video['id'].get('videoId', 'N/A')
            if video_id != 'N/A':
                message += f"{i+1}. [{title}](https://youtu.be/{video_id})\n"
        
        await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text("No results found.")

# Function to download audio/video
async def download(update: Update, context: CallbackContext):
    if len(context.args) < 1:
        await update.message.reply_text("Usage: /download <YouTube URL> <format (mp3/mp4)>")
        return

    url = context.args[0]
    format_choice = context.args[1] if len(context.args) > 1 else 'mp3'

    ydl_opts = {
        'format': 'bestaudio/best' if format_choice == 'mp3' else 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'}] if format_choice == 'mp3' else [],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if format_choice == 'mp3':
                filename = filename.replace(".webm", ".mp3").replace(".m4a", ".mp3")

            with open(filename, 'rb') as file:
                if format_choice == 'mp3':
                    await update.message.reply_audio(file, caption="🎵 Here's your audio file!")
                else:
                    await update.message.reply_video(file, caption="🎥 Here's your video file!")

        # Remove file after sending to user
        os.remove(filename)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# Function to request like on Facebook page
async def request_like(update: Update, context: CallbackContext):
    try:
        with open("support.txt", "r") as file:
            fb_link = file.read().strip()
        await update.message.reply_text(f"🙏 Mohon dukungan dengan like halaman Facebook kami: {fb_link}\nTerima kasih telah menggunakan bot ini!")
    except Exception:
        await update.message.reply_text("❌ Error: Tidak dapat membaca file support.txt.")

# Error handling function
async def error(update: Update, context: CallbackContext):
    logger.warning(f"⚠️ Update {update} caused error {context.error}")

# Main function to start the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("search", search_youtube))
    application.add_handler(CommandHandler("download", download))

    # Message handler for Facebook request
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, request_like))

    # Error handler
    application.add_error_handler(error)

    # Start bot
    application.run_polling()

if __name__ == '__main__':
    main()
