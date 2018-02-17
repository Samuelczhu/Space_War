'''
arts from opengameart
theme music: Alexandr Zhelanov, https://soundcloud.com/alexandr-zhelanov
info music: Please credit Kerri Coombs, Living Midnight Design
game music: https://soundcloud.com/alexandr-zhelanov
loose music: Alexandr Zhelanov, https://soundcloud.com/alexandr-zhelanov
'''

import pygame
import random
import math
from os import path


#******basic******
width = 770
height = 670
fps = 60

black = (0,0,0)
white = (255,255,255)
red  = (200,0,0)
brightred = (255,0,0)
green = (0,200,0)
brightgreen = (0,255,0)
blue = (0,0,200)
brightblue = (0,0,255)
yellow = (200,200,0)
brightyellow = (255,255,0)
purple = (200,0,200)
brightpurple = (255,0,255)
orange = (255,128,0)

img_dir = path.join(path.dirname(__file__),"img")
snd_dir = path.join(path.dirname(__file__),"snd")


#******Setup******
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space War")
icon = pygame.image.load("icon.png")
icon.set_colorkey(black)
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#******load_graphic********
background = pygame.image.load(path.join(img_dir,"background.jpg")).convert()
backgound = pygame.transform.scale(background,(width,height))
introbackground = pygame.image.load(path.join(img_dir,"introbackground.jpg")).convert()
introbackground = pygame.transform.scale(introbackground,(width,height))
infobackground = pygame.image.load(path.join(img_dir,"infobackground.jpg")).convert()
infobackground = pygame.transform.scale(infobackground,(width,height))
gameoverbackground = pygame.image.load(path.join(img_dir,"gameover.jpg")).convert()
gameoverbackground = pygame.transform.scale(gameoverbackground,(width,height))
playerimg = pygame.image.load(path.join(img_dir,"player.png")).convert()
liveupimg = pygame.transform.scale(playerimg,(50,40))
meteo_list = ["m1.png","m2.png","m3.png","m4.png","m5.png","m6.png","m7.png"]
mybulletimg = pygame.image.load(path.join(img_dir,"mylaser.png")).convert()
bulletupimg = pygame.image.load(path.join(img_dir,"bulletup.png")).convert()
speedupimg = pygame.image.load(path.join(img_dir,"speedup.png")).convert()
healthupimg = pygame.image.load(path.join(img_dir,"healthup.png")).convert()
enemy1img = pygame.image.load(path.join(img_dir,"enemy1.png")).convert()
enemy2img = pygame.image.load(path.join(img_dir,"enemy2.png")).convert()
roundbulletimg = pygame.image.load(path.join(img_dir,"roundbullet.png")).convert()
boss1img = pygame.image.load(path.join(img_dir,"boss1.png")).convert()
laser1img = pygame.image.load(path.join(img_dir,"laser1.png")).convert()
enemy3img = pygame.image.load(path.join(img_dir,"enemy3.png")).convert()
dartimg = pygame.image.load(path.join(img_dir,"dart.png")).convert()
boss2img = pygame.image.load(path.join(img_dir,"boss2.png")).convert()
boss3img = pygame.image.load(path.join(img_dir,"boss3.png")).convert()
ximg = pygame.image.load(path.join(img_dir,"x.png")).convert()
shieldimg = pygame.image.load(path.join(img_dir,"shield.png")).convert()
shieldupimg = pygame.image.load(path.join(img_dir,"shieldup.png")).convert()
shield_symbolimg = pygame.image.load(path.join(img_dir,"shieldsymbol.png")).convert()
missileimg = pygame.image.load(path.join(img_dir,"missile.png")).convert()
missile_symbolimg = pygame.image.load(path.join(img_dir,"missilesymbol.png")).convert()
missileupimg = pygame.image.load(path.join(img_dir,"missileup.png")).convert()
upimg = pygame.image.load(path.join(img_dir,"up.png")).convert()
upimg = pygame.transform.scale(upimg,(40,40))
downimg = pygame.image.load(path.join(img_dir,"down.png")).convert()
downimg = pygame.transform.scale(downimg,(40,40))
leftimg = pygame.image.load(path.join(img_dir,"left.png")).convert()
leftimg = pygame.transform.scale(leftimg,(40,40))
rightimg = pygame.image.load(path.join(img_dir,"right.png")).convert()
rightimg = pygame.transform.scale(rightimg,(40,40))
spaceimg = pygame.image.load(path.join(img_dir,"space.png")).convert()
spaceimg = pygame.transform.scale(spaceimg,(80,40))

explosion_anim = {}
explosion_anim['large'] = []
explosion_anim['small'] = []
explosion_anim['death'] = []
for i in range(9):
    fname = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir,fname)).convert()
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img,(100,100))
    explosion_anim['large'].append(img_lg)
    img_sm = pygame.transform.scale(img,(50,50))
    explosion_anim['small'].append(img_sm)
    fname = "sonicExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir,fname)).convert()
    img.set_colorkey(black)
    explosion_anim['death'].append(img)


#******load_sound********
bulletup_sound = pygame.mixer.Sound(path.join(snd_dir,'bulletup.wav'))
shieldup_sound = pygame.mixer.Sound(path.join(snd_dir,'shieldup.wav'))
healthup_sound = pygame.mixer.Sound(path.join(snd_dir,'healthup.wav'))
liveup_sound = pygame.mixer.Sound(path.join(snd_dir,'liveup.wav'))
missileup_sound = pygame.mixer.Sound(path.join(snd_dir,'missileup.wav'))
speedup_sound = pygame.mixer.Sound(path.join(snd_dir,'speedup.wav'))

