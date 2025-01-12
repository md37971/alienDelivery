import pygame
screenWidth,screenHeight = 1100,700
screen = pygame.display.set_mode((screenWidth,screenHeight))

class PropImage: #propClass.draw(x,y,l,w,image_index)
    def __init__(self,x,y,l,w,imageIndex = 0):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.imageIndex = imageIndex

    def draw(self): #Other Props
        imageArray = ["customer","castle","introUFO"]
        self.imageProp = pygame.image.load("sprites/" + imageArray[self.imageIndex] + ".png").convert_alpha()
        self.imageProp = pygame.transform.scale(self.imageProp,(self.l,self.w))
        self.imageDisplay = self.imageProp.get_rect(topleft = (self.x,self.y))
        screen.blit(self.imageProp,self.imageDisplay)

    def deathSprite(self,audioFix,audioVolume): #Explosion Prop
        self.sound = pygame.mixer.Sound("audio/explosion.mp3")
        self.sound.set_volume(audioVolume)
        self.image = pygame.image.load("sprites/explosion.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.l,self.w))
        self.death = self.image.get_rect(center = (self.x, self.y))

        if(audioFix < 2):
            screen.blit(self.image,self.death)
            self.sound.play()