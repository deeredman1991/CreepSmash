from renderer import console, viewport, stats_panel, inventory_panel, equipment_panel
import tools.toolbox as toolbox
import tools.libtcod.libtcodpy as libtcod


class RootConsole(console.Console):
    def __init__(self, jSettings):
        self.font_settings = jSettings.font
        libtcod.console_set_custom_font('fonts/{}'.format(self.font_settings['Fontname']), 
                                        libtcod.FONT_TYPE_GREYSCALE | self.font_settings['Layout'], 
                                        self.font_settings['Width'], self.font_settings['Height'])
                                 
        window_settings = jSettings.window
        self._settings = {
            "x": [0, window_settings["Width"]],
            "y": [0, window_settings["Height"]],
            "Width": window_settings["Width"],
            "Height": window_settings["Height"],
            "Console": libtcod.console_init_root(window_settings['Width'], window_settings['Height'], 'CreepSmash', window_settings['Fullscreen'])
        }
        
        _side_panels_width = int(self.width*0.20)
        _equipment_panel_height = 20
        _stats_panel_height = 2
        
        self.viewport = viewport.ViewportConsole (
            x = [0, self.width - _side_panels_width],
            y = [0, self.height - _stats_panel_height],
            parent_console = self
            )
        
        self.equipment_panel = equipment_panel.EquipmentPanelConsole (
            x = [self.viewport.width, self.width],
            y = [0, _equipment_panel_height],
            parent_console = self
            )
        
        self.inventory_panel = inventory_panel.InventoryPanelConsole (
            x = [self.viewport.width, self.width],
            y = [self.equipment_panel.height, self.height],
            parent_console = self
            )
        
        self.stats_panel = stats_panel.StatsPanelConsole (
            x = [0, self.width - _side_panels_width],
            y = [self.viewport.height, self.viewport.height + _stats_panel_height],
            parent_console = self
            )
        
    def render_all(self):
        self.draw()
        self.flush()
        
    def flush(self):
        libtcod.console_flush()
    
    def draw(self):
        self.viewport.draw()
        self.equipment_panel.draw()
        self.inventory_panel.draw()
        self.stats_panel.draw()