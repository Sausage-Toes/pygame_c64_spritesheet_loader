import pygame
from Commodore_64_color_palettes import *
from Spritesheet import *


#settings
screen_width = 640
screen_height = 480
sprite_height=42
sprite_width=24
scale = 8
TITLE = "Walk Cycle"
BGCOLOR = CC_BLUE

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption(TITLE)

spritesheet = Spritesheet("walk_cycle_8_frame.bmp"
                          , sprite_height=sprite_height
                          , sprite_width=sprite_width
                          , colorkey=(255,255,255)
                          , scale=8)

animation_frames = spritesheet.load_animation(0,8)


animation_index = 0
animation_max_index = 5

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            
    # Clear the screen
    screen.fill(BGCOLOR)

    x = (screen_width // 2) - (sprite_width * scale // 2)
    y  = (screen_height // 2) - ( sprite_height * scale // 2)

    screen.blit(animation_frames[animation_index], ((x,y)))




    animation_index = animation_index +1
    
    if animation_index > animation_max_index:
        animation_index = 0


    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(8)

pygame.quit()
