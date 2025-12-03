#!/bin/bash
echo "🧹 Cleaning system..."

sudo apt autoremove --purge -y
sudo apt autoclean -y
sudo apt clean -y

flatpak uninstall --delete-data
flatpak uninstall --unused

echo "✅ Cleaning complete!"