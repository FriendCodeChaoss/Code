import pygame
import math
from HelperScripts.screen import screen
import HelperScripts.screen as var

def upscale(v):
    return max(1, int(v * var.detail))

def downscale(surf, w, h):
    return pygame.transform.smoothscale(surf, (w, h))

def Rect(X, Y, width, height, fill=(0,0,0), border=None, borderWidth=2,
     opacity=255, rotateAngle=0, align='left-top',
     Screen = screen,render = False):
    
    #Create rectangle/frame
    UW = upscale(width)
    UH = upscale(height)
    UBW = upscale(borderWidth)

    if border == None:
        TempSurf = pygame.Surface((UW, UH), pygame.SRCALPHA)
        #set graident texture size
        if fill[0] == "gradient":
            TempSurf.blit(pygame.transform.smoothscale(fill[1], (UW, UH)), (0, 0))
        else:
            TempSurf.fill(pygame.Color(fill[0],fill[1],fill[2],255))
    else:
        #make the frame + border size
        TempSurf = pygame.Surface((UW+(UBW*2), UH+(UBW*2)), pygame.SRCALPHA)
        
        # Draw the border first
        if isinstance(border, list) and border[0] == "gradient":
            TempSurf.blit(pygame.transform.smoothscale(border[1], (UW+(UBW*2), UH+(UBW*2))), (0,0))
        else:
            pygame.draw.rect(TempSurf, border, pygame.Rect(0, 0, UW+(UBW*2), UH+(UBW*2)))

        # Draw the inner fill
        if fill[0] == "gradient":
            TempSurf.blit(pygame.transform.smoothscale(fill[1], (UW, UH)), (UBW, UBW))
        else:
            Box = pygame.Surface((UW, UH), pygame.SRCALPHA)
            Box.fill((fill[0],fill[1],fill[2]))
            TempSurf.blit(Box,(UBW, UBW))
    
    #set transparency
    TempSurf.set_alpha(opacity)
    #then rotate image
    TempSurf = pygame.transform.rotate(TempSurf, rotateAngle)

    Final = downscale(TempSurf, width, height)
    RotatedRect = Final.get_rect(topleft=(X, Y))

    #add to canvis
    if render == True:
        Screen.blit(Final, RotatedRect)
    else:
        return (Final,RotatedRect)

def Oval(X, Y, width, height, fill=(0,0,0), border=None,
     borderWidth=2, opacity=255, rotateAngle=0,
     Screen = screen, render = False):
    
    UW = upscale(width)
    UH = upscale(height)
    UBW = upscale(borderWidth)

    TempSurf = pygame.Surface((UW + UBW*2, UH + UBW*2), pygame.SRCALPHA)

    if border:
        if border[0] == "gradient":
            TempSurf.blit(pygame.transform.smoothscale(border[1], (UW + UBW*2, UH + UBW*2)), (0,0))
        else:
            pygame.draw.ellipse(TempSurf, border, pygame.Rect(0,0,UW + UBW*2, UH + UBW*2))
    
    if fill[0] == "gradient":
        scaled_fill = pygame.transform.smoothscale(fill[1], (UW, UH))
        mask = pygame.Surface((UW, UH), pygame.SRCALPHA)
        pygame.draw.ellipse(mask, (255,255,255), pygame.Rect(0,0,UW, UH))
        scaled_fill.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        TempSurf.blit(scaled_fill, (UBW, UBW))
    else:
        pygame.draw.ellipse(TempSurf, fill, pygame.Rect(UBW, UBW, UW, UH))

    #transparency
    TempSurf.set_alpha(opacity)
    #rotate
    TempSurf = pygame.transform.rotate(TempSurf, rotateAngle)

    Final = downscale(TempSurf, width, height)
    RotatedRect = Final.get_rect(topleft=(X-(width/2), Y-(height/2)))

    #display
    if render == True:
        Screen.blit(Final, RotatedRect)
    else:
        return(Final, RotatedRect)

