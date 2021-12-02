#!/bin/bash

#Install Script
#NEEDS SUDO PRIVILAGES

#add repositories
wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/etc/apt/trusted.gpg.d/vscodium.gpg
sudo add-apt-repository ppa:libreoffice/ppa
echo 'deb https://paulcarroty.gitlab.io/vscodium-deb-rpm-repo/debs/ vscodium main' | sudo tee --append /etc/apt/sources.list.d/vscodium.list

#Apt update & upgrade
sudo apt update && sudo apt upgrade
#Install via apt
sudo apt install thunar firefox terminator xautolock feh flameshot pnmixer gimp pavucontrol playerctl thunderbird rofi compton i3lock-fancy qt5-style-plugins materia-gtk-theme lxappearance xfce4-power-manager network-manager-gnome policykit-1-gnome libxcb-render0-dev libffi-dev libpangocairo-1.0-0 vlc virtualbox virtualbox-guest-additions-iso libnotify4 kdeconnect gnucash steam-installer ttf-mscorefonts-installer codium libreoffice neofetch

#Install pip3
sudo apt install python3-pip

#install via pip3
pip3 install xlib
pip3 install dbus-next
pip3 install bpytop
pip3 install xcffib
pip3 install --no-cache-dir cairocffi
pip3 install qtile

#Qtile setup
export PATH="$HOME/.local/bin:$PATH"
#sudo echo "[Desktop Entry]\nName=Qtile\nComment=Qtile Session\nExec=qtile start\nType=Application\nKeywords=wm;tiling" > /usr/share/xsessions/qtile.desktop

#User Commands
echo "Please Download ExpressVPn and MultiMC on YOUR OWN"
