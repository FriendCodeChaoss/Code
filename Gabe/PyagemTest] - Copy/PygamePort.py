import pygame
import random,math
from HelperScripts.Color import RandomGradient
from HelperScripts.Create_Shape import Line
from HelperScripts.ManageScene import *
from HelperScripts.Util import StartAll
import HelperScripts.screen as var

from pygame import mixer
mixer.init() 
if __name__ == "__main__":
    pygame.init()
def app():
    return

def main():
    StartAll()
   
    clock = pygame.time.Clock()
    running = True
    #Start(screen)
    size = (pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
    var.UpdateFrame = True
    var.GravObjects = [[['ball'],[25,1],.9,[55,55]]]
    while running:
        #var.UpdateFrame = True
        #Move(['sky', 'sun', 'background', 'tree','shop'],(1,1))
        Max = max(pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
        #Line(random.randint(1,Max),random.randint(1,Max),random.randint(1,Max),random.randint(1,Max),RandomGradient(20,50,"right"),10, render=True)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #end event/ close window if the X button is pressed
                running = False
            if event.type == pygame.WINDOWRESIZED:
                size = (pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
                var.UpdateFrame = True
        
        if var.UpdateFrame == True: #if need to add anything
            var.screen.fill('black')
            var.screen.blit(*Group(*var.Parts,width=size[0],height=size[1]+200))
            var.UpdateFrame = False
        #go to next frame
        pygame.display.flip()
        
        
        clock.tick(var.FPS)  # limit FPS

    pygame.quit()

if __name__ == "__main__":
    main()
    