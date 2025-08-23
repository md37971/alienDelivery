import pygame, random
pygame.init()
from classFiles.cloudObject import Clouds
from classFiles.propObject import PropImage
from classFiles.buttonObject import MenuButton

#Display Functions
def scoreboard(t,x = 0,x2 = 0,textY = 0,iconPos = 0,index = 0,resize = 0,resize2 = 0):
    iconArray = ["ufoplayer","timer","coin"]
    iconImage = pygame.image.load("images/sprites/" + iconArray[index] + ".png")
    iconImage = pygame.transform.scale(iconImage,(50 + resize,50 + resize2))
    iconDisplay = iconImage.get_rect(topleft = (iconPos + 125,52.5))
    blackbox = pygame.Surface((screenWidth / 5,screenHeight/8))
    whitebox = pygame.Surface((screenWidth / 6.5, screenHeight / 12.5))
    whitebox.fill("white")
    screen.blit(blackbox,(screenWidth / 3.15 + x,screenHeight / 13.5 - 20))
    screen.blit(whitebox,(screenWidth / 2.95 + x,screenHeight / 10 - 20))
    scoreSurface = uiFont.render( "x "+ str(int(t)), False,"black")
    scoreSurfaceRect = scoreSurface.get_rect(topleft = (screenWidth / 2.1525 + x2,screenHeight / 8.25 - 30 + textY)) #topleft
    screen.blit(scoreSurface,scoreSurfaceRect)
    screen.blit(iconImage,iconDisplay)

def gameOverScreen(bigmsg,textsw1,textsh1,keybind,textsw2,textsh2,bSurfaceW = 1.5, bSurfaceH = 5, wSurfaceW = 1.65, wSurfaceH = 6.5, bBlitw = 6.25, bBlith = 2.8, wBlitw = 5.2, wBlitH = 2.65):
    blackbox = pygame.Surface((screenWidth / bSurfaceW, screenHeight / bSurfaceH))
    whitebox = pygame.Surface((screenWidth / wSurfaceW, screenHeight / wSurfaceH))
    whitebox.fill("white")
    screen.blit(blackbox,(screenWidth/bBlitw,screenHeight/bBlith))
    screen.blit(whitebox,(screenWidth/wBlitw,screenHeight/wBlitH))
    gameOverText = scoreFont.render(bigmsg, False, "black")
    gameOverRect = gameOverText.get_rect(topleft = (screenWidth / textsw1,screenHeight / textsh1))
    restartText = restartFont.render(keybind, False, "black")
    restartTextRect = restartText.get_rect(topleft = (screenWidth / textsw2, screenWidth / textsh2))
    screen.blit(gameOverText,gameOverRect)
    screen.blit(restartText,restartTextRect)

def restartGame():
    global gameActive, playerXpos, playerYpos, level, timer, respawndelay, transitiondelay, finished, lives, audioFix, coinCount, coinStorage, coinLife
    gameActive = True
    playerXpos = 180
    playerYpos = 325
    print("Game Restarted")
    level = 1
    player.x = playerXpos
    player.y = playerYpos
    timer = timeLimit
    coinCount = 0
    coinLife = 15
    respawndelay = 0
    transitiondelay = 0
    lives = 5 - 1
    audioFix = 0
    finished = False
    coinStorage = [[True for x in range(col)] for x in range(row)]
    pygame.mixer.music.play(-1)

#levels
def level1Data():
    finishClass.draw(895,160,2,0,190) #LAST TWO PARAMETERS ARE NEXT LEVEL SPAWN CORDS
    coinClass.draw(260,145,0,0)
    coinClass.draw(250,530,0,1)
    coinClass.draw(915,350,0,2)
    coinClass.draw(590,445,0,3)
    coinClass.draw(900,670,0,4)
    solidClass.draw(510,0,100,250)
    solidClass.draw(475,165,165,100)
    solidClass.draw(128,175,225,90)
    solidClass.draw(80,385,300,35)
    solidClass.draw(125,420,200,35,2)
    solidClass.draw(170,455,100,35,2)
    solidClass.draw(120,565,205,105)
    solidClass.draw(775,190,225,80)
    solidClass.draw(755,380,260,35)
    solidClass.draw(805,415,160,35,2)
    solidClass.draw(832,450,105,35,2)
    solidClass.draw(465,475,195,35)
    solidClass.draw(487,510,150,35,2)
    solidClass.draw(500,545,125,35,2)
    solidClass.draw(800,590,45,140,2)
    solidClass.draw(800,590,120,35)
    enemyClass.draw(475,265,25,65,2)
    enemyClass.draw(350,200,125,25,6)
    enemyClass.draw(470,430,25,45,1)
    enemyClass.draw(395,600,75,75,5)
    enemyClass.draw(675,300,45,45,5)
    enemyClass.draw(1025,590,75,35,4)

