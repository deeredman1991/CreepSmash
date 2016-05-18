import tools.jpyon as JPyon
import tools.toolbox as toolbox

class Settings():
    def __init__(self):
        self.font = JPyon.JDict( "settings/font.json", toolbox.parseJson("settings/font") )
        self.keybindings = JPyon.JDict( "settings/keybindings.json", toolbox.parseJson("settings/keybindings") )
        self.music = JPyon.JDict( "settings/music.json", toolbox.parseJson("settings/music") )
        self.saving = JPyon.JDict( "settings/saving.json", toolbox.parseJson("settings/saving") )
        self.window = JPyon.JDict( "settings/window.json", toolbox.parseJson("settings/window") )