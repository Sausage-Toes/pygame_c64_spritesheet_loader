# sheet is 192 w x 672 h pixels / 8x32 sprites
# c64 sprites are 24 w x 21 h
import pygame
class Spritesheet:
    def __init__(self, filename
                 , sprite_height=21
                 , sprite_width=24
                 , sprites_per_row=8
                 , colorkey=(0,0,0)
                 , scale=1):
        self.spritesheet = pygame.image.load(filename).convert()
        self.sprite_height = sprite_height
        self.sprite_width = sprite_width
        self.sprites_per_row = sprites_per_row
        self.colorkey = colorkey
        self.scale = scale

    def get_image(self, x,y, width, height):
        image = pygame.Surface((width,height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        image = pygame.transform.scale(image
                                       , (width*self.scale
                                       , height*self.scale))
        return image

    def load_animation (self, start_index, length):
        image_array=[]
        for x in range(start_index, start_index+length):
            img = self.get_image(self.sprite_width*(x%self.sprites_per_row)
                                ,(x//self.sprites_per_row)*self.sprite_height
                                ,self.sprite_width
                                ,self.sprite_height)
            img.set_colorkey(self.colorkey)
            image_array.append(img)
        return image_array;

    def merge_images (self, img_list1, img_list2):
        merged=[]
        n = len(img_list1)
        for i in range(0,n):
            #merged.append(img_list1[i].blit(img_list2[i],(0,0)))
            img_list1[i].blit(img_list2[i],(0,0))
            merged.append(img_list1[i])
        return merged;