explodesm_sound = pygame.mixer.Sound(path.join(snd_dir,'explodesm.wav'))
explodebg_sound = pygame.mixer.Sound(path.join(snd_dir,'explodebg.wav'))
explodedeath_sound = pygame.mixer.Sound(path.join(snd_dir,'explodedeath.wav'))

shoot_sound = pygame.mixer.Sound(path.join(snd_dir,'shoot.wav'))
missile_sound = pygame.mixer.Sound(path.join(snd_dir,'missile.wav'))
shield_sound = pygame.mixer.Sound(path.join(snd_dir,'shield.wav'))

#*********Function**********
def quitgame():
    pygame.quit()
    quit()

def newmeteorite():
    m = Meteorite()
    meteorite_sprites.add(m)
    all_sprites.add(m)

def newbullet(x,y,radian):
    bullet = Mybullet(x, y, radian)
    bullet_sprites.add(bullet)
    all_sprites.add(bullet)

def newbulletup():
    bulletup = Bulletup()
    bulletup_sprites.add(bulletup)
    all_sprites.add(bulletup)
    return bulletup

def newspeedup():
    speedup = Speedup()
    speedup_sprites.add(speedup)
    all_sprites.add(speedup)
    return speedup

def newhealthup():
    healthup = Healthup()
    healthup_sprites.add(healthup)
    all_sprites.add(healthup)

def newliveup():
    liveup = Liveup()
    liveup_sprites.add(liveup)
    all_sprites.add(liveup)

def newshieldup():
    shieldup = Shieldup()
    shieldup_sprites.add(shieldup)
    all_sprites.add(shieldup)
    return shieldup

def newmissileup():
    missileup = Missileup()
    missileup_sprites.add(missileup)
    all_sprites.add(missileup)

def newenemy1():
    enemy1 = Enemy1()
    enemy1_sprites.add(enemy1)
    all_sprites.add(enemy1)
    return enemy1
def newenemy2():
    enemy2 = Enemy2()
    enemy2_sprites.add(enemy2)
    all_sprites.add(enemy2)
    return enemy2
def newenemy3():
    enemy3 = Enemy3()
    enemy3_sprites.add(enemy3)
    all_sprites.add(enemy3)
    return enemy3

def newboss1():
    boss1 = Boss1()
    boss1_sprites.add(boss1)
    all_sprites.add(boss1)
    return boss1
def newboss2():
    boss2 = Boss2()
    boss2_sprites.add(boss2)
    all_sprites.add(boss2)
    return boss2
def newboss3():
    boss3 = Boss3()
    boss3_sprites.add(boss3)
    all_sprites.add(boss3)
    return boss3

def new_roundbullet(x,y,angle):
    roundbullet = Roundbullet(x,y,angle)
    roundbullet_sprites.add(roundbullet)
    all_sprites.add(roundbullet)

def new_laser1(x,y,angle):
    laser1 = Laser1(x,y,angle)
    laser1_sprites.add(laser1)
    all_sprites.add(laser1)

def new_dart(x,y,angle):
    dart = Dart(x,y,angle)
    dart_sprites.add(dart)
    all_sprites.add(dart)

def new_x(x,y,angle):
    x = X(x,y,angle)
    x_sprites.add(x)
    all_sprites.add(x)


def health(ph,x,y):
    if ph <= 0:
        ph = 0
    container = pygame.Rect(x,y,150,20)
    blood = pygame.Rect(x+1,y+1,150*ph/100-2,20-2)
    pygame.draw.rect(screen,white,container,1)
    pygame.draw.rect(screen,red,blood)


def newshield(center):
    shield = Shield(center)
    shield_sprites.add(shield)
    all_sprites.add(shield)

def newmissile(centerx,centery):
    missile = Missile(centerx,centery)
    missile_sprites.add(missile)
    all_sprites.add(missile)

def drawlive(live,x,y):
    liveimg = pygame.transform.scale(playerimg,(42,30))
    liveimg.set_colorkey(black)
    for i in range(live):
        screen.blit(liveimg,(x+i*50,y))

def drawscore(score,x,y):
    label("Score: ",x,y,25,purple)
    label(str(score),x+100,y,25,orange)

def drawshield(num_shield,x,y):
    shield_image = pygame.transform.scale(shield_symbolimg,(50,50))
    shield_image.set_colorkey(black)
    screen.blit(shield_image,(x,y))
    label("X "+str(num_shield),x+65,y+5,30,orange)
def drawmissile(num_missile,x,y):
    missile_image = pygame.transform.scale(missile_symbolimg,(50,50))
    missile_image = pygame.transform.rotate(missile_image,45)
    missile_image.set_colorkey(white)
    screen.blit(missile_image,(x,y))
    label("X "+str(num_missile),x+65,y+5,30,orange)

def label(msg,x,y,size,color):
    font = pygame.font.SysFont("Trebuchet MS",size)
    text = font.render(msg,True,color)
    screen.blit(text,(x,y))

