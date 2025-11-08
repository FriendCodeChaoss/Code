import json
import os

#scripts
from Default_Stuff.Scripts.JsonManage import *

#vars
from Default_Stuff.Vars.Coins import Coins
from Default_Stuff.Vars.Materials import Materails
from Default_Stuff.Vars.Jobs import Jobs
from Default_Stuff.Vars.people import people


def DataSave(SaveNamePath):
    data = {
        "people": ClassToJson(people),
        "Materails": ClassToJson(Materails),
        "Coins": ClassToJson(Coins),
        "Jobs": ClassToJson(Jobs),
    }
    json_data = json.dumps(data, indent=4)
    os.makedirs("save", exist_ok=True)

    if os.path.exists(SaveNamePath):
        os.remove(SaveNamePath)
    with open(SaveNamePath, "w") as f:
        f.write(json_data)

def LoadData(path):
    if not os.path.exists(path):
        print("Save file not found:", path)
        return False
    with open(path, "r") as f:
        data = json.load(f)

    JsonToClass(data.get("people", {}), people)
    JsonToClass(data.get("Materails", {}), Materails)
    JsonToClass(data.get("Coins", {}), Coins)
    JsonToClass(data.get("Jobs", {}), Jobs)
    return True