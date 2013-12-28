import sys
from pygame.locals import *
from pygame import * 
from Class import *

import random



def start():
	global windowSurface
	global max_x
	global max_y

	init()
	display.set_caption('Survival!')


def eventos():
	global tr
	for sub_event in event.get():
		if sub_event.type == QUIT:
			quit()
			sys.exit()
		if sub_event.type == KEYUP:
			if sub_event.key == K_SPACE:
				tr = not tr

def debug(txt):
	global windowSurface
	global basicFont

	text = basicFont.render(txt, True, WHITE, BLUE)
	textRect = text.get_rect()
	textRect.centerx = windowSurface.get_rect().centerx
	textRect.centery = windowSurface.get_rect().centery
	windowSurface.blit(text, textRect)

def add_prod():
	Plantas.spawn()

def paint():
	global tr
	windowSurface.fill(BLACK)
	tranSurface.fill(BLACK)
	

	#Transparentes
	Herbivoros.paint_tr(tr)
	#Omnivoros.paint_tr(tr)
	Predador.paint_tr(tr)
	windowSurface.blit(tranSurface, (0,0))

	#Normal
	Plantas.paint()
	Herbivoros.paint()
	#Omnivoros.paint()
	Predador.paint()

def choose_path():
	Herbivoros.choose_path()
	#Omnivoros.choose_path()
	Predador.choose_path()



start()

segundo_1 = 0
segundo_10 = 0

basicFont = pygame.font.SysFont(None, 48)



Plantas = Especie([],[], GREEN, 0, 0, 0, 0, 0, 5)
Herbivoros = Especie([Plantas],[], BLUE, 10, 100, 500, pi/12, 10, 10)

#Omnivoros = Especie([Plantas, Herbivoros],[], RED, 6, 100, 500, pi/12, 5, 10)
Predador = Especie([Herbivoros],[], WHITE, 8, 100, 500, pi/12, 2, 10)

#Herbivoros.enimigo = [Predador]


while True:

	segundo_1 = segundo_1 + time.Clock().get_time()
	segundo_10 = segundo_10 + time.Clock().get_time()
 
	#time.Clock().get_time()
	time.Clock ().tick(60)

	if(segundo_10 >= 1):
		choose_path()
		segundo_10 = 0

	if(segundo_1 >= 2):
		add_prod()
		segundo_1 = 0

	
	paint()
	display.update()
	eventos()
