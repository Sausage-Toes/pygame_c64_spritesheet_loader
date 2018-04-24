import pygame
from Commodore_64_color_palettes import *
from Spritesheet import *

pygame.init()
#settings
screen_width = 640  
screen_height = 480

TITLE = "Nyan Cat"
BGCOLOR = CC_BLUE

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption(TITLE)

all_sprites_list = pygame.sprite.Group()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

spritesheet = Spritesheet("nyan_cat_c64.bmp",colorkey=(72,58,170),scale=8)

head = spritesheet.merge_images(spritesheet.load_animation(6,6)
                               ,spritesheet.load_animation(0,6))
tail = spritesheet.merge_images(spritesheet.load_animation(18,6)
                               ,spritesheet.load_animation(12,6))
body = spritesheet.merge_images(spritesheet.load_animation(24,1)
                               ,spritesheet.load_animation(25,1))

star = spritesheet.load_animation(26,6)


animation_index = 0
animation_max_index = 5
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            
    # Clear the screen
    screen.fill(BGCOLOR)
    
    # Draw all the spites
    all_sprites_list.draw(screen)
    
    screen.blit(star[animation_index], ((0,0)))
    screen.blit(star[animation_index], ((340,280)))
    
    pygame.draw.rect(screen, CC_RED,  [0, 80, 220,20])
    pygame.draw.rect(screen, CC_ORANGE,  [0, 100, 220,20])
    pygame.draw.rect(screen, CC_YELLOW,  [0, 120, 220,20])
    pygame.draw.rect(screen, CC_GREEN,  [0, 140, 220,20])
    pygame.draw.rect(screen, CC_LIGHTBLUE,  [0, 160, 220,20])
    pygame.draw.rect(screen, CC_VIOLET,  [0, 180, 220,20])

    
    screen.blit(tail[animation_index], ((152,127)))
    screen.blit(body[0], ((200,80)))    
    screen.blit(head[animation_index], ((305,110)))

    animation_index = animation_index +1
    
    if animation_index > animation_max_index:
        animation_index = 0


    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(8)

pygame.quit()
