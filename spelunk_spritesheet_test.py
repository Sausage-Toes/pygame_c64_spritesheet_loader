import pygame
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False

# Set the height and width of the screen
#scale = 1
#screen_width = 320
#screen_height = 240

scale = 2
screen_width = 640
screen_height = 480
scale = 8

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Spelunk Spritesheet Animation Test')

class Spritesheet:
    def __init__(self,filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x,y, width, height):
        image = pygame.Surface((width,height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        return image

# sheet is 192 w x 672 h pixels / 8x32 sprites
# c64 sprites are 24 w x 21 h
sprite_width = 24
sprite_height = 21
sprites_per_row = 8
spritesheet = Spritesheet("spelunk7.bmp")

def load_animation (start_index, length):
    image_array=[]
    for x in range(start_index, start_index+length):
        img = spritesheet.get_image(sprite_width*(x%sprites_per_row)
                                    ,(x//sprites_per_row)*sprite_height
                                    ,sprite_width
                                    ,sprite_height)
        img.set_colorkey((0,0,0))
        image_array.append(img)
    return image_array;

def merge_images (img_list1, img_list2):
    merged=[]
    n = len(img_list1)
    for i in range(0,n):
        #merged.append(img_list1[i].blit(img_list2[i],(0,0)))
        img_list1[i].blit(img_list2[i],(0,0))
        merged.append(img_list1[i])
    return merged;

#load player sprite animations
walk_left = merge_images(load_animation(14,7),load_animation(21,7))
walk_right = merge_images(load_animation(0,7),load_animation(7,7))
idle = merge_images(load_animation(28,4),load_animation(32,4))
crouch_right = merge_images(load_animation(36,1),load_animation(37,1))
crouch_left = merge_images(load_animation(38,1),load_animation(39,1))
idle_left = []
for i in range(0,len(idle)):
    img =  pygame.transform.flip(idle[i],True,False)
    idle_left.append(img)
idle_right = idle

animation_index = 0
animation_max_index = 3
player_x = (screen_width/2) - ((sprite_width/2) * scale)
player_y = (screen_height/2) - ((sprite_height/2) * scale)

player_move = "idle"
player_look = "right"
prev_player_move = player_move


joysticks = []
# for all the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print ("Detected joystick '",joysticks[-1].get_name(),"'")

joy_x = 0
joy_y = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player_move = "left"
            player_look = "left"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player_move = "right"
            player_look = "right"
        elif event.type == pygame.KEYUP and (
                event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
            player_move = "idle"
        elif event.type == pygame.JOYAXISMOTION:
            joy_x = round(joysticks[event.joy].get_axis(0))
            joy_y = round(joysticks[event.joy].get_axis(1))    
            print ("x:",joy_x," y:",joy_y)
            if joy_x != 0:
                if joy_x < 0:
                    player_move = "left"
                    player_look = "left"
                else:
                    player_move = "right"
                    player_look = "right"
            elif joy_y >  0:
                player_move = "crouch"
            else:
                player_move = "idle"
                
    # Clear the screen
    screen.fill(WHITE)
        
    if player_move != prev_player_move:
        animation_index = 0
        prev_player_move = player_move
    
    if player_move == "idle":
        if player_look == "right":
            screen.blit(idle_right[animation_index], ((player_x,player_y)))
        else:
            screen.blit(idle_left[animation_index], ((player_x,player_y)))
        animation_max_index = 3
    elif player_move == "left":
        screen.blit(walk_left[animation_index], ((player_x,player_y)))
        animation_max_index = 6
    elif player_move == "right":
        screen.blit(walk_right[animation_index], ((player_x,player_y)))
        animation_max_index = 6
    elif player_move == "crouch":
        if player_look == "right":
            screen.blit(crouch_right[animation_index], ((player_x,player_y)))
        else:
            screen.blit(crouch_left[animation_index], ((player_x,player_y)))
        animation_max_index = 0    
    else:
        pass

    animation_index = animation_index +1
    
    if animation_index > animation_max_index:
        animation_index = 0
               
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(8)
    #clock.tick(60)
    
pygame.quit()
