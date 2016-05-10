from tools.JDict import JDict
import tools.toolbox as toolbox

class Settings():
    def __init__(self):
        self.font = JDict( "settings/font", toolbox.parseJson("settings/font") )
        self.keybindings = JDict( "settings/keybindings", toolbox.parseJson("settings/keybindings") )
        self.music = JDict( "settings/music", toolbox.parseJson("settings/music") )
        self.saving = JDict( "settings/saving", toolbox.parseJson("settings/saving") )
        self.window = JDict( "settings/window", toolbox.parseJson("settings/window") )