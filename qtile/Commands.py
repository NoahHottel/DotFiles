#!python3
# -*- coding: utf-8 -*-
#
# Commands.py
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : GitHub.com/NoahHottel
# @Date   : 10/1/2020, 12:21:54 PM

class Commands:
    Terminal            =   'terminator'
    Lock_screen         =   'xautolock -locknow'
    Backlight_up        =   'xbacklight -inc 10'
    Backlight_down      =   'xbacklight -dec 10'
    Audio_up            =   'amixer -D pulse sset Master 5%+'
    Audio_down          =   'amixer -D pulse sset Master 5%-'
    Audio_mute          =   'amixer -D pulse set Master 1+ toggle'
    Music_play_pause    =   'playerctl play-pause'
    Music_next          =   'playerctl next'
    Music_previous      =   'playerctl previous'
    Music_stop          =   'playerctl stop'
    Screenshot          =   'flameshot full -p /home/nhottel/Pictures/Screenshots'
    Screenshot_reigion  =   'flameshot gui  -p /home/nhottel/Pictures/Screenshots'
    Screenshot_delayed  =   'flameshot full -p /home/nhottel/Pictures/Screenshots -d 5000'
    Power_manager       =   'xfce4-power-manager --customize'
    Browser             =   'firefox'
    Editor              =   'codium'
    File_manager        =   'thunar'
    Office              =   'libreoffice'
    Game                =   'steam'
    Music               =   'vlc'
    Photo_editor        =   'gimp'
    Mail                =   'thunderbird'
    Money               =   'gnucash'
    Group_www           =   ['Firefox']
    Group_dev           =   ['vscodium']
    Group_file          =   ['Thunar']
    Group_doc           =   ['libreoffice', 'Gnucash']
    Group_game          =   ['MultiMC', 'Steam']
    Group_music         =   ['vlc', 'Firefox']
    Group_sys           =   ['Terminator']
    Group_gfx           =   ['Gimp', 'Thunderbird']