def Button(msg,x,y,width,height,i_color,a_color,command=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen,a_color,(x,y,width,height))
        if click[0] == 1 and command != None:
            command()
    else:
        pygame.draw.rect(screen,i_color,(x,y,width,height))
    buttontext = pygame.font.SysFont("Trebuchet MS",20)
    buttonmsg = buttontext.render(msg,True,black)
    buttonmsgrect = buttonmsg.get_rect()
    buttonmsgrect.center = ((x+width/2),(y+height/2))
    screen.blit(buttonmsg,buttonmsgrect)
#*********Class*********
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(playerimg, (70, 50))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height - 20
        self.radius = 27
        self.speedx = 0
        self.speedy = 0
        self.lastshoot = pygame.time.get_ticks()
        self.score = 0
        self.ph = 100
        self.live = 3
        self.shootdelay = 400
        self.bulletpower = 1
        self.bulletpower_delay = 20000
        self.bulletpower_time = pygame.time.get_ticks()
        self.bulletpower_now = pygame.time.get_ticks()
        self.speedup_delay = 20000
        self.speedup_time = pygame.time.get_ticks()
        self.shield = 0
        self.missile = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.lastshoot > self.shootdelay:
            self.lastshoot = now
            shoot_sound.play()
            if self.bulletpower == 1:
                newbullet(self.rect.x+29,self.rect.y,math.pi/2)
            if self.bulletpower == 2:
                newbullet(self.rect.x-5,self.rect.y,math.pi/2)
                newbullet(self.rect.x+70-8,self.rect.y,math.pi/2)
            if self.bulletpower == 3:
                newbullet(self.rect.x+29,self.rect.y,math.pi/2)
                newbullet(self.rect.x-7, self.rect.y, math.pi / 2)
                newbullet(self.rect.x + 70-6, self.rect.y, math.pi / 2)
            if self.bulletpower == 4:
                newbullet(self.rect.x+29,self.rect.y,math.pi/2)
                newbullet(self.rect.x-7, self.rect.y, math.pi / 2)
                newbullet(self.rect.x + 70-6, self.rect.y, math.pi / 2)
                newbullet(self.rect.x-5-20,self.rect.y-10,math.pi*(7/18))
                newbullet(self.rect.x+70-8+20,self.rect.y-10,math.pi*(1-7/18))

            if self.bulletpower >= 5:
                newbullet(self.rect.x+29,self.rect.y,math.pi/2)
                newbullet(self.rect.x-7, self.rect.y, math.pi / 2)
                newbullet(self.rect.x + 70-6, self.rect.y, math.pi / 2)
                newbullet(self.rect.x-5-20,self.rect.y-10,math.pi*(7/18))
                newbullet(self.rect.x+70-8+20,self.rect.y-10,math.pi*(1-7/18))
                newbullet(self.rect.x-5-20-10,self.rect.y-15,math.pi*1/4)
                newbullet(self.rect.x+70-8+20+10,self.rect.y-15,math.pi*(1-1/4))

    def update(self):
        self.speedx = 0
        self.speedy = 0
        # set for bullet power
        self.bulletpower_now = pygame.time.get_ticks()
        if self.bulletpower_now - self.bulletpower_time > self.bulletpower_delay:
            self.bulletpower_time = pygame.time.get_ticks()
            self.bulletpower -= 1
        if self.bulletpower < 1:
            self.bulletpower = 1
        # set for speedup
        self.speedup_now = pygame.time.get_ticks()
        if self.speedup_now - self.speedup_time > self.speedup_delay:
            self.speedup_time = pygame.time.get_ticks()
            self.shootdelay += 50
        if self.shootdelay < 100:
            self.shootdelay = 100
        if self.shootdelay > 400:
            self.shootdelay = 400
        # player ph and live
        if self.ph > 100:
            self.ph = 100
        if self.ph < 0:
            expl = Explosion(self.rect.center, 'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            self.live -= 1
            self.ph = 100
            self.rect.centerx = width / 2
            self.rect.bottom = height - 20
        if player.live < 0:
            player.kill()
            gameover()
        # key event
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speedx = 6
        if keystate[pygame.K_LEFT]:
            self.speedx = -6
        if keystate[pygame.K_UP]:
            self.speedy = -6
        if keystate[pygame.K_DOWN]:
            self.speedy = 6
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height


class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.meteochoice = random.choice(meteo_list)
        self.meteoriteimg_orig = pygame.image.load(path.join(img_dir, self.meteochoice)).convert()
        self.meteoriteimg_orig.set_colorkey(black)
        self.meteoriteimg = self.meteoriteimg_orig.copy()
        self.image = self.meteoriteimg
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width)
        self.rect.y = -500
        self.radius = int(self.rect.width * 0.85 / 2)
        self.speedx = random.randrange(-10,10)
        self.speedy = random.randrange(3,13)
        self.rot = 0
        self.rotspeed = random.randrange(-15,15)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot+self.rotspeed)%360
            newimage = pygame.transform.rotate(self.meteoriteimg_orig,self.rot)
            old_center = self.rect.center
            self.image = newimage
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.right < 0) or (self.rect.left > width) or (self.rect.top > height):
            self.rect.x = random.randrange(0, width)
            self.rect.y = -500
            self.speedx = random.randrange(-10, 10)
            self.speedy = random.randrange(3, 13)


