import os.path
import shutil
import tools.toolbox as toolbox
import tools.libtcod.libtcodpy as libtcod

def init():
    font_settings = toolbox.parseJson('settings/font.json')
    libtcod.console_set_custom_font('fonts/{}'.format(font_settings['Fontname']), libtcod.FONT_TYPE_GREYSCALE | font_settings['Layout'], font_settings['Width'], font_settings['Height'])
    
    window_settings = toolbox.parseJson('settings/window.json')
    libtcod.console_init_root(window_settings['Width'], window_settings['Height'], 'CreepSmash', window_settings['Fullscreen'])