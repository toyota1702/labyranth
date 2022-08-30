from pygame import *
from time import sleep

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption("Лабиринт")

background = image.load('background.jpg')
background = transform.scale(background, (win_width, win_height))

FPS = 60

#Загружаем музыку
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
######################################
clock = time.Clock()
######################################
class GameSprite(sprite.Sprite):
	def __init__(self,img,w,h,x,y,speed):
		sprite.Sprite.__init__(self)
		self.w=w 
		self.h=h 
		self.image = image.load(img)
		self.image = transform.scale(self.image, (self.w, self.h))
		self.rect = self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.speed=speed
	def reset(self):
		window.blit(self.image ,(self.rect.x, self.rect.y))
######################################

class Hero(GameSprite):
	def __init__(self,img,w,h,x,y,speed):
		GameSprite.__init__(self,img,w,h,x,y,speed)
	def update(self):
		keys = key.get_pressed()
		if keys[K_LEFT] and self.rect.x>0:
			self.rect.x-=self.speed
		elif keys[K_RIGHT] and self.rect.x+self.w<win_width:
			self.rect.x+=self.speed
		elif keys[K_UP] and self.rect.y>0:
			self.rect.y-=self.speed
		elif keys[K_DOWN] and self.rect.y+self.h<win_height:
			self.rect.y+=self.speed
######################################
class Enemy(GameSprite):
	def __init__(self,img,w,h,x,y,speed):
		GameSprite.__init__(self,img,w,h,x,y,speed)
		self.direction="left"
	def update(self):
		if self.direction=='left':
			self.rect.x-=self.speed
		elif self.direction=='right':
			self.rect.x+=self.speed
		#=====Касания стенок=======
		if self.rect.x<=0:
			self.direction='right'
		if self.rect.x+self.w>=win_width:
			self.direction='left' 
######################################

class Wall(sprite.Sprite):
	def __init__(self,x,y,width,height,col1,col2,col3):
		self.width = width
		self.height = height
		self.img = Surface([self.width,self.height]) 
		self.img.fill((col1, col2, col3))
		self.rect = self.img.get_rect() 
		self.rect.x=x
		self.rect.y=y
	def reset(self):
		window.blit(self.img ,(self.rect.x, self.rect.y))
######################################



treasure = GameSprite(img="treasure.png",w=50,h=50,x=300,y=100,speed=0)
#######################################################################
hero = Hero(img="hero_1.png",w=50,h=50,x=610,y=390,speed=1)
###########################################################
enemy = Enemy(img="cyborg.png",w=50,h=50,x=100,y=100,speed=1)
#############################################################
wall1 = Wall(x=5,y=480,width=690,height=10,col1=255,col2=0,col3=0)
##################################################################
wall2 = Wall(x=5,y=280,width=10,height=200,col1=255,col2=0,col3=0)
##################################################################
wall3 = Wall(x=685,y=80,width=10,height=400,col1=255,col2=0,col3=0)
###################################################################
wall4 = Wall(x=5,y=280,width=90,height=10,col1=255,col2=0,col3=0)
#################################################################
wall5 = Wall(x=165,y=280,width=130,height=10,col1=255,col2=0,col3=0)
####################################################################
wall6 = Wall(x=485,y=280,width=200,height=10,col1=255,col2=0,col3=0)
####################################################################
wall7 = Wall(x=485,y=280,width=10,height=140,col1=255,col2=0,col3=0)
####################################################################
wall8 = Wall(x=570,y=360,width=10,height=130,col1=255,col2=0,col3=0)
####################################################################
wall9 = Wall(x=350,y=410,width=140,height=10,col1=255,col2=0,col3=0)
####################################################################
wall10 = Wall(x=485,y=200,width=110,height=10,col1=255,col2=0,col3=0)
#####################################################################
wall11 = Wall(x=585,y=85,width=10,height=115,col1=255,col2=0,col3=0)
####################################################################
wall12 = Wall(x=85,y=170,width=10,height=115,col1=255,col2=0,col3=0)

wall13 = Wall(x=85,y=80,width=190,height=10,col1=255,col2=0,col3=0)

wall14 = Wall(x=165,y=180,width=10,height=100,col1=255,col2=0,col3=0)

wall15 = Wall(x=265,y=160,width=130,height=10,col1=255,col2=0,col3=0)

wall16 = Wall(x=385,y=160,width=10,height=175,col1=255,col2=0,col3=0)



kick = mixer.Sound('kick.ogg')
font.init()#Подключаем шрифты
font24=font.SysFont('Bold',30)#Задаем параметры шрифта
text_fail = font24.render("Террористы победили!",True,(255,0,0)) 
text_win = font24.render("Спецназы победили!",True,(0,0,255))


while True:
	window.blit(background,(0,0))
	treasure.reset()

	wall1.reset()
	wall2.reset()
	wall3.reset()
	wall4.reset()
	wall5.reset()
	wall6.reset()
	wall7.reset()
	wall8.reset()
	wall9.reset()
	wall10.reset()
	wall11.reset()
	wall12.reset()
	wall13.reset()
	wall14.reset()
	wall15.reset()
	wall16.reset()

	hero.reset()
	hero.update()
	
	enemy.reset()
	enemy.update()
	
	display.update()
	

		
	if sprite.collide_rect(hero,enemy) or sprite.collide_rect(hero,wall1) or sprite.collide_rect(hero,wall2) or sprite.collide_rect(hero,wall3) or sprite.collide_rect(hero,wall4) or sprite.collide_rect(hero,wall5) or sprite.collide_rect(hero,wall6) or sprite.collide_rect(hero,wall7) or sprite.collide_rect(hero,wall8) or sprite.collide_rect(hero,wall9) or sprite.collide_rect(hero,wall10) or sprite.collide_rect(hero,wall11) or sprite.collide_rect(hero,wall12) or sprite.collide_rect(hero,wall13) or sprite.collide_rect(hero,wall14) or sprite.collide_rect(hero,wall15) or sprite.collide_rect(hero,wall16):
		window.blit(text_fail,(320,230))
		display.update()
		sleep(3)
		kick.play()
		quit() 
	if sprite.collide_rect(hero,treasure) :
		window.blit(text_win,(320,230))
		display.update()
		sleep(3)
		quit() 
	for i in event.get(): 
		if i.type==QUIT:
			quit()

######################################
######################################
######################################
######################################
######################################
######################################
######################################
######################################
######################################
######################################
######################################