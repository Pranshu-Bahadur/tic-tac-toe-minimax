import pygame
from model import Model
import sys

#REMEMBER TO ADD COMMENTS AS YOU GO!

class GuiView():
	"""
	Represents the gui view of the Tic-Tac-Toe game.
	"""
	def __init__(self):
		"""
		Initilizes pygame, size of the game screen
		"""
		self.pygame = pygame
		self.pygame.init()
		#self.display = pygame.display.set_mode((500, 500))
		self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
		self.pygame.display.set_caption('Tic Tac Toe')
		self.display.fill(pygame.Color(255,235,215))
		self.clock = pygame.time.Clock()
		self.positions= {
		#Row 1:
		1: [[640 ,240], [840, 240], [640, 440], [840, 440]],
		2: [[840 ,240], [1040, 240], [840, 440], [1040, 440]],
		3: [[1040 ,240], [1240, 240], [1040, 440], [1240, 440]],
		#Row 2:
		4: [[640 ,440], [840, 440], [640, 640], [840, 640]],
		5: [[840 ,440], [1040, 440], [840, 640], [1040, 640]],
		6: [[1040 ,440], [1240, 440], [1040, 640], [1240, 640]],
		#Row 3:
		7: [[640 ,640], [840, 640], [640, 840], [840, 840]],
		8: [[840 ,640], [1040, 640], [840, 840], [1040, 840]],
		9: [[1040 ,640], [1240, 640], [1040, 840], [1240, 840]],
		}


	def draw(self, state):
		"""
		Draws the current state of the game on to the screen.
		"""
		for row in state.board:
			for tile in row:
				if tile["value"] is not 0:
					position = self.positions[tile["position"]]
					if tile["value"] is 1:
						pygame.draw.line(self.display, (0, 0, 0), [position[0][0] + 25, position[0][1] + 25], [position[3][0] - 25, position[3][1] - 25], 5)
						pygame.draw.line(self.display, (0, 0, 0), [position[1][0] - 25, position[1][1] + 25], [position[2][0] + 25, position[2][1] - 25], 5)
					else:
						center = [int(sum([position[0][0]*0.25, position[1][0]*0.25, position[2][0]*0.25, position[3][0]*0.25])),
						int(sum([position[0][1]*0.25, position[1][1]*0.25, position[2][1]*0.25, position[3][1]*0.25]))] 
						pygame.draw.circle(self.display, (0, 0, 0), center, 75, 5)

	def draw_start_menu(self):
		self.display.fill((255, 255, 215))
		mouse = self.pygame.mouse.get_pos()
		font = self.pygame.font.SysFont('Comic Sans MS', 48)
		introText = font.render("Tic-Tac-Toe:", True, (0, 0, 0))
		self.display.blit(introText, (740, 440))
		if 790 + 100 >= mouse[0] >= 790 and 540 + 50 >= mouse[1] >= 540:
			font = self.pygame.font.SysFont('Comic Sans MS', 40)
			introText = font.render("v/s Player", True, (0, 0, 0))
			self.display.blit(introText, (790, 540))
			font = self.pygame.font.SysFont('Comic Sans MS', 30)
			introText = font.render("v/s Computer", True, (0, 0, 0))
			self.display.blit(introText, (790, 640))
		elif 790 + 100 >= mouse[0] >= 790 and 640 + 50 >= mouse[1] >= 640:
			font = self.pygame.font.SysFont('Comic Sans MS', 30)
			introText = font.render("v/s Player", True, (0, 0, 0))
			self.display.blit(introText, (790, 540))
			font = self.pygame.font.SysFont('Comic Sans MS', 40)
			introText = font.render("v/s Computer", True, (0, 0, 0))
			self.display.blit(introText, (790, 640))
		else:
			font = self.pygame.font.SysFont('Comic Sans MS', 30)
			introText = font.render("v/s Player", True, (0, 0, 0))
			self.display.blit(introText, (790, 540))
			introText = font.render("v/s Computer", True, (0, 0, 0))
			self.display.blit(introText, (790, 640))


	def draw_win_state(self, player):
		self.display.fill((255, 255, 215))
		mouse = self.pygame.mouse.get_pos()
		font = self.pygame.font.SysFont('Comic Sans MS', 48)
		introText = font.render("Winner is {} !!!".format(player), True, (0, 0, 0))
		self.display.blit(introText, (740, 440))
		if 790 + 100 >= mouse[0] >= 790 and 540 + 50 >= mouse[1] >= 540:
			font = self.pygame.font.SysFont('Comic Sans MS', 40)
			introText = font.render("Menu", True, (0, 0, 0))
			self.display.blit(introText, (790, 540))
			font = self.pygame.font.SysFont('Comic Sans MS', 30)
			introText = font.render("Exit", True, (0, 0, 0))
			self.display.blit(introText, (790, 640))
		elif 790 + 100 >= mouse[0] >= 790 and 640 + 50 >= mouse[1] >= 640:
			font = self.pygame.font.SysFont('Comic Sans MS', 30)
			introText = font.render("Menu", True, (0, 0, 0))
			self.display.blit(introText, (790, 540))
			font = self.pygame.font.SysFont('Comic Sans MS', 40)
			introText = font.render("Exit", True, (0, 0, 0))
			self.display.blit(introText, (790, 640))
		else:
			font = self.pygame.font.SysFont('Comic Sans MS', 30)
			introText = font.render("Menu", True, (0, 0, 0))
			self.display.blit(introText, (790, 540))
			introText = font.render("Exit", True, (0, 0, 0))
			self.display.blit(introText, (790, 640))


	def draw_grid(self):
		"""
		Draws the background grid on the screen.
		"""
		pygame.draw.line(self.display, (0, 0, 0), [840, 240], [840, 840], 5)
		pygame.draw.line(self.display, (0, 0, 0), [1040, 240], [1040, 840], 5)
		pygame.draw.line(self.display, (0, 0, 0), [640, 440], [1240, 440], 5)
		pygame.draw.line(self.display, (0, 0, 0), [640, 640], [1240, 640], 5)

