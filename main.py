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
    
        window.render_all()
        
        libtcod.console_wait_for_keypress(True)
        
main()