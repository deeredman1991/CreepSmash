import renderer.console as console
import tools.libtcod.libtcodpy as libtcod

class StatsPanelConsole(console.Console):
    def __init__(self, *args, **kwargs):
        super(StatsPanelConsole, self).__init__(*args, **kwargs)
        self.major_stats = 0
        
    def draw(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                if x == 0 or y == 0 or x == self.width-1 or y == self.height-1:
                    libtcod.console_put_char_ex(self.console, x, y, ' ', libtcod.black, libtcod.light_orange) 
                else:
                    libtcod.console_put_char_ex(self.console, x, y, '.', libtcod.white, libtcod.dark_orange)
        
        #Placeholder code for drawing health and mana values to screen!
        self.draw_major_stat("HEALTH", 250, 250, libtcod.darker_red, libtcod.darker_green)
        self.draw_major_stat("ARKANA", 500, 1000, libtcod.darker_blue, libtcod.darker_blue)
        
        self.blit()
        self.major_stats = 0
        
    def draw_major_stat(self, stat_name, stat_curr_value, stat_max_value, bar_color, text_color):
        stat_location = self.width/6 + self.major_stats*20
        self.major_stats += 1
        
        libtcod.console_set_default_foreground(self.console,libtcod.black)
        stat_name = '{}: '.format(stat_name)
        libtcod.console_print(self.console, stat_location-len(stat_name), 0, stat_name)
        
        for x in range(stat_location, stat_location+10):
            libtcod.console_put_char_ex(self.console, x, 0, '|', bar_color, libtcod.light_orange)
            
        stat_value = '{}/{}'.format(stat_curr_value, stat_max_value)
        if stat_curr_value <= stat_max_value*0.50:
            text_color = libtcod.dark_red
        libtcod.console_set_default_foreground(self.console, text_color)
        libtcod.console_print(self.console, stat_location+5-len(stat_value)/2, 1, stat_value)