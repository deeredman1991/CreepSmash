import renderer.console as console
import tools.toolbox as toolbox
import tools.libtcod.libtcodpy as libtcod


class RootConsole(console.Console):
    def __init__(self):
        self.font_settings = toolbox.parseJson('settings/font.json')
        libtcod.console_set_custom_font('fonts/{}'.format(self.font_settings['Fontname']), 
                                        libtcod.FONT_TYPE_GREYSCALE | self.font_settings['Layout'], 
                                        self.font_settings['Width'], self.font_settings['Height'])
        
        #print (self.font_settings)
        '''
        self.font_settings = toolbox.parseJson('settings/font.json')
        libtcod.console_set_custom_font('fonts/{}'.format(self.font_settings['Fontname']), 
                                        libtcod.FONT_TYPE_GREYSCALE | self.font_settings['Layout'], 
                                        self.font_settings['Width'], self.font_settings['Height'])
        '''                             
        window_settings = toolbox.parseJson('settings/window.json')
        self._settings = {
            "Width": window_settings["Width"],
            "Height": window_settings["Height"],
            "Console": libtcod.console_init_root(window_settings['Width'], window_settings['Height'], 'CreepSmash', window_settings['Fullscreen'])
        }
        self.equipment_panel = console.Console(
            width = int(self.width*0.20),
            height = 20
            )
        self.inventory_panel = console.Console(
            width = self.equipment_panel.width,
            height = self.height - self.equipment_panel.height
            )
        self.stats_panel = console.Console(
            width = self.width - self.inventory_panel.width,
            height = 2
            )
        self.viewport = console.Console (
            width = self.width - self.inventory_panel.width,
            height = self.height - self.stats_panel.height
            )
        
    def render_all(self):
        self.blit_all()
        self.flush()
        
    def flush(self):
        libtcod.console_flush()
        
    def blit_all(self):
        self.equipment_panel.blit(-self.viewport.width, 0, self.viewport.width + self.equipment_panel.width, self.equipment_panel.height, 0, 0, 0)
        self.inventory_panel.blit(-self.viewport.width, -self.equipment_panel.height, self.viewport.width + self.inventory_panel.width, self.height + self.inventory_panel.height, 0, 0, 0)
        self.stats_panel.blit(0, -self.viewport.height, self.stats_panel.width, self.stats_panel.height + self.viewport.height, 0, 0, 0)
        self.viewport.blit(0, 0, self.viewport.width,  self.viewport.height, 0, 0, 0)