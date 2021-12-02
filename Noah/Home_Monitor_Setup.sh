#!/bin/sh
# -*- coding: utf-8 -*-
#
# HomeMonitorSetup.sh
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : GitHub.com/NoahHottel
# @Date   : 9/16/2020, 12:49:45 PM

# Setup monitors for Laptop Use 2020 - 2021
#xrandr --output HDMI1 --primary --mode 1920x1080 --pos 1366x0 --rate 60.00 --rotate normal --output eDP1 --mode 1366x768 --pos 0x155 --rate 60.00 --rotate normal
# Setup monitors for Desktop Use 2021 - Present
xrandr --output DisplayPort-0 --off --output DisplayPort-1 --off --output HDMI-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --rate 60.00 --output DVI-0 --mode 1920x1080 --pos 0x0 --rotate normal --rate 60.00