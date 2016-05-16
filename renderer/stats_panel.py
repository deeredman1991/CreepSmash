import renderer.console as console
import tools.libtcod.libtcodpy as libtcod


class StatsPanelConsole(console.Console):
    def draw(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                if x == 0 or y == 0 or x == self.width-1 or y == self.height-1:
                    libtcod.console_put_char_ex(self.console, x, y, ' ', libtcod.black, libtcod.light_orange) 
                else:
                    libtcod.console_put_char_ex(self.console, x, y, '.', libtcod.white, libtcod.dark_orange)
        #Placeholder code for drawing health and mana values to screen!
        health_location = self.width/6
        
        libtcod.console_set_default_foreground(self.console,libtcod.black)
        
        health_string = "HEALTH: "
        libtcod.console_print(self.console, health_location-len(health_string), 0, health_string)
        
        for x in range(health_location, health_location+10):
            libtcod.console_put_char_ex(self.console, x, 0, '|', libtcod.darker_red, libtcod.light_orange)
            
        libtcod.console_set_default_foreground(self.console,libtcod.darker_green)
        health_string = "250/250"
        libtcod.console_print(self.console, health_location+5-len(health_string)/2, 1, health_string)
        
        mana_location = self.width/6+20
        
        libtcod.console_set_default_foreground(self.console,libtcod.black)
        mana_string = "MANA: "
        libtcod.console_print(self.console, mana_location-len(mana_string), 0, mana_string)
        
        for x in range(mana_location, mana_location+10):
            libtcod.console_put_char_ex(self.console, x, 0, '|', libtcod.darker_blue, libtcod.light_orange)
            
        libtcod.console_set_default_foreground(self.console,libtcod.darker_blue)
        mana_string = "1000/1000"
        libtcod.console_print(self.console, mana_location+5-len(mana_string)/2, 1, mana_string)
        
        
        
        #End of placeholder code.
        self.blit()