def level2Data():
    finishClass.draw(925,575,3,1000,160)
    coinClass.draw(215,500,1,0)
    coinClass.draw(415,200,1,1)
    coinClass.draw(983,155,1,2)
    coinClass.draw(750,95,1,3)
    coinClass.draw(588,560,1,4)
    solidClass.draw(0,250,100,450,1)
    solidClass.draw(265,0,75,500,1)
    solidClass.draw(340,35,150,50)
    solidClass.draw(435,90,50,60)
    solidClass.draw(340,250,150,50)
    solidClass.draw(435,375,85,85)
    solidClass.draw(530,590,60,115,1)
    solidClass.draw(590,500,90,200,1)
    solidClass.draw(630,200,180,30)
    solidClass.draw(650,230,140,30,2)
    solidClass.draw(670,260,100,30,2)
    solidClass.draw(850,360,250,100)
    solidClass.draw(870,0,60,190)
    solidClass.draw(870,190,130,50)
    enemyClass.draw(205,150,60,60,4)
    enemyClass.draw(195,380,70,50,4)
    enemyClass.draw(100,575,60,50,3)
    enemyClass.draw(325,570,60,80,6)
    enemyClass.draw(650,375,60,60,5)
    enemyClass.draw(690,160,60,40,6)
    enemyClass.draw(1000,40,60,60,5)
    enemyClass.draw(830,490,40,40,5)
    enemyClass.draw(985,490,40,40,5)
    enemyClass.draw(830,620,40,40,5)
    enemyClass.draw(985,620,40,40,5)
    enemyClass.draw(880,310,40,50,6)
    
def level3Data():
    finishClass.draw(50,50,4,0,0)
    coinClass.draw(410,550,2,0)
    coinClass.draw(80,230,2,1)
    coinClass.draw(400,150,2,2)
    coinClass.draw(750,158,2,3)
    coinClass.draw(220,530,2,4)
    teleportClass.draw(1020,250,1000,575,3,4,1,3)
    teleportClass.draw(340,330,200,650,3,1,1)
    teleportClass.draw(0,650,175,360,4,1,0,3)
    solidClass.draw(870,0,50,200)
    solidClass.draw(760,0,110,120)
    solidClass.draw(865,300,245,125)
    solidClass.draw(475,200,190,35)
    solidClass.draw(505,235,135,35,2)
    solidClass.draw(525,270,100,60,2)
    solidClass.draw(865,625,250,80)
    solidClass.draw(865,625,250,80)
    solidClass.draw(665,465,75,250,1)
    solidClass.draw(250,0,75,700,1)
    solidClass.draw(250,380,200,90)
    solidClass.draw(450,380,50,220,1)
    solidClass.draw(0,80,120,60)
    solidClass.draw(130,210,120,60)
    solidClass.draw(150,410,100,60)
    solidClass.draw(90,350,60,120)
    enemyClass.draw(625,300,240,20,6)
    enemyClass.draw(865,425,50,100,6)
    enemyClass.draw(550,0,50,200,6)
    enemyClass.draw(500,400,60,60,3)
    enemyClass.draw(0,580,250,30,6)

def level4Data():
    finishClass.draw(573,355,5,700,600)
    coinClass.draw(110,260,3,0)
    coinClass.draw(620,150,3,1)
    coinClass.draw(550,650,3,2)
    coinClass.draw(830,620,3,3)
    coinClass.draw(920,260,3,4)
    teleportClass.draw(470,450,620,450,1,3,1,3)
    teleportClass.draw(205,250,440,540,2,1,1,2)
    teleportClass.draw(540,540,710,350,4,2,0,3)
    teleportClass.draw(816,100,460,225,2,3,1,2)
    solidClass.draw(90,150,190,30)
    solidClass.draw(160,150,45,160,1)
    solidClass.draw(50,300,260,60)
    solidClass.draw(0,550,180,160)
    solidClass.draw(360,500,80,200)
    solidClass.draw(440,500,230,40)
    solidClass.draw(620,500,80,200)
    solidClass.draw(520,425,100,75,2)
    solidClass.draw(420,385,220,45)
    solidClass.draw(420,195,40,190,2)
    solidClass.draw(420,180,220,45)
    solidClass.draw(600,225,40,160,2)
    solidClass.draw(670,150,40,250,1)
    solidClass.draw(950,150,40,250,1)
    solidClass.draw(710,150,240,30)
    solidClass.draw(670,400,320,30)
    solidClass.draw(850,300,100,100)
    solidClass.draw(700,500,150,45)
    solidClass.draw(770,650,75,65)
    solidClass.draw(1030,500,70,200,1)
    solidClass.draw(500,0,70,180,1)
    enemyClass.draw(230,360,60,90,2)
    enemyClass.draw(340,25,60,60,5)
    enemyClass.draw(280,560,80,60,4)
    enemyClass.draw(970,560,60,40,4)

