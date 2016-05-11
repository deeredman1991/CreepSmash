import tools.toolbox as toolbox
import os.path
import shutil
import tools.QJson as QJson

def get_unused_ID(jSettings):
    IDs_json = "{}/IDs.json".format(jSettings.saving["LoadedSave"])
    
    if not os.path.isfile(IDs_json):
        shutil.copyfile('saves/.defaults/IDs.json', IDs_json)
    
    ID_settings = QJson.JDict( IDs_json, toolbox.parseJson( IDs_json ) )
    
    if len(ID_settings["UnusedIDs"]) > 1:
        return ID_settings["UnusedIDs"].pop(0)
    else:
        nextID = ID_settings["NextID"]
        ID_settings["NextID"] = nextID + 1
        return nextID
        
    
def recycle_ID(jSettings, ID):
    IDs_json = "{}/IDs.json".format(jSettings.saving["LoadedSave"])
    
    if not os.path.isfile(IDs_json):
        shutil.copyfile( 'saves/.defaults/IDs.json', IDs_json )
    
    ID_settings = QJson.JDict( IDs_json, toolbox.parseJson( IDs_json ) )
    
    print("---")
    
    print(ID)
    print(ID_settings["UnusedIDs"])
    
    ID_settings["UnusedIDs"].append(ID)
    
    print(ID)
    print(ID_settings["UnusedIDs"])
    