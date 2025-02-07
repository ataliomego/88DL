# YouTube Downloader Bot Telegram

![Banner](https://via.placeholder.com/1200x400.png?text=YouTube+Downloader+Bot+Telegram)

Bot Telegram sederhana dan kuat untuk mengunduh video dan audio YouTube dalam berbagai format. Mendukung pengunduhan MP3 (320 kbps), MP4 (480p, 720p, 1080p) dengan mudah dan memungkinkan pengguna untuk mencari video YouTube berdasarkan kata kunci.

## Fitur

- **Unduh Audio**: Mengunduh audio dari video YouTube dalam format MP3 (320 kbps).
- **Unduh Video**: Mengunduh video dalam format MP4 (480p, 720p, 1080p).
- **Cari YouTube**: Mencari video di YouTube menggunakan API YouTube.
- **Halaman Dukungan**: Meminta pengguna untuk mendukung bot dengan menyukai halaman Facebook.
- **Dukungan Multibahasa**: Pilih antara Bahasa Indonesia dan Bahasa Inggris untuk interaksi pengguna.

## Cara Kerja

1. **Kirim Link YouTube**: Pengguna cukup mengirimkan URL YouTube.
2. **Pilih Format**: Pilih format untuk mengunduh audio dalam MP3 (320 kbps) atau video dalam MP4 (480p, 720p, 1080p).
3. **Unduh File**: Bot akan mengirimkan tautan unduhan ke pengguna.
4. **Dukung Kami**: Setelah unduhan selesai, bot dengan sopan meminta pengguna untuk mendukung halaman Facebook bot.

## Instalasi

### Prasyarat

Pastikan Anda sudah menginstal:

- Python 3.7 atau lebih tinggi
- `pip` untuk menginstal dependensi Python

### Langkah-langkah

1. **Clone repository ini**:

   ```bash
   git clone https://github.com/username/telegram-youtube-downloader-bot.git
   cd telegram-youtube-downloader-bot

2. Siapkan Environment:

Buat file .env di direktori root dan tambahkan variabel berikut:

BOT_TOKEN=your-telegram-bot-token
YOUTUBE_API_KEY=your-youtube-api-key
API_ID=your-api-id
API_HASH=your-api-hash

Pastikan untuk mengganti placeholder dengan kredensial Anda yang sebenarnya:

BOT_TOKEN: Dapatkan token Anda dari BotFather.

YOUTUBE_API_KEY: Dapatkan API key Anda dari Google Cloud Console.

API_ID dan API_HASH: Jika perlu berinteraksi dengan API Telegram, buat aplikasi di my.telegram.org.



3. Instal Dependensi:

Instal semua pustaka Python yang dibutuhkan:

pip install -r requirements.txt


4. Jalankan Bot:

Mulai bot dengan perintah berikut:

python bot.py



Perintah

/start: Mulai bot dan pilih bahasa Anda (Bahasa Indonesia/Inggris).

/search <query>: Cari video YouTube berdasarkan kata kunci.

/download <YouTube URL> <format>: Unduh video/audio. Format: mp3, mp4 480p, mp4 720p, mp4 1080p.


Contoh Perintah:

1. Mulai Bot:

/start

Pilih bahasa Anda: Bahasa Indonesia atau Bahasa Inggris.




2. Cari Video:

/search never gonna give you up

Bot akan mencari video YouTube berdasarkan kueri Anda.




3. Unduh Video atau Audio:

/download https://www.youtube.com/watch?v=dQw4w9WgXcQ mp3

Perintah ini akan mengunduh audio dalam format MP3 (320kbps).


/download https://www.youtube.com/watch?v=dQw4w9WgXcQ mp4 720p

Perintah ini akan mengunduh video dalam format MP4 (720p).





Dukungan

Kami sangat menghargai dukungan Anda! Pertimbangkan untuk menyukai halaman Facebook Kami untuk membantu kami memperbaiki dan menjaga bot tetap berjalan dengan lancar.

Kontribusi

Kontribusi sangat diterima! Jika Anda memiliki saran atau ingin menambahkan fitur baru, silakan buka issue atau kirim pull request.

Langkah-langkah untuk berkontribusi:

1. Fork repository ini


2. Buat branch baru (git checkout -b feature-branch)


3. Commit perubahan Anda (git commit -m 'Add new feature')


4. Push ke branch (git push origin feature-branch)


5. Buka pull request



Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LICENSE untuk detailnya.


---

Catatan Pengembang

Bot ini dikembangkan dengan tujuan untuk menyederhanakan proses pengunduhan konten YouTube melalui Telegram. Kami berharap bot ini akan mempermudah dan menyenangkan Anda untuk mengunduh video dan audio favorit dari YouTube.

Selamat mengunduh! 🚀


---

Dibuat dengan ❤️ oleh [Nama Anda]
