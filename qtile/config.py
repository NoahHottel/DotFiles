#!python3
# -*- coding: utf-8 -*-
#
# config.py
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : GitHub.com/NoahHottel
# @Date   : 9/7/2020, 5:46:12 PM

### IMPORTS ###
import os
import subprocess

from libqtile import hook, layout
from libqtile.config import Match

from Groups import groups
from Keys import keys
from Monitors import screens

### LAYOUTS / WIDGETS ###

layouts = [
    layout.Max(),
    layout.MonadTall(border_focus='#2222ff'),
    layout.TreeTab(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


@hook.subscribe.startup_once
def Autostart():
    Home = os.path.expanduser('~/.config/Noah/Autostart.sh')
    subprocess.call([Home])

@hook.subscribe.startup
def Restart():
    Home = os.path.expanduser('~/.config/Noah/Restart.sh')
    subprocess.call([Home])
### DEFAULTS ###

wmname = "Qtile"
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    Match(wm_class   =  'confirm'),
    Match(wm_class   =   'dialog'),
    Match(wm_class   =   'download'),
    Match(wm_class   =   'error'),
    Match(wm_class   =   'file_progress'),
    Match(wm_class   =   'notification'),
    Match(wm_class   =   'splash'),
    Match(wm_class   =   'toolbar'),
    Match(wm_class   =   'confirmreset'),  # gitk
    Match(wm_class   =   'makebranch'),  # gitk
    Match(wm_class   =   'maketag'),  # gitk
    Match(title     =   'branchdialog'),  # gitk
    Match(title     =   'pinentry'),  # GPG key password entry
    Match(wm_class   =   'ssh-askpass'),  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
