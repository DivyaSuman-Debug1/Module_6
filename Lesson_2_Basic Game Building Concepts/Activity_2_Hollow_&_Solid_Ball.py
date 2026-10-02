import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
    pygame.draw.circle(screen, (0, 255, 0), (50, 150),50) #Put , 3 after 50 if you want hollow
    
    pygame.display.flip()