def level5Data():
    finishClass.draw(1050,65,6,0,125)
    coinClass.draw(145,540,4,0)
    coinClass.draw(240,135,4,1)
    coinClass.draw(700,200,4,2)
    coinClass.draw(375,660,4,3)
    coinClass.draw(940,660,4,4)
    teleportClass.draw(650,330,0,370,4,3,1,3)
    teleportClass.draw(390,295,0,650,4,3,1)
    teleportClass.draw(200,650,1050,650,4,4)
    teleportClass.draw(200,650,1050,650,4,4)
    teleportClass.draw(775,370,775,120,1,4,1,3)
    solidClass.draw(250,350,75,350)
    solidClass.draw(85,570,65,170)
    solidClass.draw(0,420,260,60)
    solidClass.draw(185,260,65,160,2)
    solidClass.draw(140,225,155,35,2)
    solidClass.draw(115,195,205,35,2)
    solidClass.draw(90,165,255,35)
    solidClass.draw(250,345,250,75)
    solidClass.draw(460,170,75,250)
    solidClass.draw(535,230,170,75)
    solidClass.draw(700,170,400,75)
    solidClass.draw(950,95,250,75)
    solidClass.draw(700,0,75,420,1)
    solidClass.draw(700,420,100,60)
    solidClass.draw(800,420,75,280)
    solidClass.draw(965,420,50,280)
    solidClass.draw(615,570,75,200)
    solidClass.draw(410,550,150,150)
    enemyClass.draw(440,0,75,50,2)
    enemyClass.draw(650,380,50,100,2)
    enemyClass.draw(450,420,50,75,2)
    enemyClass.draw(965,245,50,50,2)
    enemyClass.draw(965,375,50,50,1)
    enemyClass.draw(865,350,10,70,6)

def level6Data():
    finishClass.draw(1050,65,7,0,510)
    coinClass.draw(50,600,5,0)
    coinClass.draw(445,650,5,1)
    coinClass.draw(635,150,5,2)
    coinClass.draw(815,140,5,3)
    coinClass.draw(1075,650,5,4)
    teleportClass.draw(403,490,360,0,2,3,1)
    solidClass.draw(0,200,120,100)
    solidClass.draw(0,400,120,100)
    solidClass.draw(215,550,70,220,1)
    solidClass.draw(290,0,75,320,1)
    solidClass.draw(290,310,240,110)
    solidClass.draw(455,420,75,285,2)
    solidClass.draw(395,540,60,50)
    solidClass.draw(480,0,75,220,1)
    solidClass.draw(620,415,150,150)
    solidClass.draw(660,0,75,320,1)
    solidClass.draw(735,175,125,75)
    solidClass.draw(870,340,100,150)
    solidClass.draw(800,600,160,100)
    solidClass.draw(960,300,50,400,1)
    solidClass.draw(950,95,150,100)
    enemyClass.draw(85,500,35,130,2)
    enemyClass.draw(460,150,20,70,6)
    enemyClass.draw(655,565,70,140,6)
    enemyClass.draw(365,295,165,15,6)
    enemyClass.draw(620,410,150,15,6)
    enemyClass.draw(250,0,40,420,6)

def level7Data():
    finishClass.draw(1075,600,8,60,420)
    coinClass.draw(180,310,6,0)
    coinClass.draw(440,330,6,1)
    coinClass.draw(480,150,6,2)
    coinClass.draw(770,680,6,3)
    coinClass.draw(970,675,6,4)
    solidClass.draw(0,550,200,250)
    solidClass.draw(200,630,150,70)
    solidClass.draw(110,340,60,210)
    solidClass.draw(110,340,140,35)
    solidClass.draw(210,215,40,125)
    solidClass.draw(150,0,110,125)
    solidClass.draw(380,0,50,250,1)
    solidClass.draw(350,250,135,40)
    solidClass.draw(350,375,135,70)
    solidClass.draw(380,445,75,120)
    solidClass.draw(600,400,95,300)
    solidClass.draw(645,230,50,170,2)
    solidClass.draw(590,210,105,40)
    solidClass.draw(785,0,70,220)
    solidClass.draw(830,370,65,330)
    solidClass.draw(895,430,100,55)
    solidClass.draw(950,130,45,320,1)
    solidClass.draw(980,580,45,140)
    solidClass.draw(1025,630,80,70)
    enemyClass.draw(110,215,100,65,6)
    enemyClass.draw(350,360,135,15,6)
    enemyClass.draw(350,290,135,15,6)
    enemyClass.draw(260,440,120,50,4)
    enemyClass.draw(350,110,30,140,1)
    enemyClass.draw(430,175,55,75,1)
    enemyClass.draw(575,250,70,150,6)
    enemyClass.draw(635,0,70,100,2)
    enemyClass.draw(550,600,50,100,1)
    enemyClass.draw(790,575,40,35,4)
    enemyClass.draw(695,470,40,35,3)
    enemyClass.draw(855,0,250,50,6)
    enemyClass.draw(995,210,15,35,6)
    enemyClass.draw(1085,330,15,35,6)
    enemyClass.draw(995,435,15,35,6)
    enemyClass.draw(895,485,100,25,6)

