import os.path
import shutil
import tools.toolbox as toolbox
import tools.libtcod.libtcodpy as libtcod

def init():
    if not os.path.isfile('settings/font.json'):
        shutil.copyfile('settings/.defaults/font.json', 'settings/font.json')
    font_settings = toolbox.parseJson('settings/font.json')
    libtcod.console_set_custom_font('fonts/{}'.format(font_settings['Fontname']), libtcod.FONT_TYPE_GREYSCALE | font_settings['Layout'], font_settings['Width'], font_settings['Height'])
    
    if not os.path.isfile('settings/window.json'):
        shutil.copyfile('settings/.defaults/window.json', 'settings/window.json')
    window_settings = toolbox.parseJson('settings/window.json')
    libtcod.console_init_root(window_settings['Width'], window_settings['Height'], 'CreepSmash', window_settings['Fullscreen'])