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
                    
        libtcod.console_set_default_foreground(self.console, libtcod.white)
        libtcod.console_print(self.console, 0, 0, "INVENTORY")
        
        temp_inventory = []
        
        for i in range(0, self.height-2+1):
            temp_inventory.append(i)
        
        self.draw_inventory_list(temp_inventory)
        
        if temp_inventory >= self.height-1:
            self.draw_scroll_bar(temp_inventory)
                    
        self.blit()
        
    def draw_inventory_list(self, list):
        libtcod.console_set_default_foreground(self.console, libtcod.white)
        for k, v in enumerate(list):
            if k != self.height-2:
                libtcod.console_print(self.console, 1, k+1, str(v))
            
    def draw_scroll_bar(self, list):
        bar_size = (self.height-2)-(len(list)+4-self.height-2)
        if bar_size >= self.height-2:
            return
        elif bar_size < 3:
            bar_size = 3
        
        for i in range(2, self.height-2):
            libtcod.console_put_char_ex( self.console, self.width-2, i, ' ', libtcod.black, libtcod.gray)
        libtcod.console_put_char_ex( self.console, self.width-2, 1, '^', libtcod.black, libtcod.white)
        for i in range(2, bar_size):
            libtcod.console_put_char_ex( self.console, self.width-2, i, ' ', libtcod.black, libtcod.black)
        libtcod.console_put_char_ex( self.console, self.width-2, self.height-2, 'v', libtcod.black, libtcod.white)
        