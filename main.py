import os
import renderer.root_console as root_console
import tools.libtcod.libtcodpy as libtcod
import tools.toolbox as toolbox


keybindings = toolbox.parseJson('settings/keybindings')

print ( keybindings["KeyCodes"][ keybindings['Controls']['CamUp'] ] )
print ( keybindings["KeyCodes"][ keybindings['Controls']['CamDown'] ] )

window = root_console.RootConsole()

def main():
    if not os.path.exists('saves/autosave'):
        os.makedirs('saves/autosave')

    

    while not libtcod.console_is_window_closed():
        libtcod.console_set_default_foreground(0, libtcod.white)
        for x in range(0, window.viewport.width):
            for y in range (0, window.viewport.height):
                if x == 0 or y == 0 or x == window.viewport.width-1 or y == window.viewport.height-1:
                    libtcod.console_put_char_ex(window.viewport.console, x, y, ' ', libtcod.black, libtcod.light_red)
                else:
                    libtcod.console_put_char(window.viewport.console, x, y, '.', libtcod.BKGND_NONE)
                if x == 0 and y == 0:
                    libtcod.console_put_char_ex(window.viewport.console, x, y, '0', libtcod.black, libtcod.light_red)
                    
        for x in range(0, window.stats_panel.width):
            for y in range(0, window.stats_panel.height):
                if x != window.stats_panel.width and y != window.stats_panel.height:
                    libtcod.console_put_char_ex(window.stats_panel.console, x, y, ' ', libtcod.black, libtcod.light_orange)
                
        for x in range(0, window.inventory_panel.width):
            for y in range(0, window.inventory_panel.height):
                if x == 0 or y == 0 or x == window.inventory_panel.width-1 or y == window.inventory_panel.height-1:
                    libtcod.console_put_char_ex(window.inventory_panel.console, x, y, ' ', libtcod.black, libtcod.dark_blue)
                else:
                    libtcod.console_put_char_ex(window.inventory_panel.console, x, y, '*', libtcod.black, libtcod.light_blue)
                
        for x in range(0, window.equipment_panel.width):
            for y in range(0, window.equipment_panel.height):
                if x == 0 or y == 0 or x == window.equipment_panel.width-1 or y == window.equipment_panel.height-1:
                    libtcod.console_put_char_ex(window.equipment_panel.console, x, y, ' ', libtcod.black, libtcod.dark_purple)
                else:
                    libtcod.console_put_char_ex(window.equipment_panel.console, x, y, '/', libtcod.black, libtcod.light_purple)
                
        libtcod.console_put_char(window.viewport.console, 1, 1, '@', libtcod.BKGND_NONE)
        libtcod.console_put_char(window.viewport.console, 1, 2, 'A', libtcod.BKGND_NONE)
        libtcod.console_put_char(window.viewport.console, 1, 3, 'B', libtcod.BKGND_NONE)
        libtcod.console_put_char(window.viewport.console, 1, 4, 'C', libtcod.BKGND_NONE)
        
        window.render_all()
        
        libtcod.console_wait_for_keypress(True)
    
    
main()