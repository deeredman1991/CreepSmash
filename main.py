# The MIT License (MIT)
# 
# Copyright (c) 2016 deeredman1991
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import renderer.root_console as root_console
import tools.audio_player as audio_player
import tools.libtcod.libtcodpy as libtcod
import settings.settings as jSettings

settings = jSettings.Settings()
keybindings = settings.keybindings

print ( keybindings["KeyCodes"][ keybindings['Controls']['CamUp'] ] )
print ( keybindings["KeyCodes"][ keybindings['Controls']['CamDown'] ] )

window = root_console.RootConsole(settings)
audio_player = audio_player.AudioPlayer(settings)

def main():
    if not os.path.exists('saves/autosave'):
        os.makedirs('saves/autosave')
        
    while not libtcod.console_is_window_closed():
        
        if audio_player.music_track == None:
            audio_player.music_track = audio_player.music_settings["WorldTheme"]
        
        window.render_all()
        
        libtcod.console_wait_for_keypress(True)
        
main()