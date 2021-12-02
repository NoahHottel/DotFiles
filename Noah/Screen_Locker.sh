#!/bin/sh
# -*- coding: utf-8 -*-
#
# Screen_Locker.sh
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : GitHub.com/NoahHottel
# @Date   : 1/1/2021, 8:54:49 PM

# xautolock -detectsleep -time 10 -locker "i3lock-fancy" -killtime 15 -killer "systemctl suspend" -notify 30 -notifier "notify-send -u critical -t 10000 -- 'LOCKING screen in 30 seconds'" -corners 0-00
xautolock -detectsleep -time 10 -locker "i3lock-fancy" -notify 30 -notifier "notify-send -u critical -t 10000 -- 'LOCKING screen in 30 seconds'" -corners 0-00