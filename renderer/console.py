import tools.libtcod.libtcodpy as libtcod


class Console(object):
    def __init__(self, x=[0,0], y=[0,0], parent_console=None):
        self._settings = {
            "x": x,
            "y": y,
            "Parent_Console": parent_console
        }
        self._settings["Width"] = int(max(self._settings["x"][1], self._settings["x"][0]) - min(self._settings["x"][1], self._settings["x"][0]))
        self._settings["Height"] = int(max(self._settings["y"][1], self._settings["y"][0]) - min(self._settings["y"][1], self._settings["y"][0]))
        self._settings["Console"] = libtcod.console_new(self._settings["Width"], self._settings["Height"])
        
    @property
    def x(self):
        return min(self._settings["x"][1], self._settings["x"][0])
        
    @property
    def y(self):
        return min(self._settings["y"][1], self._settings["y"][0])
        
    @property
    def height(self):
        return self._settings["Height"]
        
    @property
    def width(self):
        return self._settings["Width"]
        
    @property
    def console(self):
        return self._settings["Console"]
        
    @property
    def parent_console(self):
        return self._settings["Parent_Console"]

    #   destination_console | The destination to be blitted to.
    #   foregroundAlpha, backgroundAlpha | Normalized Alpha transparency of the blitted console.
    def blit(self, destination_console = None, foregroundAlpha = 1.0, backgroundAlpha = 1.0):
        destination_console = destination_console or self.parent_console.console
        libtcod.console_blit(self._settings["Console"], 0, 0, self.width, self.height, destination_console, self.x, self.y, foregroundAlpha, backgroundAlpha)