import pygame
screenWidth, screenHeight = 1100,700
screen = pygame.display.set_mode((screenWidth,screenHeight))

class MenuButton:   
    def draw(self,sw1,sh1,constant,sw2,sh2,r,g,b,x,y,index,add = 0): #Audio Button
        iconImages = ["audioIcon.png","musicIcon.png"]
        self.selectedIcon = pygame.image.load("images/sprites/" + iconImages[index]).convert_alpha()
        self.selectedIcon = pygame.transform.scale(self.selectedIcon,(85,85))
        self.iconLogo = self.selectedIcon.get_rect(topleft = (x + add,y))
        self.blackBorder = pygame.Rect(screenWidth / sw1 + add, screenHeight / sh1,constant + 20,constant + 20)
        self.whiteBorder = pygame.Rect(screenWidth / sw2 + add, screenHeight / sh2,constant,constant)
        pygame.draw.rect(screen,(0,0,0),self.blackBorder)
        pygame.draw.rect(screen,(r,g,b),self.whiteBorder)
        screen.blit(self.selectedIcon,self.iconLogo)

    def play(self,color, y = 0, texty = 0,text = "Play",x = 0): #Play Button
        self.playFont = pygame.font.Font(None,70)
        self.play1 = pygame.Rect(screenWidth / 2.8,screenHeight / 2.8 + y,300,100)
        self.play2 = pygame.Surface((screenWidth / 4.25, screenHeight / 9))
        self.play2.fill(color)
        self.playText = self.playFont.render(text, False, "black")
        self.playRect = self.playText.get_rect(topleft = (490 + x,275 + texty))
        pygame.draw.rect(screen,(0,0,0),self.play1)
        screen.blit(self.play2,(413,260 + y))
        screen.blit(self.playText,self.playRect)