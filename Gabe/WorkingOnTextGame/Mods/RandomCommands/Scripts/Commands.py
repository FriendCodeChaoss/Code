import math
from Mods import mods


from Default_Stuff.Vars.Materials import Materails
from Default_Stuff.Vars.people import people
from Default_Stuff.Scripts.Time import Time
from Default_Stuff.Vars.TimeTrack import TimeTrack

#from main import people,Materails,TimeTrack,mods,Time,DataSave,LoadData,SaveNamePath,ext

def Stats():
    print(f"People:{math.floor(people.ammount)}")
    print(f"People per year:{math.floor(people.ammount*people.born)}")
    print(f"Deaths:{math.floor(people.ammount*people.death)}")
    print(f"Salt:{math.floor(Materails.mine.Salt)}")
def Help():
    print("This is an exsample command")
def Help2(arg):
    print(f"This is an ArgCommand command. the value that you have inputted will be",arg)

def Commands(SplitCommand):
    if SplitCommand[0] == "command":
        Help()
    elif SplitCommand[0] == "ArgCommand":
        if len(SplitCommand) > 1:
            Help2(SplitCommand[1])
        else:
            Help2(SplitCommand[1])