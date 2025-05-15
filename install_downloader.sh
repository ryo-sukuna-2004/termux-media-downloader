#!/data/data/com.termux/files/usr/bin/bash
clear
echo "📥 Installing Termux Media Downloader by ryo_sukuna_2004"
pkg update && pkg upgrade -y
pkg install python ffmpeg git -y
pip install yt-dlp spotdl mutagen rich

echo "✅ Setup complete!"
echo "▶️ Now run:"
echo "python termux_downloader.py"
