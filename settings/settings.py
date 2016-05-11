import tools.QJson as QJson
import tools.toolbox as toolbox

class Settings():
    def __init__(self):
        self.font = QJson.JDict( "settings/font", toolbox.parseJson("settings/font") )
        self.keybindings = QJson.JDict( "settings/keybindings", toolbox.parseJson("settings/keybindings") )
        self.music = QJson.JDict( "settings/music", toolbox.parseJson("settings/music") )
        self.saving = QJson.JDict( "settings/saving", toolbox.parseJson("settings/saving") )
        self.window = QJson.JDict( "settings/window", toolbox.parseJson("settings/window") )