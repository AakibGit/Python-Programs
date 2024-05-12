import pygame 

pygame.init()


x = 130
y = 100
h = 20
w = 20
t = 10

screen = pygame.display.set_mode((350,300))

pygame.display.set_caption("Moving object")

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x += t

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x -= t
        
            
    pygame.draw.rect(screen, "red", (x,y,h,w))
    pygame.display.update()
    
pygame.quit()
    
    