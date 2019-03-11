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
		player = True
		while not self.model.gameOver() or self.quit:
			for event in self.view.pygame.event.get():
				
				if event.type is self.view.pygame.QUIT or event.type is 2:
					self.quit = True
					pygame.quit()
					quit()
					break
				if event.type is self.view.pygame.MOUSEBUTTONDOWN:
					self.move()
			self.view.draw(self.model)
			self.view.pygame.display.update()
			self.view.clock.tick(60)

	def move(self):
		mouse = pygame.mouse.get_pos()
		for pos in range(1, len(self.view.positions) + 1):
			position = self.view.positions[pos]
			if position[0][0] + 200 >= mouse[0] >= position[0][0] and position[0][1] + 200 >= mouse[1] >= position[0][1]:
				if pos in self.agent.get_all_next_moves(self.model):
					self.model.move('X', pos)
					if len(self.agent.get_all_next_moves(self.model)) > 0:
						move = self.agent.choose(self.model, False)[0]
						self.model.move('O', move)
					


model = Model()
view = GuiView()
agent = MinimaxAlphaBetaAgent()
controller = Controller(model, view, agent)
controller.run_game()



