import pygame
from math import * 

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)
ORANGE = (255, 255, 0)
PINK = (255, 0, 255)
OTHER = (0, 100, 200)

max_x = 1000
max_y = 700

windowSurface = pygame.display.set_mode((max_x, max_y), 0, 32)
tranSurface = pygame.Surface((max_x, max_y))
tranSurface.set_alpha(10)

tr = False

def graus_rad(graus):
	return pi * graus / 180.0

def rad_graus(rad):
	return 180 * rad / pi

def distancia(pos_a, pos_b):
	xa = pos_a[0]
	ya = pos_a[1]
	xb = pos_b[0]
	yb = pos_b[1]

	dx = abs(xa - xb)
	dy = abs(ya - yb)
	dx = dx * dx
	dy = dy * dy
	valor = dx + dy
	valor = valor**0.5
	return valor

def f_atan(pos_a, pos_b):
	xa = pos_a[0]
	ya = pos_a[1]
	xb = pos_b[0]
	yb = pos_b[1]

	dx = xb - xa
	dy = yb - ya
	a = atan2(dy,dx)
	return a

def ponto(pos_a, dist, delta):
	xa = pos_a[0]
	ya = pos_a[1]

	x = cos(delta) * dist
	y = sin(delta) * dist

	x = xa + x
	y = ya + y
	


	return x, y


