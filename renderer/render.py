import os.path
import shutil
import tools.toolbox as toolbox
import tools.libtcod.libtcodpy as libtcod


class Console():
    def __init__(self):
        self.font_settings = toolbox.parseJson('settings/font.json')
        libtcod.console_set_custom_font('fonts/{}'.format(self.font_settings['Fontname']), 
                                        libtcod.FONT_TYPE_GREYSCALE | self.font_settings['Layout'], 
                                        self.font_settings['Width'], self.font_settings['Height'])
        
        self.root = toolbox.parseJson('settings/window.json')
        self.root["Console"] = libtcod.console_init_root(self.root['Width'], self.root['Height'], 'CreepSmash', self.root['Fullscreen'])
        
        self.equipment_panel = {
            "Width": int(self.root["Width"]*0.20),
            "Height": 20
        }
        self.equipment_panel["Console"] = libtcod.console_new(self.equipment_panel["Width"], self.equipment_panel["Height"])
        
        self.inventory_panel = {
            "Width": self.equipment_panel["Width"],
            "Height": self.root["Height"]-self.equipment_panel["Height"]
        }
        self.inventory_panel["Console"] = libtcod.console_new(self.inventory_panel["Width"], self.inventory_panel["Height"])
        
        self.stats_panel = {
            "Width": self.root["Width"]-self.inventory_panel["Width"],
            "Height": 2
            }
        self.stats_panel["Console"] = libtcod.console_new(self.stats_panel["Width"], self.stats_panel["Height"])
        
        self.viewport = {
            "Width": self.root["Width"]-self.inventory_panel["Width"],
            "Height": self.root["Height"] - self.stats_panel["Height"]
        }
        self.viewport["Console"] = libtcod.console_new(self.viewport['Width'], self.viewport['Height'])
        
    def render_all(self):
        self.blit_all()
        self.flush()
        
    def flush(self):
        libtcod.console_flush()
        
    def blit_all(self):
        self.blit_equipment_panel()
        self.blit_inventory_panel()
        self.blit_stats_panel()
        self.blit_viewport()
        
    def blit_equipment_panel(self):
        libtcod.console_blit(self.equipment_panel["Console"], -self.viewport["Width"], 0, self.viewport["Width"]+self.equipment_panel["Width"], self.equipment_panel["Height"], 0, 0, 0)
        
    def blit_inventory_panel(self):
        libtcod.console_blit(self.inventory_panel["Console"], -self.viewport["Width"], -self.equipment_panel["Height"], self.viewport["Width"]+self.inventory_panel["Width"], self.root["Height"]+self.inventory_panel["Height"], 0, 0, 0)
        
    def blit_stats_panel(self):
        libtcod.console_blit(self.stats_panel["Console"], 0, -self.viewport["Height"], self.stats_panel["Width"], self.stats_panel["Height"]+self.viewport["Height"], 0, 0, 0)
        
    def blit_viewport(self):
        libtcod.console_blit(self.viewport["Console"], 0, 0, self.viewport["Width"],  self.viewport["Height"], 0, 0, 0)
        #libtcod.console_blit(self.viewport, camera.x-(SCREEN_WIDTH/2), (camera.y-((SCREEN_HEIGHT)-PANEL_HEIGHT)/2), camera.x+(SCREEN_WIDTH/2), (camera.y+((SCREEN_HEIGHT)-PANEL_HEIGHT)/2), 0, 0, 0)