def level8Data():
    PropImage(700,300,200,100,1).draw()
    finishClass.draw(800,370,9,430,580)
    coinClass.draw(50,120,7,0)
    coinClass.draw(580,135,7,1)
    coinClass.draw(500,660,7,2)
    coinClass.draw(1050,110,7,3)
    coinClass.draw(1080,650,7,4)
    solidClass.draw(0,470,150,100)
    solidClass.draw(250,0,100,230,1)
    solidClass.draw(300,400,120,350,1)
    solidClass.draw(470,160,200,100)
    solidClass.draw(530,259,80,100,2)
    solidClass.draw(920,150,200,100)
    solidClass.draw(640,600,360,100)
    solidClass.draw(900,450,100,150)
    solidClass.draw(700,400,200,200)
    enemyClass.draw(0,170,100,60,3)
    enemyClass.draw(530,359,80,341,6)
    enemyClass.draw(455,160,15,100,6)
    
def level9Data():
    blackbox = pygame.Surface((70,400))
    screen.blit(blackbox,(0,300))
    screen.blit(blackbox,(1030,300))
    finishClass.draw(1050,250,10,0,350)
    teleportClass.draw(530,535,105,650,4,3,1,3)
    teleportClass.draw(860,650,0,230,1,4,1,3)
    solidClass.draw(70,310,35,390,3)
    solidClass.draw(1000,310,35,390,3)
    solidClass.draw(70,310,930,35,3)
    solidClass.draw(380,500,320,35,3)
    solidClass.draw(380,500,35,200,3)
    solidClass.draw(700,500,35,200,3)
    solidClass.draw(0,118,1100,30,3)
    solidClass.draw(0,280,1100,35,3)
    solidClass.draw(190,500,80,100,4)
    solidClass.draw(420,370,75,75,4)
    solidClass.draw(620,425,75,75,4)
    solidClass.draw(840,345,80,100,4)
    solidClass.draw(735,630,75,75,3)
    enemyClass.draw(260,400,25,25,5)
    enemyClass.draw(800,530,25,25,5)
    enemyClass.draw(200,660,25,25,5)
    enemyClass.draw(950,660,25,25,5)
    enemyClass.draw(800,400,25,25,5)
    enemyClass.draw(150,148,100,60,6)
    enemyClass.draw(350,220,100,60,6)
    enemyClass.draw(550,148,100,60,6)
    enemyClass.draw(750,210,225,70,6)

def level10Data():
    finishClass.draw(1030,325,11,75,630)
    coinClass.draw(325,430,9,0)
    coinClass.draw(405,640,9,1)
    coinClass.draw(1050,430,9,2)
    coinClass.draw(575,450,9,3)
    coinClass.draw(315,640,9,4)
    solidClass.draw(0,117,1100,37.5,3)
    solidClass.draw(0,150,30,175,3)
    solidClass.draw(30,295,60,30,3)
    solidClass.draw(0,450,30,500,3)
    solidClass.draw(0,670,1100,30,3)
    solidClass.draw(30,470,80,30,3)
    solidClass.draw(1070,125,30,575,3)
    solidClass.draw(120,210,150,30,3)
    solidClass.draw(205,240,30,250,3)
    solidClass.draw(320,300,65,30,3)
    solidClass.draw(355,230,30,230,3)
    solidClass.draw(205,460,180,30,3)
    solidClass.draw(470,300,30,200,3)
    solidClass.draw(320,600,30,70,3)
    solidClass.draw(120,580,490,30,3)
    solidClass.draw(355,210,140,30,3)
    solidClass.draw(500,390,100,30,3)
    solidClass.draw(600,210,30,400,3)
    solidClass.draw(465,155,30,55,3)
    solidClass.draw(725,155,30,105,3)
    solidClass.draw(725,255,145,35,3)
    solidClass.draw(840,155,30,100,3)
    solidClass.draw(725,355,145,30,3)
    solidClass.draw(955,155,30,60,3)
    solidClass.draw(955,270,30,210,3)
    solidClass.draw(840,385,30,185,3)
    solidClass.draw(630,450,120,30,3)
    solidClass.draw(840,560,135,30,3)
    solidClass.draw(815,290,30,65,3)
    solidClass.draw(720,560,120,30,3)
    solidClass.draw(985,355,85,30,3)
    enemyClass.draw(205,490,50,35,2)
    enemyClass.draw(350,545,50,35,1)
    enemyClass.draw(720,590,255,25,6)

