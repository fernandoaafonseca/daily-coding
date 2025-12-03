#!/bin/bash

# Verifica se Zenity está instalado
command -v zenity >/dev/null 2>&1 || { echo "Zenity não está instalado. Execute: sudo apt install zenity"; exit 1; }

# Pede link
url=$(zenity --entry --title="YouTube Player" --text="Cole o link do YouTube:")
[ -z "$url" ] && exit 1

# Escolhe qualidade
quality=$(zenity --list --title="Qualidade" --radiolist \
  --column="Selecionado" --column="Qualidade" TRUE "360p" FALSE "480p" FALSE "720p")
[ -z "$quality" ] && exit 1
quality_num=${quality//p/}

# Escolhe ação
action=$(zenity --list --title="Ação" --radiolist \
  --column="Selecionado" --column="Ação" TRUE "Reproduzir" FALSE "Baixar")
[ -z "$action" ] && exit 1

# Executa ação
if [ "$action" = "Reproduzir" ]; then
    mpv --ytdl-format="bestvideo[height<=${quality_num}]+bestaudio/best[height<=${quality_num}]" "$url"
else
    yt-dlp -f "bestvideo[height<=${quality_num}]+bestaudio/best[height<=${quality_num}]" "$url"
fi

