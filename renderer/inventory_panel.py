import renderer.console as console
import tools.libtcod.libtcodpy as libtcod


class InventoryPanelConsole(console.Console):
    def draw(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                if x == 0 or y == 0 or x == self.width-1 or y == self.height-1:
                    libtcod.console_put_char_ex(self.console, x, y, ' ', libtcod.black, libtcod.dark_blue)
                else:
                    libtcod.console_put_char_ex(self.console, x, y, '*', libtcod.black, libtcod.light_blue)
                    
        self.blit()
        