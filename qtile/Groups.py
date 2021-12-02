#!python3
# -*- coding: utf-8 -*-
#
# Groups.py
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : GitHub.com/NoahHottel
# @Date   : 10/1/2020, 12:30:06 PM
from libqtile.config import Group, Match

from Commands import Commands

group_names = [
    ('WWW',  {'layout': 'max',       'persist': True, 'matches': [Match(wm_class=Commands.Group_www)],   'init': True, 'label': '' ,'spawn': Commands.Browser                      }),
    ('DEV',  {'layout': 'max',       'persist': True, 'matches': [Match(wm_class=Commands.Group_dev)],   'init': True, 'label': '' ,'spawn': Commands.Editor                       }),
    ('FILE', {'layout': 'monadtall', 'persist': True, 'matches': [Match(wm_class=Commands.Group_file)],  'init': True, 'label': '' ,'spawn': Commands.File_manager                 }),
    ('DOC',  {'layout': 'max',       'persist': True, 'matches': [Match(wm_class=Commands.Group_doc)],   'init': True, 'label': '' ,'spawn': Commands.Money                        }),
    ('GAME', {'layout': 'max',       'persist': True, 'matches': [Match(wm_class=Commands.Group_game)],  'init': True, 'label': ''                                                 }),
    ('MUSIC',{'layout': 'max',       'persist': True, 'matches': [Match(wm_class=Commands.Group_music)], 'init': True, 'label': ''                                                 }),
    ('SYS',  {'layout': 'monadtall', 'persist': True, 'matches': [Match(wm_class=Commands.Group_sys)],   'init': True, 'label': '' ,'spawn': Commands.Terminal                     }),
    ('GFX',  {'layout': 'max',       'persist': True, 'matches': [Match(wm_class=Commands.Group_gfx)],   'init': True, 'label': '' ,'spawn': Commands.Mail                         })
    ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]
