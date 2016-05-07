import os
import renderer.root_console as root_console
import tools.libtcod.libtcodpy as libtcod

if not os.path.exists('saves/autosave'):
    os.makedirs('saves/autosave')

root_console.init()

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
    libtcod.console_put_char(0, 1, 2, 'A', libtcod.BKGND_NONE)
    libtcod.console_put_char(0, 1, 3, 'B', libtcod.BKGND_NONE)
    libtcod.console_put_char(0, 1, 4, 'C', libtcod.BKGND_NONE)
    libtcod.console_flush()
    libtcod.console_wait_for_keypress(True)