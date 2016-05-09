import renderer.console as console
import tools.libtcod.libtcodpy as libtcod


class ViewportConsole(console.Console):
    def draw(self):
        for x in range(0, self.width):
            for y in range (0, self.height):
                if x == 0 or y == 0 or x == self.width-1 or y == self.height-1:
                    libtcod.console_put_char_ex(self.console, x, y, ' ', libtcod.black, libtcod.light_red)
                else:
                    libtcod.console_put_char(self.console, x, y, '.', libtcod.BKGND_NONE)
                    
        libtcod.console_put_char_ex(self.console, 30, 30, '@', libtcod.white, libtcod.BKGND_NONE)
        
        self.blit(self.parent_console)