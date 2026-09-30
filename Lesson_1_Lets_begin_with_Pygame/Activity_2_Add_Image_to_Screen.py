import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500))

done = False

bg = pygame.transform.scale(
    pygame.image.load('https://codehs.com/uploads/eaf6f328569f4e6eef3dfae36767e85f').convert(),
    (500, 500))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    display_surface.blit(bg, (0, 0))
    pygame.display.flip()