def Circle(X, Y, radius, fill=(0,0,0), border=None,
       borderWidth=2, opacity=100, rotateAngle=0,
       Screen = screen, render = False):
    return Oval(X,Y,radius,radius,fill,border,borderWidth,opacity,rotateAngle, Screen=Screen, render=render)

def Line(x1, y1, x2, y2, fill=(0,0,0), lineWidth=2, opacity=255, Screen = screen, render = False):
    
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)

    UL = upscale(length)
    ULW = upscale(lineWidth)

    TempSurf = pygame.Surface((UL, ULW), pygame.SRCALPHA)

    # Check if fill is a gradient
    if isinstance(fill, list) and fill[0] == "gradient":
        TempSurf.blit(pygame.transform.smoothscale(fill[1], (UL, ULW)), (0, 0))
    else:
        TempSurf.fill((fill[0], fill[1], fill[2]))

    angle = -math.degrees(math.atan2(dy, dx))
    TempSurf = pygame.transform.rotate(TempSurf, angle)

    Final = pygame.transform.smoothscale(
        TempSurf,
        (int(TempSurf.get_width()/var.detail), int(TempSurf.get_height()/var.detail))
    )

    rect = Final.get_rect(center=((x1 + x2)/2, (y1 + y2)/2))
    Final.set_alpha(opacity)

    if render == True:
        Screen.blit(Final, rect)
    else:
        return [Final, rect.topleft]

def Label(text,
          x,
          y,
          size=24,
          fill=(255, 255, 255),
          font=None,
          Screen = screen,):
    
    global screen
    if Screen is None:
        Screen = screen

    if font is None:
        font = pygame.font.SysFont(None, size)

    pos = (x, y)

    text_surface = font.render(text, True, (255, 255, 255))
    text_w, text_h = text_surface.get_size()

    mask_surface = pygame.Surface((text_w, text_h), pygame.SRCALPHA)
    mask_surface.blit(text_surface, (0, 0))

    is_gradient = isinstance(fill, dict) and fill.get("gradient")

    if not is_gradient:
        colored = font.render(text, True, fill)
        Screen.blit(colored, pos)
        return

    grad_info = fill

    final_surf = pygame.Surface((text_w, text_h), pygame.SRCALPHA)
    final_surf.blit(fill, (0, 0))
    final_surf.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    Screen.blit(final_surf, pos)

def Polygon(*args,
            fill=(0,0,0),
            border=None,
            borderWidth=2,
            opacity=255,
            rotateAngle=0,
            Screen = screen,render = False):

    pts = [a for a in args if isinstance(a, (int, float))]
    if len(pts) % 2 != 0 or len(pts) < 6:
        return

    pointList = [(pts[i], pts[i+1]) for i in range(0, len(pts), 2)]

    xs = [p[0] for p in pointList]
    ys = [p[1] for p in pointList]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    w = max(maxx - minx, 1)
    h = max(maxy - miny, 1)

    UW = upscale(w)
    UH = upscale(h)
    UBW = upscale(borderWidth)

    TempSurf = pygame.Surface((UW+UBW*2, UH+UBW*2), pygame.SRCALPHA)
    shifted = [((x-minx)*var.detail + UBW, (y-miny)*var.detail + UBW) for (x,y) in pointList]

    if isinstance(fill, list) and fill[0] == "gradient":
        grad_surf = pygame.transform.smoothscale(fill[1], (UW, UH))
        mask = pygame.Surface((UW, UH), pygame.SRCALPHA)
        pygame.draw.polygon(mask, (255,255,255), [(x-UBW, y-UBW) for (x,y) in shifted])
        grad_surf.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        TempSurf.blit(grad_surf, (UBW, UBW))
    else:
        pygame.draw.polygon(TempSurf, fill, shifted)

    if border is not None:
        pygame.draw.polygon(TempSurf, border, shifted, UBW)

    TempSurf.set_alpha(opacity)

    if rotateAngle != 0:
        TempSurf = pygame.transform.rotate(TempSurf, rotateAngle)

    Final = downscale(TempSurf, w, h)
    rect = Final.get_rect(topleft=(minx, miny))

    if render == True:
        Screen.blit(Final, rect)
    else:
        return(Final,rect)