def level11Data():
    finishClass.draw(960,225,12,0,0)
    teleportClass.draw(790,285,50,205,1,2,0,3)
    enemyClass.draw(0,125,10,600,6)
    solidClass.draw(0,575,950,30,3)
    solidClass.draw(100,450,1000,30,3)
    solidClass.draw(0,255,750,90,3)
    solidClass.draw(0,115,1100,30,3)
    solidClass.draw(880,260,500,220,3)
    solidClass.draw(750,255,130,30,3)
    solidClass.draw(200,145,80,50,4)
    solidClass.draw(400,205,80,50,4)
    solidClass.draw(600,145,80,50,4)
    solidClass.draw(800,205,80,50,4)
    enemyClass.draw(280,145,320,5,6)
    enemyClass.draw(480,250,320,5,6)
    enemyClass.draw(1090,480,10,225,6)
    enemyClass.draw(200,605,90,30,6)
    enemyClass.draw(400,675,90,30,6)
    enemyClass.draw(600,605,90,30,6)
    enemyClass.draw(800,675,90,30,6)
    enemyClass.draw(700,530,200,45,6)
    enemyClass.draw(400,480,200,45,6)
    enemyClass.draw(125,555,175,20,6)
    enemyClass.draw(125,480,175,20,6)
    enemyClass.draw(230,250,170,5,6)
    enemyClass.draw(190,345,50,50,2)
    enemyClass.draw(360,400,50,50,1)
    enemyClass.draw(515,345,100,15,6)
    enemyClass.draw(515,415,100,35,6)
    PropImage(980,168,100,100,0).draw()

#Core Game Class Mechanics
class EnemyBlock: #enemyClass.draw(x,y,l,w,imageIndex)
    def draw(self,x,y,l,w,index = 0):
        global gameActive, lives
        enemyArray = ["emptyEnemy","spike1","spike2","spike3","spike4","spikeBall","enemyFlame"]
        self.enemyImage = pygame.image.load("images/sprites/" +enemyArray[index] + ".png").convert_alpha()
        self.enemyImage = pygame.transform.scale(self.enemyImage,(l,w))
        self.enemy = self.enemyImage.get_rect(topleft = (x,y))
        screen.blit(self.enemyImage,self.enemy)
        if player.colliderect(self.enemy):
            lives -= 1
            gameActive = False
            pygame.mixer_music.stop()

class SolidBlock: #solidClass.draw(x,y,l,w,imageIndex) -- TO BE FIXED
    def draw(self,x,y,l,w,index = 0):
        textureArray = ["dirt","dirt2","dirt3","castle","block"]
        solidImage = pygame.image.load("images/platforms/" + textureArray[index] + ".png").convert()
        solidImage = pygame.transform.scale(solidImage,(l,w))
        solidDisplay = solidImage.get_rect(topleft = (x,y))
        screen.blit(solidImage,solidDisplay)
        #"""
        if player.colliderect(solidDisplay): #block collisions (BUGGY)
            if (player.top < solidDisplay.top + 45) and (player.top <= solidDisplay.y): #OK
                player.top = solidDisplay.top - 45
                #print("c")
            elif (player.bottom > solidDisplay.bottom - 45) and (player.bottom > solidDisplay.y): #OK
                player.bottom = solidDisplay.bottom + 45
                #print("d")
            #if(player.left > block.left) and (player.left - 50 > block.x):
            elif (player.left > solidDisplay.left) and (player.left > solidDisplay.x):
                #player.x += 3 DEFAULT
                player.x += 3 
                #print("a")
            #if(player.right < block.right - 50) and (player.right < block.right)
            elif (player.right < solidDisplay.right) and (player.right < solidDisplay.right): 
               #player.x == 3 DEFAULT
               player.x -= 3 
               #print("b")
        #"""

