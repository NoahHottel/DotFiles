#!python3
# -*- coding: utf-8 -*-
#
# Monitors.py
# @Author : Noah Hottel
# @Link   : GitHub.com/NoahHottel
# @Date   : 9/16/2020, 1:41:42 PM
import os
import socket

from libqtile import bar, widget
from libqtile.config import Screen
from Xlib import display as Xdisplay

from Mpris10 import Mpris100



def Get_Monitor_Num():
    Monitor_num = 0
    try:
        Display = Xdisplay.Display()
        Screen = Display.screen()
        Resources = Screen.root.xrandr_get_screen_resources()

        for Output in Resources.outputs:
            Monitor = Display.xrandr_get_output_info(Output, Resources.config_timestamp)
            Preferred = False
            if hasattr(Monitor, "preferred"):
                Preferred = Monitor.preferred
            elif hasattr(Monitor, "num_preferred"):
                Preferred = Monitor.num_preferred
            if Preferred:
                Monitor_num += 1
    except Exception:
        # always setup at least one monitor
        return 1
    else:
        return Monitor_num

Monitor_num = Get_Monitor_Num()


### SCREENS ###

### PRIMARY SCREEN ###

screens = [
    Screen(
        top=bar.Bar(
                [
                widget.GroupBox(),
                widget.TextBox(
                    text                =   '|'
                ),
                widget.Notify(
                    width               =   bar.STRETCH
                ),
                widget.TextBox(
                    text                =   '|'
                ),
                widget.Mpris2(
                    objname             =   Mpris100('firefox'),
                    scroll_chars        =   None,
                    stop_pause_text     =   ''
                ),
                widget.TextBox(
                    text                =   '|'
                ),
                widget.Prompt(
                    prompt              =   "{0}@{1}: ".format(os.environ['USER'], socket.gethostname()),
                ),
                widget.Systray(),
                widget.TextBox(
                    text                =   '|'
                ),
                widget.Clock(
                    format              =   '%Y-%m-%d %a %H:%M'
                ),
                widget.QuickExit(
                    default_text        =   '[  Logout  ]',
                    countdown_format    =   '[  Sec: {}  ]'
                ),
                ],
                30,
            ),
        ),
]

### MULTIPLE / OTHER SCREENS ###

if Monitor_num > 1:
    for Monitor in range(Monitor_num - 1):
        screens.append(
            Screen(
                top=bar.Bar(
                    [
                        widget.GroupBox(),
                        widget.TextBox(
                            text                =   '|'
                        ),
                        widget.Mpris2(
                           objname             =   Mpris100('firefox'),
                           scroll_chars        =   None,
                           stop_pause_text     =   ''
                        ),
                        widget.Spacer(),
                        widget.TextBox(
                            text                =   '|'
                        ),
                        widget.Clock(
                            format              =   '%Y-%m-%d %a %H:%M'
                        ),
                        widget.QuickExit(
                            default_text        =   '[  Logout  ]',
                            countdown_format    =   '[  Sec: {}  ]'
                        ),
                    ],
                30,
                ),
            )
        )
