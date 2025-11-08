import json, os

if __name__ == "__main__":
    from Default_Stuff.Scripts.SaveLoad import DataSave,LoadData
    from Default_Stuff.Vars.Materials import Materails
    from Default_Stuff.Vars.Jobs import Jobs
    from Default_Stuff.Scripts.Commands import Commands
    from Default_Stuff.Vars.Save import *
from Mods import mods
# ----- Save / Load -----

def Text():
    global mods
    global SaveNamePath
    Userin = input().strip().lower()
    SplitCommand = Userin.split(" ")
    Commands(SplitCommand)
    mods.run_all("Commands",SplitCommand)

def main():
    global mods

    print("type HTP for instructions")
    print("type help for commands")

    for attr in dir(Jobs):
        JobClass = getattr(Jobs, attr)
        if isinstance(JobClass, type):
            for sub_attr in dir(JobClass):
                if not sub_attr.startswith("__"):
                    value = getattr(JobClass, sub_attr)
                    if isinstance(value, (int, float)):
                        setattr(JobClass, sub_attr, value / 100)
    while True:
        choice = input("Load save y/n: ").strip().lower()
        if choice == "y":
            name = input("Load Save: ").strip().lower()
            SaveNamePath = f"save/{name}.{ext}"
            if LoadData(SaveNamePath):
                break
        elif choice == "n":
            name = input("Save Name: ").strip().lower()
            SaveNamePath = f"save/{name}.{ext}"
            break
    DataSave(SaveNamePath)
    print("Loaded mods:", mods.list_mods())

    # Main loop
    if Materails.mine.Salt == 69:
        import Funny
    while True:
        Text()

if __name__ == "__main__":
    main()
