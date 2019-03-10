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

		"""
		pygame.__init__("Tic-Tac-Toe")

		self.WIDTH = 500
		self.HEIGHT = 500

		background = pygame.Surface(ttt.get_size())
		background = background.convert()
		background.fill ((250, 250, 250))

		# draw the grid lines
		# vertical lines...
		pygame.draw.line (background, (0,0,0), (100, 0), (100, 300), 2)
		pygame.draw.line (background, (0,0,0), (200, 0), (200, 300), 2)

		# horizontal lines...
		pygame.draw.line (background, (0,0,0), (0, 100), (300, 100), 2)
		pygame.draw.line (background, (0,0,0), (0, 200), (300, 200), 2)


		# return the board
		#return background
		"""
		self.pygame = pygame
		self.pygame.init()
		self.display = pygame.display.set_mode((300, 325))
		self.pygame.display.set_caption('Tic Tac Toe')
		self.clock = pygame.time.Clock()


	def draw(self, state):
		"""
		Draws the current state of the game on to the screen.
		"""
		return


	def mouse_input(self, state):
		"""
		Returns a mosue input position based on the player's mouse click.
		param: 
			- state: current state of the game.
		return: position as an integer
		"""
		return

