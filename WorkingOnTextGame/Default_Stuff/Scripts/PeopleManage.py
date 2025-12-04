from Default_Stuff.Vars.people import people
from Default_Stuff.Vars.Jobs import Jobs
from math import floor

def CaculateBornDeath():
    subclasses = [cls for cls in Jobs.__dict__.values() if isinstance(cls, type)]
    born_values = [cls.BornAdd for cls in subclasses]
    death_values = [cls.DeathAdd for cls in subclasses]
    people.born = floor(sum(born_values) / len(born_values)*100)/100
    people.death = floor(sum(death_values) / len(death_values)*100)/100
    print(people.born, people.death)