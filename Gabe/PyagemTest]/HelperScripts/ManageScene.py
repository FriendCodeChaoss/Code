import pygame
import math
from HelperScripts.Color import *
from HelperScripts.Create_Shape import Rect,Oval,Polygon

def Move(Parts,Name,pos):
    if isinstance(Name,list):
        for name in Name:
            Parts[0][Parts[1].index(name)][1].move_ip(pos)
    else:
        Parts[0][Parts[1].index(Name)][1].move_ip(pos)
    return Parts

def Group(*Draw, width=400, height=400, run=True):
    if not run:
        return None
    temp_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for call in Draw:
        IfSurf = call[0]
        Pos = call[1]

        if callable(IfSurf):
            surf = IfSurf()
            if isinstance(surf, pygame.Surface):
                temp_surface.blit(surf, Pos)

        elif isinstance(IfSurf, pygame.Surface):
            temp_surface.blit(IfSurf, Pos)

        elif isinstance(IfSurf, list):
            for surf in IfSurf:
                if isinstance(surf, pygame.Surface):
                    temp_surface.blit(surf, Pos)

    return [temp_surface, temp_surface.get_rect(topleft=(0, 0))]

def render(surface,x,y,screen):
    screen.blit(surface,(x,y))