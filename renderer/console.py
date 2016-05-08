import tools.libtcod.libtcodpy as libtcod


class Console():
    def __init__(self, width=0, height=0):
        self._settings = {
            "Width": width,
            "Height": height,
            "Console": libtcod.console_new(width, height)
        }
        
    @property
    def height(self):
        return self._settings["Height"]
        
    @property
    def width(self):
        return self._settings["Width"]
        
    @property
    def console(self):
        return self._settings["Console"]

    #   xSrc,ySrc,wSrc,hSrc | The rectangular area of the source console that will be blitted. If wSrc and/or hSrc == 0, the source console width/height are used
    #   dst | The destination console.
    #   xDst,yDst | Where to blit the upper-left corner of the source area in the destination console.
    #   foregroundAlpha,backgroundAlpha | normalized Alpha transparency of the blitted console.
    def blit(self, xSrc, ySrc, wSrc, hSrc, dst, xDst, yDst, foregroundAlpha=1.0, backgroundAlpha=1.0):
        libtcod.console_blit(self._settings["Console"], xSrc, ySrc, wSrc, hSrc, dst, xDst, yDst, foregroundAlpha, backgroundAlpha)