import pygame
import math
from HelperScripts.Color import *
import HelperScripts.screen as var
from HelperScripts.Util import GetPos,GetSize
import threading
import time
import HelperScripts.screen as var
clock =  pygame.time.Clock()

#manage objects
# region Manageing objects

def AddObject(*args): #input object then name so [rect(args), "rectangle"]
    for i in args:
        var.Parts[0].append(i[0])
        var.Parts[1].append(i[1])
    var.UpdateFrame = True

def DeleteObject(*args):
    for i in args:
        Del = var.Parts[1].index(i)
        #list.remove(Var) deletes the item that is called Var from list
        #list.pop(numb) removes the list[numb] from the list and if no number givven removes the last value
        var.Parts[0].pop(Del)
        var.Parts[1].pop(Del)

def Group(*Draw, width=600, height=600):

    temp_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for item in Draw:
        if isinstance(item, tuple) and len(item) == 2:
            surf, rect = item
            temp_surface.blit(surf, rect)
        elif isinstance(item, list):
            for sub in item:
                if isinstance(sub, tuple) and len(sub) == 2:
                    temp_surface.blit(sub[0], sub[1])

    return temp_surface, temp_surface.get_rect(topleft=(0,0))

#movement
def Move(Name,pos):
    #print(Name,pos)
    var.UpdateFrame = True
    if isinstance(Name,list):
        for name in Name:
            var.Parts[0][var.Parts[1].index(name)][1].move_ip(pos)
    else:
        var.Parts[0][var.Parts[1].index(Name)][1].move_ip(pos)

#untested
def MoveToTime(Name, pos, duration=None):
    var.UpdateFrame = True
    def MoveToPos_thread(name_list, offset, duration):
        if not isinstance(name_list, list):
            name_list_local = [name_list]
        else:
            name_list_local = name_list

        dx, dy = offset

        # Instant movement if duration is None
        if not duration or duration <= 0:
            for name in name_list_local:
                idx = var.Parts[1].index(name)
                var.Parts[0][idx][1].move_ip(offset)
            return

        steps = max(int(duration * var.FPS), 1)
        step_dx = dx / steps
        step_dy = dy / steps
        step_time = 1 / var.FPS

        for _ in range(steps):
            for name in name_list_local:
                idx = var.Parts[1].index(name)
                var.Parts[0][idx][1].move_ip((step_dx, step_dy))
            time.sleep(step_time)

        # Ensure final position is exact
        for name in name_list_local:
            idx = var.Parts[1].index(name)
            var.Parts[0][idx][1].move_ip((dx - step_dx*steps, dy - step_dy*steps))
    
    t = threading.Thread(target=MoveToPos_thread, args=(Name, pos, duration))
    t.start()
# endregion

# region Sound

def AddSound(*args): #input object then name so [rect(args), "rectangle"]
    for i in args:
        var.Sounds[0].append(i[0])
        var.Sounds[1].append(i[1])
    var.UpdateFrame = True

def DeleteSound(*args):
    for i in args:
        Del = var.Sounds[1].index(i)
        #list.remove(Var) deletes the item that is called Var from list
        #list.pop(numb) removes the list[numb] from the list and if no number givven removes the last value
        var.Sounds[0].pop(Del)
        var.Sounds[1].pop(Del)



# endregion

# region working on
def grav():
    while True:
        for Object in var.GravObjects:
            size = (pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
            OffsetX = -200
            OffsetY = -200
            PaSizeX = Object[3][0]
            PaSizeY = Object[3][1]
            Object[1][1] += .3
            pos = GetPos(Object[0])
            if pos[0] >= size[0]+OffsetX-PaSizeX:
                Object[1][0] = -abs(Object[1][0])

            if pos[0] <= 0+OffsetX+PaSizeX:
                Object[1][0] = abs(Object[1][0])
            if pos[1] >= size [1]+OffsetY-PaSizeY:
                Object[1][1] = -abs(Object[1][1])
                Object[1][1] =+ (Object[1][1]*Object[2])
                if Object[1][1] >= 1:
                    Object[1][1] = 0
            if pos[1] <= 0+OffsetY+PaSizeY:
                Object[1][1] = abs(Object[1][1])

            
            Move(Object[0],Object[1])
        clock.tick(80)
    
def ObjectGravity(Object,Bounce):
    a=a
# endregion
