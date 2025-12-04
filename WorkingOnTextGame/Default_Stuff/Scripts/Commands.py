from math import floor

from Mods import mods

#scripts
from Default_Stuff.Scripts.SaveLoad import DataSave,LoadData,SaveNamePath,ext
from Default_Stuff.Scripts.Time import Time

#vars
from Default_Stuff.Vars.Materials import Materails
from Default_Stuff.Vars.people import people
from Default_Stuff.Vars.TimeTrack import TimeTrack,MonthDays

def Stats():
    print(f"People:{floor(people.ammount)}")
    print(f"People per year:{floor(people.ammount*people.born)}")
    print(f"Deaths:{floor(people.ammount*people.death)}")
    print(f"Salt:{floor(Materails.mine.Salt)}")
def Help():
    print("type save to save data. Every month it will auto save")
    print("stats for current stats")

def HTP():
    print("To go to the next time you type time")
    print("you then need to type [Day,Week,Month,Year]")
    print("This can be shortened to [D,W,M,Y]")

def CalculateDay():
    days_in_month = MonthDays.get_days(TimeTrack.Year)
    while TimeTrack.Day > days_in_month[TimeTrack.Month]:
        TimeTrack.Day -= days_in_month[TimeTrack.Month]
        TimeTrack.Month += 1
        if TimeTrack.Month > 12:
            TimeTrack.Month = 1
            TimeTrack.Year += 1
            days_in_month = MonthDays.get_days(TimeTrack.Year)
    print(f"Day: {TimeTrack.Day}, Month: {TimeTrack.Month}, Year: {TimeTrack.Year}")
        
CalculateDay()
def Commands(SplitCommand):
    days_in_month = MonthDays.get_days(TimeTrack.Year)
    if SplitCommand[0] == "help":
        Help()
    elif SplitCommand[0] == "htp":
        HTP()
    elif SplitCommand[0] == "stats":
        Stats()
    elif SplitCommand[0] in ("d", "day"):
        TimeTrack.Day += 1
        mods.run_all("Time", 1)
        Time(1)
        CalculateDay()
        print(f"You have {floor(people.ammount)} people")

    elif SplitCommand[0] in ("w", "week"):
        TimeTrack.Day += 7
        mods.run_all("Time", 7)
        Time(7)
        CalculateDay()
        print(f"You have {floor(people.ammount)} people")

    elif SplitCommand[0] in ("m", "month"):
        days_in_month = MonthDays.get_days(TimeTrack.Year)
        TimeTrack.Day += days_in_month[TimeTrack.Month]
        mods.run_all("Time", days_in_month[TimeTrack.Month])
        Time(days_in_month[TimeTrack.Month])
        CalculateDay()
        print(f"You have {floor(people.ammount)} people")

    elif SplitCommand[0] in ("y", "year"):
        days_in_year = 366 if (TimeTrack.Year % 4 == 0 and (TimeTrack.Year % 100 != 0 or TimeTrack.Year % 400 == 0)) else 365
        TimeTrack.Day += days_in_year
        mods.run_all("Time", days_in_year)
        Time(days_in_year)
        CalculateDay()
        print(f"You have {floor(people.ammount)} people")

    elif SplitCommand[0] == "save":
        DataSave()
    elif SplitCommand[0] == "load":
        if len(SplitCommand) > 1:
            path = f"save/{SplitCommand[1]}.{ext}"
            LoadData(path)
        else:
            LoadData(SaveNamePath)