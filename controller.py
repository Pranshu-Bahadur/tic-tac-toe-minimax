from gui import GuiView
from model import Model
from minimaxAlphaBetaAgent import MinimaxAlphaBetaAgent
import pygame


class Controller:
	"""
	Represents a Controller that handles the input and output of the game.
	As well as the game loop.
	"""
	def __init__(self, model, view, agent):
		"""
		Initializes the game controller with a model view and an AI agent.
		Also, Initializes pygame.
		"""
		self.model = model
		self.view = view
		self.agent = agent
		self.quit = False

	def run_game(self):
		"""
		Main game loop of the tic-tac-toe game
		"""
		while not self.model.gameOver() or self.quit:
			for event in view.pygame.event.get():
				if event.type == view.pygame.QUIT:
					self.quit = True

			self.view.pygame.display.update()
			self.view.clock.tick(60)
		pygame.quit()
		quit()

model = Model()
view = GuiView()
agent = MinimaxAlphaBetaAgent()

controller = Controller(model, view, agent)

controller.run_game()



