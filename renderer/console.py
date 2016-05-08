import tools.libtcod.libtcodpy as libtcod


class Console():
    def __init__(self, x=[0,0], y=[0,0]):
        self._settings = {
            "x": x,
            "y": y,
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

    #   dst | The destination console.
    #   foregroundAlpha, backgroundAlpha | Normalized Alpha transparency of the blitted console.
    def blit(self, dst, foregroundAlpha = 1.0, backgroundAlpha = 1.0):
        libtcod.console_blit(self._settings["Console"], 0, 0, self.width, self.height, dst, self.x, self.y, foregroundAlpha, backgroundAlpha)