class CoinBlock: #coinClass.draw(x,y,row,col)
    def draw(self,x,y,row = 0, col = 0):
        global coinCount, coinLife, lives
        self.coinImage = pygame.image.load("images/sprites/coin.png").convert_alpha()
        self.coinImage = pygame.transform.scale(self.coinImage,(50,50))
        self.coinDisplay = self.coinImage.get_rect(midright = (x,y))
        if coinStorage[row][col] == True: screen.blit(self.coinImage, self.coinDisplay)
        if player.colliderect(self.coinDisplay) and coinStorage[row][col] == True:
            soundArray[2].play()
            coinStorage[row][col] = False
            coinCount += 1
            coinLife -= 1
            if coinLife == 0:
                lives += 1
                coinLife = 15
                soundArray[4].play()
    
    def extraLifeCount(self,x,y):
        self.textSurface = uiFont.render("1-UP x " + str(int(coinLife)),False,"black")
        self.textSurfaceRect = self.textSurface.get_rect(topleft = (screenWidth / 2.1525 + x,screenHeight / 8.25 - 30 + y))
        screen.blit(self.textSurface,self.textSurfaceRect)
        
class FinishLine: #finishClass.draw(x,y,nextLevel,nextX,nextY, max (optional))
    def draw(self,x,y,nextLevel,nextX,nextY,max = 11 + 1):
        global level, playerXpos, playerYpos, transitiondelay, gameActive, finished
        self.finishImage = pygame.image.load("images/sprites/finishFlag.png").convert_alpha()
        self.finishImage = pygame.transform.scale(self.finishImage,(60,60))
        self.finishDisplay = self.finishImage.get_rect(center = (x,y))
        screen.blit(self.finishImage,self.finishDisplay)
        if player.colliderect(self.finishDisplay):
            level = nextLevel
            playerXpos = nextX
            playerYpos = nextY
            if level < max: #Next Level
              print(str(playerXpos) + "," + str(playerYpos) + " - NEXT LEVEL")
              player.x = playerXpos
              player.y = playerYpos
              transitiondelay = 0
              print("--CURRENT LEVEL: "+str(level) + "--")
              soundArray[4].play()
        if player.colliderect(self.finishDisplay) and level == max: #Victory
            soundArray[4].play()
            pygame.mixer.music.stop()
            gameActive = False
            finished = True

class TeleportBlock: #teleportClass.draw(x1,y1,x2,y2,action1(tp2),action2(tp1))
    def draw(self,x1,y1,x2,y2,action1 = 1,action2 = 1,index1 = 0, index2 = 2):
        global teleportdelay
        newPos = 90
        tpArray = ["tp1_1","tp1_2","tp2_1","tp2_2"]
        self.tp1Image = pygame.image.load("images/sprites/" + tpArray[index1] + ".png").convert_alpha()
        self.tp1Image = pygame.transform.scale(self.tp1Image,(50,50))
        self.tp1 = self.tp1Image.get_rect(topleft = (x1,y1))
        self.tp2Image = pygame.image.load("images/sprites/" + tpArray[index2] + ".png").convert_alpha()
        self.tp2Image = pygame.transform.scale(self.tp2Image,(50,50))
        self.tp2 = self.tp2Image.get_rect(topleft = (x2,y2))
        screen.blit(self.tp1Image,self.tp1)
        screen.blit(self.tp2Image,self.tp2)
        """
        *ACTIONS*
        1: Player.x + 100
        2: Player.y + 100
        3: Player.x - 100
        4: Player.y - 100
        """
        if player.colliderect(self.tp1) and teleportdelay > 50:
            soundArray[3].play()
            if action1 == 1: player.x,player.y = self.tp2.x + newPos,self.tp2.y
            elif action1 == 2: player.x,player.y = self.tp2.x,self.tp2.y + newPos
            elif action1 == 3: player.x,player.y = self.tp2.x - newPos,self.tp2.y
            elif action1 == 4: player.x,player.y = self.tp2.x,self.tp2.y - newPos
            teleportdelay = 0
        elif player.colliderect(self.tp2) and teleportdelay > 50:
            soundArray[3].play()
            if action2 == 1: player.x,player.y = self.tp1.x + newPos,self.tp1.y
            elif action2 == 2: player.x,player.y = self.tp1.x,self.tp1.y + newPos
            elif action2 == 3: player.x,player.y = self.tp1.x - newPos,self.tp1.y
            elif action2 == 4: player.x,player.y = self.tp1.x,self.tp1.y - newPos
            teleportdelay = 0

#Important Variables
startButton = True #Main Menu Start Button
screenWidth, screenHeight = 1100, 700
screen = pygame.display.set_mode((screenWidth,screenHeight))
fps = 144
dt = 0 #Delta time for framerate
gameActive = True
level = 0 #Set level = 0 for title screen
finished = False
timeLimit = 400

