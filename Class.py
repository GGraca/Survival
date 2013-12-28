import sys, random
from pygame.locals import *
from pygame import *
from Vars import *
from math import *


class Individuo:

	def __init__(self, x, y, color, size  = 10):
		self.size = size
		self.x = x
		self.y = y
		self.t_x = 0
		self.t_y = 0
		self.energia = random.randint(200,300)
		self.color = color
		self.dir = 0.0
		self.t_parado = 0

	def get_x_y(self):
		return int(self.x), int(self.y)

	def get_t_x_y(self):
		return int(self.t_x), int(self.t_y)

	def set_x_y(self, x, y):
		self.x = x
		self.y = y

	def set_t_x_y(self, x, y):
		self.t_x = x
		self.t_y = y
		
	def paint(self):
		draw.circle(windowSurface, self.color, self.get_x_y(), self.size, 0)

	def paint_tr(self, size, v_w = -1):
		if(v_w == -1):
			draw.circle(tranSurface, self.color, self.get_x_y(), size, 0)
		else:
			draw.polygon(tranSurface, self.color, (self.get_x_y(), ponto(self.get_x_y(), size, self.dir + v_w),ponto(self.get_x_y(), size, self.dir - v_w)), 0)

	def olfato(self, al, o_range):
		dist_min = 10000
		target_x = -1
		target_y = -1
		for a in al:
			for i in a.populacao:
				d = distancia(self.get_x_y(), i.get_x_y())
				if(d <= o_range) & (d <= dist_min):
					dist_min = d
					target_x = i.x
					target_y = i.y
		return target_x, target_y, dist_min

	def visao(self, al, v_range, v_w):
		dist_min = 10000
		target_x = -1
		target_y = -1
		for a in al:
			for i in a.populacao:
				dis = distancia(self.get_x_y(), i.get_x_y())
				delta = f_atan(self.get_x_y(), i.get_x_y())
				if(dis <= v_range) & (dis <= dist_min):
					if(delta <= self.dir + v_w) & (delta >= self.dir - v_w):
						dist_min = dis
						target_x = i.x
						target_y = i.y
		return target_x, target_y, dist_min

	def mov(self, en, speed):
		enimigo = False
		for e in en:
			for i in e.populacao:
				d = distancia(self.get_x_y(), i.get_x_y())
				if(d < 50):
					enimigo = True
		if(self.t_x != -1) or (self.t_y != -1):
		
			delta = f_atan(self.get_x_y(),self.get_t_x_y())

			if enimigo == False:
				self.x = self.x + (speed * cos(delta))
				self.y = self.y + (speed * sin(delta))
			else:
				self.x = self.x + (speed * 1.5 * cos(delta))
				self.y = self.y + (speed * 1.5 * sin(delta))

			self.dir = delta

	def nom(self, al, n_range):
		for a in al:
			for i in a.populacao:
				d = distancia(self.get_x_y(), i.get_x_y())
				if(d < n_range):
					a.populacao.remove(i)
					self.energia = self.energia + 50


class Especie:

	def __init__(self, alimento, enimigo, color, speed, o_range, v_range, v_w, populacao_inicial = 10, size = 10):
		self.size = size
		self.populacao_inicial = populacao_inicial
		self.populacao = []
		self.color = color
		self.alimento = alimento
		self.enimigo = enimigo

		self.speed = speed
		self.olf_range = o_range
		self.vis_range = v_range
		self.vis_w = v_w
		

		for a in range(0,self.populacao_inicial):
			self.spawn()
		

	def spawn(self, x = -1, y = -1):
		if(x == -1) & (y == -1):
			i = Individuo(random.randint(0, max_x), random.randint(0, max_y), self.color, self.size)
		else:
			i = Individuo(x, y, self.color, self.size)
		
		self.populacao.append(i)

	def paint(self):
		for i in self.populacao:
			i.paint()

	def paint_tr(self, on = False):
		if(on == True):
			for i in self.populacao:
				i.paint_tr(self.olf_range)
				i.paint_tr(self.vis_range, self.vis_w)

	def choose_path(self):
		for i in self.populacao:
			
			i.energia = i.energia - 1
			
			if(i.t_x == -1) or (i.t_y == -1):
				i.t_parado = i.t_parado + 1
				if(i.t_parado > 20):
					i.dir = (random.random() - 0.5) * 2 * pi

			if(i.energia <= 0):
				self.populacao.remove(i)

			#elif(i.energia <= 100):

			#elif(i.energia <= 200):

			#elif(i.energia <= 300):

			#elif(i.energia <= 400):

			#elif(i.energia <= 500):

			elif(i.energia > 500):
				i.set_t_x_y(-1, -1)
				self.spawn(i.x, i.y)
				i.energia = i.energia - 200

			else:

				t_o_x, t_o_y, t_o_d = i.olfato(self.alimento, self.olf_range)
				t_v_x, t_v_y, t_v_d = i.visao(self.alimento, self.vis_range, self.vis_w)


				if(t_o_d > t_v_d):
					i.set_t_x_y(t_v_x, t_v_y)

				elif(t_o_d < t_v_d):
					i.set_t_x_y(t_o_x, t_o_y)

				else:
					i.set_t_x_y(-1, -1)



			i.mov(self.enimigo, self.speed)
			i.nom(self.alimento, self.size - 2)