#!python3
# -*- coding: utf-8 -*-
#
# Keys.py
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : GitHub.com/NoahHottel
# @Date   : 10/1/2020, 12:24:05 PM
from libqtile.config import Key
from libqtile.lazy import lazy

from Commands import Commands
from Groups import group_names

mod = "mod4"
alt = "mod1"

keys = [
    # Switch between windows
    Key([alt],              "Tab",      lazy.layout.next(),                     desc="Move window focus to other window"),
    # Move windows
    Key([alt, "shift"],     "Tab",      lazy.layout.shuffle_down(),             desc= "Move window down"),
    # Grow / shrink windows
    Key([mod, "control"],   "Left",     lazy.layout.shrink(),                   lazy.layout.grow_left(),    desc= "Grow window to the left"),
    Key([mod, "control"],   "Right",    lazy.layout.grow(),                     lazy.layout.grow_right(),   desc= "Grow window to the right"),
    Key([mod, "control"],   "Up",       lazy.layout.maximize(),                 lazy.layout.grow_up(),      desc= "Grow window up"),
    Key([mod, "control"],   "Down",     lazy.layout.grow_down(),                                            desc= "Grow window down"),
    Key([mod, "control"],   "n",        lazy.layout.normalize(),                                            desc= "Normailize window"),
    # Toggle between different layouts as defined below
    Key([mod],              "Tab",      lazy.next_layout(),                     desc= "Toggle between layouts"),
    Key([mod],              "q",        lazy.window.kill(),                     desc= "Kill focused window"),
    # Misc commands
    Key([mod],              "l",        lazy.spawn(Commands.Lock_screen),       desc= "Lock with i3-fancy"),
    Key([mod],              "Return",   lazy.spawn(Commands.Terminal),          desc= "Launch terminal"),
    Key([mod, "control"],   "r",        lazy.restart(),                         desc= "Restart Qtile"),
    Key([mod, "control"],   "q",        lazy.shutdown(),                        desc= "Shutdown Qtile"),
    Key([mod],              "r",        lazy.spawncmd(),                        desc= "Spawn a command using a prompt widget"),
    # Backlight, Volume and music
    # Built-in Keyboard
    Key([], "XF86MonBrightnessUp",      lazy.spawn(Commands.Backlight_up),      desc= "Backlight up"),
    Key([], "XF86MonBrightnessDown",    lazy.spawn(Commands.Backlight_down),    desc= "Backlight down"),
    Key([], "XF86AudioRaiseVolume",     lazy.spawn(Commands.Audio_up),          desc= "Audio up"),
    Key([], "XF86AudioLowerVolume",     lazy.spawn(Commands.Audio_down),        desc= "Audio down"),
    Key([], "XF86AudioMute",            lazy.spawn(Commands.Audio_mute),        desc= "Audio mute toggle"),
    Key([], "XF86AudioPlay",            lazy.spawn(Commands.Music_play_pause),  desc= "Music play / pause"),
    Key([], "XF86AudioNext",            lazy.spawn(Commands.Music_next),        desc= "Music next"),
    Key([], "XF86AudioPrev",            lazy.spawn(Commands.Music_previous),    desc= "Music previous"),
    Key([], "XF86AudioStop",            lazy.spawn(Commands.Music_stop),        desc= "Music stop"),
    # Default
    Key([mod],              "Up",       lazy.spawn(Commands.Audio_up),          desc= "Audio up"),
    Key([mod],              "Down",     lazy.spawn(Commands.Audio_down),        desc= "Audio down"),
    Key([mod],              "space",    lazy.spawn(Commands.Music_play_pause),  desc= "Music play / pause"),
    Key([mod],              "Right",    lazy.spawn(Commands.Music_next),        desc= "Music next"),
    Key([mod],              "Left",     lazy.spawn(Commands.Music_previous),    desc= "Music previous"),
    # Screenshots
    Key([],                 "Print",    lazy.spawn(Commands.Screenshot),        desc= "Take a whole Screenshot"),
    Key([mod],              "Print",    lazy.spawn(Commands.Screenshot_reigion),desc= "Take a regioned Screenshot"),
    Key(["control"],        "Print",    lazy.spawn(Commands.Screenshot_delayed),desc= "Take a delayed Screenshot"),
    ]


for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))                                # Switch to another group
    keys.append(Key([mod, 'shift'], str(i), lazy.window.togroup(name)))                         # Send current window to another group
