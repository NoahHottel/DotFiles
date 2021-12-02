#!/bin/sh
# -*- coding: utf-8 -*-
#
# autostart.sh
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : GitHub.com/NoahHottel
# @Date   : 9/12/2020, 7:50:54 PM

nm-applet --indicator   &   # Wifi indicator
pnmixer                 &   # Sound indicator
xfce4-power-manager     &   # Power indicator
flameshot               &   # Screenshot manager
steam -silent           &   # Game client
kdeconnect-indicator    &   # Phone connector
compton		            &   # Transparency
#blueman-applet          &   # Bluetooth Manager
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 & #Run applications as Sudo

cd ~
./.config/Noah/Home_Monitor_Setup.sh &
./.config/Noah/Screen_Locker.sh &
