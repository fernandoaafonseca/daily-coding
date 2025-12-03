#!/bin/bash
echo "🔧 Cleaning and maintaining system..."

sudo apt --fix-broken install

sudo apt update -y
sudo apt upgrade -y
#sudo apt full-upgrade -y

sudo apt autoremove --purge -y
sudo apt autoclean -y
sudo apt clean -y

flatpak uninstall --delete-data
flatpak uninstall --unused

# Remove órfãos de kernels não usados
sudo update-initramfs -u
sudo update-grub

echo "✅ Maintenance complete!"

