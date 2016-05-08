import os
import renderer.render as render
import tools.libtcod.libtcodpy as libtcod
import tools.toolbox as toolbox


keybindings = toolbox.parseJson('settings/keybindings')

print ( keybindings["KeyCodes"][ keybindings['Controls']['CamUp'] ] )
print ( keybindings["KeyCodes"][ keybindings['Controls']['CamDown'] ] )

console = render.Console()

def main():
    if not os.path.exists('saves/autosave'):
        os.makedirs('saves/autosave')

    

    while not libtcod.console_is_window_closed():
        libtcod.console_set_default_foreground(0, libtcod.white)
        for x in range(0, console.viewport['Width']):
            for y in range (0, console.viewport['Height']):
                if x == 0 or y == 0 or x == console.viewport['Width']-1 or y == console.viewport['Height']-1:
                    libtcod.console_put_char_ex(console.viewport['Console'], x, y, ' ', libtcod.black, libtcod.light_red)
                else:
                    libtcod.console_put_char(console.viewport['Console'], x, y, '.', libtcod.BKGND_NONE)
                    
                
        for x in range(0, console.stats_panel['Width']):
            for y in range(0, console.stats_panel['Height']):
                if x != console.stats_panel['Width'] and y != console.stats_panel['Height']:
                    libtcod.console_put_char_ex(console.stats_panel['Console'], x, y, ' ', libtcod.black, libtcod.light_orange)
                
        for x in range(0, console.inventory_panel['Width']):
            for y in range(0, console.inventory_panel['Height']):
                if x == 0 or y == 0 or x == console.inventory_panel['Width']-1 or y == console.inventory_panel['Height']-1:
                    libtcod.console_put_char_ex(console.inventory_panel['Console'], x, y, ' ', libtcod.black, libtcod.dark_blue)
                else:
                    libtcod.console_put_char_ex(console.inventory_panel['Console'], x, y, '*', libtcod.black, libtcod.light_blue)
                
        for x in range(0, console.equipment_panel['Width']):
            for y in range(0, console.equipment_panel['Height']):
                if x == 0 or y == 0 or x == console.equipment_panel['Width']-1 or y == console.equipment_panel['Height']-1:
                    libtcod.console_put_char_ex(console.equipment_panel['Console'], x, y, ' ', libtcod.black, libtcod.dark_purple)
                else:
                    libtcod.console_put_char_ex(console.equipment_panel['Console'], x, y, '/', libtcod.black, libtcod.light_purple)
                
        libtcod.console_put_char(console.viewport["Console"], 1, 1, '@', libtcod.BKGND_NONE)
        libtcod.console_put_char(console.viewport["Console"], 1, 2, 'A', libtcod.BKGND_NONE)
        libtcod.console_put_char(console.viewport["Console"], 1, 3, 'B', libtcod.BKGND_NONE)
        libtcod.console_put_char(console.viewport["Console"], 1, 4, 'C', libtcod.BKGND_NONE)
        
        console.render_all()
        
        libtcod.console_wait_for_keypress(True)
    
    
main()