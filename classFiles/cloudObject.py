import pygame, random
screenWidth,screenHeight = 1100,700
screen = pygame.display.set_mode((screenWidth,screenHeight))

class Clouds: #cloudClass.draw(x,y,l,w,image_index)
    def __init__(self,x,y,l,w,randomCloud):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.randomCloud = randomCloud

    def draw(self):
        self.cloudImage = pygame.image.load("images/sprites/"+ self.randomCloud).convert_alpha()
        self.cloudImage = pygame.transform.scale(self.cloudImage,(self.l,self.w))
        self.cloudDisplay = self.cloudImage.get_rect(midright = (self.x,self.y))
        screen.blit(self.cloudImage,self.cloudDisplay)
        self.x -= 0.5

        if(self.x < 0):
            clouds = ["cloud1.png","cloud2.png","cloud3.png"]
            self.x = screenWidth + random.randint(200,600)
            self.randomCloud = clouds[random.randint(0,len(clouds) - 1)]