#Game Variables
pygame.display.set_caption("Alien Delivery")
pygame.mixer.music.load("audio/BGmusic.ogg")
sound = pygame.mixer.Sound
playerXpos = 180 #level 1 x position
playerYpos = 325 #level 1 y position
speed = 450 #player speed
timer = timeLimit + 1 #time limit
coinCount = 0
coinLife = 15
scoreFont = pygame.font.Font(None,70)
restartFont = pygame.font.Font(None,45)
uiFont = pygame.font.Font(None,35)
respawndelay = 0 #Respawn Delay
transitiondelay = 50 #transition Delay
teleportdelay = 0 #teleport Delay
audioFix = 0 #Prevents crash audio from playing twice
musicToggle = 0
audioToggle = 0
audioVolume = 0.60
lives = 5 - 1

#Images
titlescreen = pygame.image.load("images/backgrounds/titlescreen.png").convert_alpha()
titlescreen = pygame.transform.scale(titlescreen,(1100,700))
background = pygame.image.load("images/backgrounds/background.png").convert_alpha()
background = pygame.transform.scale(background,(screenWidth,screenHeight))
background2 = pygame.image.load("images/backgrounds/background2.png").convert_alpha()
ufoPlayerImage = pygame.image.load("images/sprites/ufoplayer.png").convert_alpha()
ufoPlayerImage = pygame.transform.scale(ufoPlayerImage,(80,45))
player = ufoPlayerImage.get_rect(topleft = (playerXpos,playerYpos))

#-Coin Storage Arrays-
row = 11 - 1 #LEVELS (REMEMBER 0 BASED INDEXING)
col = 5 #NUMBER OF COINS FOR EACH STAGE
coinStorage = [[True for x in range(col)] for x in range(row)]
clouds = ["cloud1.png","cloud2.png","cloud3.png"]

#Classes
enemyClass = EnemyBlock()
solidClass = SolidBlock()
coinClass = CoinBlock()
cloud1 = Clouds(random.randint(0,screenWidth) - 250,150,250,150,clouds[random.randint(0,len(clouds) - 1)])
cloud2 = Clouds(random.randint(0,screenWidth) + 650,50,200,200,clouds[random.randint(0,len(clouds) - 1)])
finishClass = FinishLine()
menuClass = MenuButton()
teleportClass = TeleportBlock()
introUFO = PropImage(700,350,175,175,2)

#Arrays
soundArray = [sound("audio/explosion.mp3"),sound("audio/click.mp3"),sound("audio/coinsound.wav"),sound("audio/teleport.mp3"),sound("audio/ding.mp3")]
levelArray = [level1Data,level2Data,level3Data,level4Data,level5Data,level6Data,level7Data,level8Data,level9Data,level10Data,level11Data]

