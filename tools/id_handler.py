import tools.toolbox as toolbox
from tools.JDict import JDict

def get_unused_ID(jSettings):
    IDs_json = "{}/IDs.Json".format(jSettings.saving["LoadedSave"])
    ID_settings = JDict( IDs_json, toolbox.parseJson( IDs_json ) )
    
    if len(ID_settings["UnusedIDs"]) > 1:
        return ID_settings["UnusedIDs"].pop(0)
    else:
        ID_settings["LargestID"] += 1
        return ID_settings["LargestID"]
        
    
def recyle_ID(jSettings, ID):
    IDs_json = "{}/IDs.Json".format(jSettings.saving["LoadedSave"])
    ID_settings = JDict( IDs_json, toolbox.parseJson( IDs_json ) )
    
    ID_settings["UnusedIDs"].append(ID)
    