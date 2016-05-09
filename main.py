import os
import renderer.root_console as root_console
import tools.audio_player as audio_player
import tools.libtcod.libtcodpy as libtcod
import tools.toolbox as toolbox

keybindings = toolbox.parseJson('settings/keybindings')

print ( keybindings["KeyCodes"][ keybindings['Controls']['CamUp'] ] )
print ( keybindings["KeyCodes"][ keybindings['Controls']['CamDown'] ] )

window = root_console.RootConsole()
audio_player = audio_player.AudioPlayer()

def main():
    if not os.path.exists('saves/autosave'):
        os.makedirs('saves/autosave')
        
    while not libtcod.console_is_window_closed():
        
        if audio_player.music_track == None:
            audio_player.music_track = audio_player.music_settings["WorldTheme"]
        
        window.render_all()
        
        libtcod.console_wait_for_keypress(True)
        
main()