#Pygame
running = True
animateIntro = False
while running:
    if gameActive and level > 0: #ACTIVE GAME CODE
        #Mechanics
        if timer < 0: gameActive = False
        if level > 0 and level < 9: screen.blit(background,(0,0))
        else: screen.blit(background2,(0,0))
        transitiondelay += 1
        teleportdelay += 1
        levelArray[level-1]()
        screen.blit(ufoPlayerImage,player)
        scoreboard(lives + 1, -260, -285, 10, 5,0,30)
        scoreboard(timer, +80, 25, 10,350,1)
        scoreboard(coinCount, +400, +345, + -1,695,2,-20,-20)
        coinClass.extraLifeCount(295,+29)
        timer -= (1 / (fps / 1.5))
    elif level == 0: #Title screen and level 0 Data
        screen.blit(titlescreen,(0,0))
        cloud1.draw()
        cloud2.draw()
        introUFO.draw()
        gameOverScreen("Alien Delivery", 3, 8.8, "Deliver the package to the customer...", 4.10, 8, 1.5, 4.8, 1.65, 6.5, 6.25, 12, 5.2, 9)
        playButton = pygame.Rect(screenWidth / 2.8,screenHeight / 2.8,300,100)
        musicButton = pygame.Rect(screenWidth / 2.8, screenHeight / 1.85,100,100)
        audioButton = pygame.Rect(screenWidth / 2.8 + 200, screenHeight / 1.85,100,100)
        
        if not startButton: #Play button
            menuClass.play((105,105,105))
        else:
            menuClass.play("white")
        
        #Audio Settings
        if musicToggle % 2 == 0: #Enabled Music
            menuClass.draw(2.735,1.85,80,2.668,1.8,255,255,255,408,280 + 100,1,-11)
            musicVolume = 0.55
        else: #Disabled Music
            menuClass.draw(2.735,1.85,80,2.668,1.8,105,105,105,408,380,1,-11)
            pygame.draw.line(screen,"red", (393.5,379), (489,480),10)
            musicVolume = 0

        if audioToggle % 2 == 0: #Enabled Audio
            menuClass.draw(2.735,1.85,80,2.668,1.8,255,255,255,408,385.5,0,190)
            audioVolume = 0.60
        else: #Disabled Audio
            menuClass.draw(2.735,1.85,80,2.668,1.8,105,105,105,408,385.5,0,190)
            pygame.draw.line(screen,"red",(593.5,379), (689, 480), 10)
            audioVolume = 0
        
        for i in range(0,len(soundArray)): soundArray[i].set_volume(audioVolume)
        pygame.mixer.music.set_volume(musicVolume)
        
        #Animation Intro
        if animateIntro:
            introUFO.y -= 3.75
            if introUFO.y < -600:
                level = 1
                animateIntro = False
    else:
        gameActive = False
        respawndelay += 1
        if not finished:
            audioFix += 1
            PropImage(player.x + 50,player.y + 50,150,150,-1).deathSprite(audioFix,audioVolume)
            if timer <= 0: gameOverScreen("PACKAGE IS LATE!", 3.5, 2.5, "Press the 'space' key to restart",3.5,3.25)
            elif lives > -1: gameOverScreen("YOU CRASHED", 3.2, 2.5, "Press the 'space' key to respawn",3.7,3.25)
            elif lives <  0: gameOverScreen("ZERO LIVES", 2.9, 2.5, "Press the 'space' key to restart",3.5,3.25)
        elif finished and timer > 0: 
            gameOverScreen("Congratulations!", 3.25, 2.5, "Press the 'space' key to return to level 1.",4.25,3.25)

    #KEYBINDS
    if level > 0:
        key = pygame.key.get_pressed()
        if transitiondelay >= 50:
            if (key[pygame.K_w] and key[pygame.K_d] or (key[pygame.K_UP] and key[pygame.K_RIGHT])): player.move_ip(speed * dt,-speed * dt)
            elif (key[pygame.K_w] and key[pygame.K_a] or (key[pygame.K_UP] and key[pygame.K_LEFT])): player.move_ip(-speed * dt,-speed * dt)
            elif (key[pygame.K_s] and key[pygame.K_d] or (key[pygame.K_DOWN] and key[pygame.K_RIGHT])): player.move_ip(speed * dt,speed * dt)
            elif (key[pygame.K_s] and key[pygame.K_a] or (key[pygame.K_DOWN] and key[pygame.K_LEFT])): player.move_ip(-speed * dt,speed * dt)
            elif (key[pygame.K_w] or key[pygame.K_UP]): player.move_ip(0,-speed * dt)
            elif (key[pygame.K_s] or key[pygame.K_DOWN]): player.move_ip(0,speed * dt)
            elif (key[pygame.K_a] or key[pygame.K_LEFT]): player.move_ip(-speed * dt,0)
            elif (key[pygame.K_d] or key[pygame.K_RIGHT]): player.move_ip(speed * dt,0)
            else: player.move_ip(0,0)
        
        #keeps player on screen
        if player.x < 0: player.x = 0
        if player.x > screenWidth - 85: player.x = screenWidth - 85
        if player.y <= 0: player.y = 0
        if player.y >= screenHeight - 50: player.y = screenHeight - 50
    
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit(), exit()
        #--Click to print mouse coordinates / Delete when done--
        """
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mousePos = pygame.mouse.get_pos()
            print(mousePos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: exit()
        """
        #---------------------------------------------
        if level > 0 and respawndelay >= 50:
            if (event.type == pygame.KEYDOWN and lives < 0 and not finished) or (event.type == pygame.KEYDOWN and gameActive == False and finished) and timer > 0:
                #Zero Lives OR Completes Game
                if event.key == pygame.K_SPACE:
                    restartGame()
            elif ((event.type == pygame.KEYDOWN and gameActive == False) and not finished) and timer > 0: #Respawns Player
                if event.key == pygame.K_SPACE:
                    gameActive = True
                    print(str(playerXpos) + "," + str(playerYpos) + " - RESPAWNED")
                    player.x = playerXpos
                    player.y = playerYpos
                    respawndelay = 0
                    audioFix = 0
                    transitiondelay = 0
                    pygame.mixer.music.play(-1)
            elif timer < 0 and gameActive == False: #Player runs out of time.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        restartGame()
        elif level == 0 and event.type == pygame.MOUSEBUTTONDOWN: #Menu Screen
            mousePos = pygame.mouse.get_pos()
            if startButton:
                if playButton.collidepoint(mousePos):
                    print("Title Screen clicked")
                    animateIntro = True
                    pygame.mixer.music.play(-1)
                    startButton = False
                    soundArray[1].play()
                elif musicButton.collidepoint(mousePos): 
                    musicToggle += 1
                    soundArray[1].play()
                elif audioButton.collidepoint(mousePos): 
                    audioToggle += 1
                    soundArray[1].play()
    pygame.display.update()
    clock = pygame.time.Clock()
    dt = clock.tick(fps) / 1000 #Deltatime solved by fps / 1000
pygame.quit()