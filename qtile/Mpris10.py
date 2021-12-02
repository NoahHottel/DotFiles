#!python3
# -*- coding: utf-8 -*-
#
# Mpris10.py
# @Author : Noah Hottel (NoahHottel@Gmail.com)
# @Link   : https://github.com/NoahHottel
# @Date   : 11/11/2021, 8:53:01 PM
import mpris2
#from time import sleep

def Mpris100(player_str):

    player_uri ='vlc'
    player_uris = list(mpris2.get_players_uri())
 
    for uri in player_uris:
        if player_str in uri:
            player_uri = uri
            break

    return(player_uri)