class Mybullet(pygame.sprite.Sprite):
    def __init__(self,x,y,radian):
        pygame.sprite.Sprite.__init__(self)
        self.image = mybulletimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x
        self.speed = -15
        self.speedx = math.cos(radian)*self.speed
        self.speedy = math.sin(radian)*self.speed

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.bottom < 0) or (self.rect.right < 0) or (self.rect.left > width):
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,mode):
        pygame.sprite.Sprite.__init__(self)
        self.mode = mode
        self.image = explosion_anim[self.mode][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.update_rate = 90

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.update_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.mode]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.mode][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Bulletup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -500
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()


class Speedup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = speedupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -500
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()

class Healthup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = healthupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -500
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()


class Liveup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(playerimg,(35,25))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -500
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()


class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_org = pygame.transform.scale(enemy1img,(90,70))
        self.image_org.set_colorkey(black)
        self.image = self.image_org.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -random.randrange(300,1300)
        self.radius = int(self.rect.width * 0.85 / 2)
        self.speedy = 3
        self.rotate_time = pygame.time.get_ticks()
        self.angle = 0
        self.shoot_time = pygame.time.get_ticks()
        self.shoot_delay = 700
        self.ph = 70
        self.fullph = 70
        self.drawph = False

    def rotate(self,angle):
        now = pygame.time.get_ticks()
        if now - self.rotate_time > 50:
            self.rotate_time = pygame.time.get_ticks()
            newimage = pygame.transform.rotate(self.image_org,angle)
            oldcenter = self.rect.center
            self.image = newimage
            self.rect = self.image.get_rect()
            self.rect.center = oldcenter

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shoot_time > self.shoot_delay and self.rect.y > 0:
            self.shoot_time = pygame.time.get_ticks()
            new_roundbullet(self.rect.centerx,self.rect.centery,self.angle)

    def enemy_health(self,ph, fullph, x, y):
        container = pygame.Rect(x, y, 150, 20)
        blood = pygame.Rect(x + 1, y + 1, 150 * ph / fullph - 2, 20 - 2)
        pygame.draw.rect(screen, white, container, 1)
        pygame.draw.rect(screen, purple, blood)

    def update(self):
        try:
            self.angle = math.degrees(math.atan((player.rect.x-self.rect.x)/(player.rect.y-self.rect.y)))
        except:
            self.angle = 0
        if player.rect.y < self.rect.y:
            self.angle = 180 + self.angle
        self.rotate(self.angle)
        self.shoot()
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.drawph = False
            self.kill()
        if self.ph <= 0:
            self.drawph = False
            expl = Explosion(self.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            self.kill()

class Enemy2(Enemy1):
    def __init__(self):
        Enemy1.__init__(self)
        self.image_org = pygame.transform.scale(enemy2img,(90,70))
        self.image_org.set_colorkey(black)
        self.image = self.image_org.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -random.randrange(700,2800)
        self.radius = int(self.rect.width * 0.85 / 2)
        self.shoot_delay = 500
        self.ph = 120
        self.fullph = 120


class Roundbullet(pygame.sprite.Sprite):
    def __init__(self,x,y,degree):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(roundbulletimg,(30,30))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 7
        self.speedx = self.speed*math.sin(math.radians(degree))
        self.speedy = self.speed * math.cos(math.radians(degree))

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.top > height) or (self.rect.right < 0) or (self.rect.left > width):
            self.kill()

class Boss1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss1img
        self.image.set_colorkey((black))
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.centery = -3500
        self.speedy = 2
        self.speedx = 2
        self.shoot_mode = 1
        self.shootdelay = 700
        self.shoot_time = pygame.time.get_ticks()
        self.shiftmode_delay = 10000
        self.shift_time = pygame.time.get_ticks()
        self.ph = 1000
        self.fullph = 1000
        self.drawph = False

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shoot_time > self.shootdelay:
            self.shoot_time = now
            if self.shoot_mode == 1:
                new_laser1(self.rect.left+20, self.rect.centery+60, -math.pi/2)
                new_laser1(self.rect.right-20, self.rect.centery+60, -math.pi/2)
            if self.shoot_mode == 2:
                new_roundbullet(self.rect.left+20, self.rect.centery+60, -30)
                new_roundbullet(self.rect.right-20, self.rect.centery+60, 30)
                new_roundbullet(self.rect.centerx,self.rect.bottom,0)
        if now - self.shift_time > self.shiftmode_delay:
            self.shift_time = now
            self.shoot_mode += 1
            if self.shoot_mode > 2:
                self.shoot_mode = 1

    def enemy_health(self,ph, fullph, x, y):
        container = pygame.Rect(x, y, 150, 20)
        blood = pygame.Rect(x + 1, y + 1, 150 * ph / fullph - 2, 20 - 2)
        pygame.draw.rect(screen, white, container, 1)
        pygame.draw.rect(screen, orange, blood)

    def update(self):
        self.rect.centery += self.speedy
        if self.rect.top > 50:
            self.rect.top = 50
            self.rect.centerx += self.speedx
            self.shoot()
            if self.rect.right > width:
                self.speedx = -self.speedx
            if self.rect.left < 0:
                self.speedx = -self.speedx
        if self.ph <= 0:
            self.drawph = False
            expl = Explosion(self.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            self.kill()

class Laser1(Roundbullet):
    def __init__(self,x,y,degree):
        Roundbullet.__init__(self,x,y,degree)
        self.image = laser1img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

class Enemy3(Enemy1):
    def __init__(self):
        Enemy1.__init__(self)
        self.image_org = enemy3img
        self.image_org.set_colorkey(black)
        self.image = self.image_org.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -random.randrange(1000,3500)
        self.speedy = 2
        self.radius = int(self.rect.width * 0.85 / 2)
        self.shoot_delay = 350
        self.ph = 800
        self.fullph = 800

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shoot_time > self.shoot_delay and self.rect.y > 0:
            self.shoot_time = pygame.time.get_ticks()
            new_dart(self.rect.centerx,self.rect.centery,self.angle)


class Dart(Roundbullet):
    def __init__(self,x,y,degree):
        Roundbullet.__init__(self,x,y,degree)
        self.img_orig = dartimg
        self.img_orig.set_colorkey(black)
        self.image = self.img_orig.copy()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.rot = 0
        self.rotspeed = 15
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rotspeed) % 360
            newimage = pygame.transform.rotate(self.img_orig, self.rot)
            old_center = self.rect.center
            self.image = newimage
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rotate()
        if (self.rect.top > height) or (self.rect.right < 0) or (self.rect.left > width):
            self.kill()


class X(Dart):
    def __init__(self,x,y,degree):
        Dart.__init__(self,x,y,degree)
        self.img_orig = dartimg
        self.img_orig.set_colorkey(black)
        self.image = self.img_orig.copy()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.rot = 0
        self.rotspeed = 20
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = -(self.rot + self.rotspeed) % 360
            newimage = pygame.transform.rotate(self.img_orig, self.rot)
            old_center = self.rect.center
            self.image = newimage
            self.rect = self.image.get_rect()
            self.rect.center = old_center


class Boss2(Boss1):
    def __init__(self):
        Boss1.__init__(self)
        self.image = boss2img
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.centery = -3500
        self.shootdelay = 600


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shoot_time > self.shootdelay:
            self.shoot_time = now
            if self.shoot_mode == 1:
                new_laser1(self.rect.centerx+20, self.rect.bottom+20, -math.pi/2)
                new_laser1(self.rect.centerx-20, self.rect.bottom+20, -math.pi/2)
            if self.shoot_mode == 2:
                new_roundbullet(self.rect.left+20, self.rect.centery+60, -30)
                new_roundbullet(self.rect.right-20, self.rect.centery+60, 30)
                new_roundbullet(self.rect.centerx+20,self.rect.bottom,0)
                new_roundbullet(self.rect.centerx-20,self.rect.bottom,0)
            if self.shoot_mode == 3:
                new_dart(self.rect.left+20, self.rect.centery+60, -30)
                new_dart(self.rect.right-20, self.rect.centery+60, 30)
                new_dart(self.rect.centerx,self.rect.bottom,0)

        if now - self.shift_time > self.shiftmode_delay:
            self.shift_time = now
            self.shoot_mode += 1
            if self.shoot_mode > 3:
                self.shoot_mode = 1


class Boss3(Boss1):
    def __init__(self):
        Boss1.__init__(self)
        self.image = boss3img
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.centery = -3500
        self.shootdelay = 550


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shoot_time > self.shootdelay:
            self.shoot_time = now
            if self.shoot_mode == 1:
                new_laser1(self.rect.centerx+50, self.rect.bottom+20, -math.pi/2)
                new_laser1(self.rect.centerx-50, self.rect.bottom+20, -math.pi/2)
                new_roundbullet(self.rect.centerx+20, self.rect.centery+60, 30)
                new_roundbullet(self.rect.centerx-20, self.rect.centery+60, -30)
            if self.shoot_mode == 2:
                new_dart(self.rect.left+20, self.rect.centery+60, -30)
                new_dart(self.rect.right-20, self.rect.centery+60, 30)
                new_roundbullet(self.rect.centerx+20,self.rect.bottom,0)
                new_roundbullet(self.rect.centerx-20,self.rect.bottom,0)
            if self.shoot_mode == 3:
                new_dart(self.rect.centerx+50,self.rect.bottom,0)
                new_dart(self.rect.centerx-50, self.rect.bottom, 0)
                new_laser1(self.rect.centerx, self.rect.bottom+20, -math.pi/2)
                new_x(self.rect.left+20, self.rect.centery+60, -30)
                new_x(self.rect.left-20, self.rect.centery+60, -30)
        if now - self.shift_time > self.shiftmode_delay:
            self.shift_time = now
            self.shoot_mode += 1
            if self.shoot_mode > 3:
                self.shoot_mode = 1

class Shieldup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = shieldupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -500
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()


class Shield(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = shieldimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.radius = self.rect.width/2
        self.delay = 7000
        self.shield_time = pygame.time.get_ticks()

    def update(self):
        self.rect.center = player.rect.center
        now = pygame.time.get_ticks()
        if now - self.shield_time > self.delay:
            self.kill()


class Missileup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = missileupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -500
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()


class Missile(pygame.sprite.Sprite):
    def __init__(self,centerx,centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missileimg,(50,70))
        self.image.set_colorkey((black))
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedy = -7

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()



#********game*******
def intro():
    pygame.mixer.music.load(path.join(snd_dir, 'theme.mp3'))
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        screen.blit(introbackground,(0,0))
        label("Welcome",width/2-100,100,50,purple)
        label("to",width/2-10,170,30,green)
        label("Space War",width/2-150,200,60,red)
        label("Tips: kill enemies to get powerups",width/2-230,500,30,orange)
        Button("Exit",width-250,height/2+100,100,50,red,brightred,quitgame)
        Button("Start",150,height/2+100,100,50,green,brightgreen,gameloop)
        Button("Info",335,height/2+100,100,50,blue,brightblue,info)

        clock.tick(15)
        pygame.display.update()

def info():
    pygame.mixer.music.load(path.join(snd_dir, 'info.mp3'))
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        screen.blit(infobackground,(0,0))
        label("Information",width/2-160,70,60,orange)
        label("Press",130,180,40,green)
        label("Effect",width-230,180,40,green)
        screen.blit(spaceimg,(130,250))
        label("Shoot Bullets",width-250,250,25,purple)
        screen.blit(upimg,(160,310))
        screen.blit(downimg,(160,350))
        screen.blit(leftimg,(120,350))
        screen.blit(rightimg,(200,350))
        label("Move",width-200,310,25,purple)
        label("x",170,400,30,purple)
        label("Missile",width-210,380,25,purple)
        label("z",170,440,30,purple)
        label("Shield",width-210,440,25,purple)

        screen.blit(bulletupimg,(width/2-90,190))
        label("bullet type up",width/2-40,190,20,brightblue)
        screen.blit(speedupimg,(width/2-85,240))
        label("shooting speed up",width/2-40,240,20,brightblue)
        screen.blit(healthupimg,(width/2-90,290))
        label("health up",width/2-40,290,20,brightblue)
        screen.blit(liveupimg,(width/2-100,330))
        label("live up",width/2-40,335,20,brightblue)
        screen.blit(shieldupimg,(width/2-90,390))
        label("shield up",width/2-40,390,20,brightblue)
        screen.blit(missileupimg,(width/2-90,440))
        label("missile up",width/2-40,440,20,brightblue)

        Button("Exit",width-250,height/2+200,100,50,red,brightred,quitgame)
        Button("Start",150,height/2+200,100,50,green,brightgreen,gameloop)
        Button("Intro",335,height/2+200,100,50,blue,brightblue,intro)

        clock.tick(15)
        pygame.display.update()

def gameover():
    pygame.mixer.music.load(path.join(snd_dir, 'loose.mp3'))
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        screen.blit(gameoverbackground,(0,0))
        label("Game Over",width/2-250,height/2-200,100,brightred)
        Button("Exit",width-250,height/2+100,100,50,red,brightred,quitgame)
        Button("Replay", 150, height/2+100, 100, 50, green, brightgreen, gameloop)
        Button("Info",335,height/2+100,100,50,blue,brightblue,info)

        clock.tick(15)
        pygame.display.update()

def gameloop():
    pygame.mixer.music.load(path.join(snd_dir, 'game.mp3'))
    pygame.mixer.music.play(-1)
    # set up
    global all_sprites,meteorite_sprites,bullet_sprites,bulletup_sprites,speedup_sprites,healthup_sprites,liveup_sprites,enemy1_sprites,enemy2_sprites,roundbullet_sprites,boss1_sprites,laser1_sprites,dart_sprites,enemy3_sprites
    global boss2_sprites,x_sprites,boss3_sprites,shieldup_sprites,shield_sprites,missileup_sprites,missile_sprites,player
    all_sprites = pygame.sprite.Group()
    meteorite_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    bulletup_sprites = pygame.sprite.Group()
    speedup_sprites = pygame.sprite.Group()
    healthup_sprites = pygame.sprite.Group()
    liveup_sprites = pygame.sprite.Group()
    enemy1_sprites = pygame.sprite.Group()
    enemy2_sprites = pygame.sprite.Group()
    roundbullet_sprites = pygame.sprite.Group()
    boss1_sprites = pygame.sprite.Group()
    laser1_sprites = pygame.sprite.Group()
    dart_sprites = pygame.sprite.Group()
    enemy3_sprites = pygame.sprite.Group()
    boss2_sprites = pygame.sprite.Group()
    x_sprites = pygame.sprite.Group()
    boss3_sprites = pygame.sprite.Group()
    shieldup_sprites = pygame.sprite.Group()
    shield_sprites = pygame.sprite.Group()
    missileup_sprites = pygame.sprite.Group()
    missile_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(4):
        newmeteorite()

    enemy1 = newenemy1()
    enemy1.rect.y = -1000
    enemy2 = newenemy2()
    enemy2.rect.y = -3500
    boss1 = newboss1()
    boss1.rect.y = -5000
    enemy3 = newenemy3()
    enemy3.rect.y = -8000
    count1 = 1

    shieldup = newshieldup()
    shieldup.rect.y = -2000
    bulletup = newbulletup()
    bulletup.rect.y = -700
    speedup = newspeedup()
    speedup.rect.y = -2500
    shieldup = newshieldup()
    shieldup.rect.y = -4000
    bulletup = newbulletup()
    bulletup.rect.y = -1500
    speedup = newspeedup()
    speedup.rect.y = -3500


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    if player.shield > 0:
                        player.shield -= 1
                        newshield(player.rect.center)
                        shield_sound.play()
                if event.key == pygame.K_x:
                    if player.missile > 0:
                        player.missile -= 1
                        newmissile(player.rect.centerx,player.rect.centery)
                        missile_sound.play()
        clock.tick(fps)
        #******update*****
        all_sprites.update()

        # meteor hit player
        hits = pygame.sprite.spritecollide(player,meteorite_sprites,True,pygame.sprite.collide_circle)
        for hit in hits:
            player.ph -= hit.radius * 1.5
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            newmeteorite()

        # mybullet hit meteor
        hits = pygame.sprite.groupcollide(bullet_sprites,meteorite_sprites,True,True)
        for hit in hits:
            expl = Explosion(hit.rect.center,'large')
            explodebg_sound.play()
            all_sprites.add(expl)
            newmeteorite()
            player.score += 10
            bulletup_chance = random.randrange(0,100)
            if bulletup_chance > 95:
                newbulletup()
            speedup_chance = random.randrange(0,100)
            if speedup_chance > 95:
                newspeedup()
            healthup_chance = random.randrange(0,100)
            if healthup_chance > 95:
                newhealthup()
            liveup_chance = random.randrange(0,100)
            if liveup_chance > 99:
                newliveup()
            shieldup_chance = random.randrange(0,100)
            if shieldup_chance > 95:
                newshieldup()
            missileup_chance = random.randrange(0,100)
            if missileup_chance > 93:
                newmissileup()
        # missile hit meteor
        hits = pygame.sprite.groupcollide(missile_sprites,meteorite_sprites,True,True)
        for hit in hits:
            expl = Explosion(hit.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            newmeteorite()
            player.score += 10

        # player get bulletup
        hits = pygame.sprite.spritecollide(player,bulletup_sprites,True)
        for hit in hits:
            player.bulletpower += 1
            bulletup_sound.play()
            player.bulletpower_time = pygame.time.get_ticks()
        # player get speedup
        hits = pygame.sprite.spritecollide(player,speedup_sprites,True)
        for hit in hits:
            player.shootdelay -= 50
            speedup_sound.play()
        # player get health up
        hits = pygame.sprite.spritecollide(player,healthup_sprites,True)
        for hit in hits:
            player.ph += random.randrange(10,70)
            healthup_sound.play()
        # player get liveup
        hits = pygame.sprite.spritecollide(player,liveup_sprites,True)
        for hit in hits:
            player.live += 1
            liveup_sound.play()
        # player get shieldup
        hits = pygame.sprite.spritecollide(player,shieldup_sprites,True)
        for hit in hits:
            player.shield += 1
            shieldup_sound.play()
        # player get missileup
        hits = pygame.sprite.spritecollide(player,missileup_sprites,True)
        for hit in hits:
            player.missile += 1
            missileup_sound.play()

        # player hit enemy1
        hits = pygame.sprite.spritecollide(player,enemy1_sprites,False,pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center,'large')
            explodebg_sound.play()
            all_sprites.add(expl)
            player.ph -= enemy1.ph
            enemy1.ph = 0
        # player hit enemy2
        hits = pygame.sprite.spritecollide(player,enemy2_sprites,False,pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center,'large')
            explodebg_sound.play()
            all_sprites.add(expl)
            player.ph -= enemy2.ph
            enemy2.ph = 0
        # player hit enemy3
        hits = pygame.sprite.spritecollide(player,enemy3_sprites,False,pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center,'large')
            explodebg_sound.play()
            all_sprites.add(expl)
            player.ph -= enemy3.ph
            enemy3.ph = 0
        # mybullet hit enemy1
        hits = pygame.sprite.groupcollide(bullet_sprites,enemy1_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            enemy1.drawph = True
            enemy1.ph -= 10
        # mybullet hit enemy2
        hits = pygame.sprite.groupcollide(bullet_sprites,enemy2_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            enemy2.drawph = True
            enemy2.ph -= 10
        # mybullet hit enemy3
        hits = pygame.sprite.groupcollide(bullet_sprites,enemy3_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            enemy3.drawph = True
            enemy3.ph -= 10
        # missile hit enemy1
        hits = pygame.sprite.groupcollide(missile_sprites,enemy1_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            enemy1.drawph = True
            enemy1.ph -= 700
        # missile hit enemy2
        hits = pygame.sprite.groupcollide(missile_sprites,enemy2_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            enemy2.drawph = True
            enemy2.ph -= 700
        # missile hit enemy3
        hits = pygame.sprite.groupcollide(missile_sprites,enemy3_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            enemy3.drawph = True
            enemy3.ph -= 700
        # regenerate enemy1
        if enemy1.ph <= 0:
            newbulletup()
            player.score += 100
            enemy1 = newenemy1()
        if enemy1.rect.top > height:
            enemy1 = newenemy1()
        # regenerate enemy2
        if enemy2.ph <= 0:
            newspeedup()
            player.score += 100
            enemy2 = newenemy2()
        if enemy2.rect.top > height:
            enemy2 = newenemy2()
        # regenerate enemy3
        if enemy3.ph <= 0:
            newhealthup()
            newmissileup()
            player.score += 100
            enemy3 = newenemy2()
        if enemy3.rect.top > height:
            enemy3 = newenemy3()

        # roundbullet hit player
        hits = pygame.sprite.spritecollide(player,roundbullet_sprites,True)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            player.ph -= 10
        # laser1 hit player
        hits = pygame.sprite.spritecollide(player,laser1_sprites,True)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            player.ph -= 20
        # dart hit player
        hits = pygame.sprite.spritecollide(player,dart_sprites,True)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            player.ph -= 30
        # x hit player
        hits = pygame.sprite.spritecollide(player,x_sprites,True)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            player.ph -= 35

        # roundbullet hit shield
        hits = pygame.sprite.groupcollide(shield_sprites,roundbullet_sprites,False,True,pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion((hit.rect.centerx,hit.rect.centery-50),'small')
            explodesm_sound.play()
            all_sprites.add(expl)
        # laser1 hit shield
        hits = pygame.sprite.groupcollide(shield_sprites,laser1_sprites,False,True,pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion((hit.rect.centerx,hit.rect.centery-50),'small')
            explodesm_sound.play()
            all_sprites.add(expl)
        # dart hit shield
        hits = pygame.sprite.groupcollide(shield_sprites,dart_sprites,False,True,pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
        # x hit shield
        hits = pygame.sprite.groupcollide(shield_sprites,x_sprites,False,True,pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)


        # player hit boss1
        hits = pygame.sprite.spritecollide(player,boss1_sprites,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'large')
            explodebg_sound.play()
            all_sprites.add(expl)
            hurt = boss1.ph
            boss1.ph -= player.ph
            player.ph -= hurt
            boss1.drawph = True
        # player hit boss2
        hits = pygame.sprite.spritecollide(player,boss2_sprites,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'large')
            explodebg_sound.play()
            all_sprites.add(expl)
            hurt = boss2.ph
            boss2.ph -= player.ph
            player.ph -= hurt
            boss2.drawph = True
        # player hit boss3
        hits = pygame.sprite.spritecollide(player,boss3_sprites,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'large')
            explodebg_sound.play()
            all_sprites.add(expl)
            hurt = boss3.ph
            boss3.ph -= player.ph
            player.ph -= hurt
            boss3.drawph = True
        # mybullet hit boss1
        hits = pygame.sprite.groupcollide(bullet_sprites,boss1_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            boss1.drawph = True
            boss1.ph -= 10
        # mybullet hit boss2
        hits = pygame.sprite.groupcollide(bullet_sprites,boss2_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            boss2.drawph = True
            boss2.ph -= 10
        # mybullet hit boss3
        hits = pygame.sprite.groupcollide(bullet_sprites,boss3_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'small')
            explodesm_sound.play()
            all_sprites.add(expl)
            boss3.drawph = True
            boss3.ph -= 10
        # missile hit boss1
        hits = pygame.sprite.groupcollide(missile_sprites,boss1_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            boss1.drawph = True
            boss1.ph -= 700
        # missile hit boss2
        hits = pygame.sprite.groupcollide(missile_sprites,boss2_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            boss2.drawph = True
            boss2.ph -= 700
        # missile hit boss3
        hits = pygame.sprite.groupcollide(missile_sprites,boss3_sprites,True,False)
        for hit in hits:
            expl = Explosion(hit.rect.center,'death')
            explodedeath_sound.play()
            all_sprites.add(expl)
            boss3.drawph = True
            boss3.ph -= 700

        try:
            # boss1 die generate boss2
            if boss1.ph <= 0:
                count1 += 2
                newbulletup()
                newspeedup()
                newliveup()
                boss2 = newboss2()
                boss2.ph *= count1
                boss2.fullph *= count1
                boss1.drawph = False
                expl = Explosion(boss1.rect.center,'death')
                explodedeath_sound.play()
                all_sprites.add(expl)
                boss1.kill()
                boss1.ph = 1
            # boss2 die generate boss3
            if boss2.ph <= 0:
                count1 += 2
                newbulletup()
                newspeedup()
                newliveup()
                boss3 = newboss3()
                boss3.ph *= count1
                boss3.fullph *= count1
                boss2.drawph = False
                expl = Explosion(boss2.rect.center,'death')
                explodedeath_sound.play()
                all_sprites.add(expl)
                boss2.kill()
                boss2.ph = 1
            # boss3 die generate boss1
            if boss3.ph <= 0:
                count1 += 2
                newbulletup()
                newspeedup()
                newliveup()
                boss1 = newboss1()
                boss1.ph *= count1
                boss1.fullph *= count1
                boss3.drawph = False
                expl = Explosion(boss3.rect.center,'death')
                explodedeath_sound.play()
                all_sprites.add(expl)
                boss3.kill()
                boss3.ph = 1
        except:
            pass



        #******draw******
        screen.blit(background,(0,0))
        all_sprites.draw(screen)
        health(player.ph,50,50)
        drawlive(player.live,50,100)
        drawscore(player.score,width/2-50,45)
        drawshield(player.shield,50,width-250)
        drawmissile(player.missile,50,width-200)
        # draw enemy1 ph
        try:
            if enemy1.drawph:
                enemy1.enemy_health(enemy1.ph, enemy1.fullph, width - 200, 50)
        except:
            pass
        # draw enemy2 ph
        try:
            if enemy2.drawph:
                enemy2.enemy_health(enemy2.ph, enemy2.fullph, width - 200, 50)
        except:
            pass
        # draw enemy3 ph
        try:
            if enemy3.drawph:
                enemy3.enemy_health(enemy3.ph, enemy3.fullph, width - 200, 50)
        except:
            pass
        # draw boss1 ph
        try:
            if boss1.drawph:
                boss1.enemy_health(boss1.ph, boss1.fullph, width - 200, 50)
        except:
            pass
        # draw boss2 ph
        try:
            if boss2.drawph:
                boss2.enemy_health(boss2.ph, boss2.fullph, width - 200, 50)
        except:
            pass
        # draw boss3 ph
        try:
            if boss3.drawph:
                boss3.enemy_health(boss3.ph, boss3.fullph, width - 200, 50)
        except:
            pass

        pygame.display.update()



intro()
quitgame()
