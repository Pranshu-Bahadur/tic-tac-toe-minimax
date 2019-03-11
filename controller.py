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
		self.ai = False
		self.player = True



	def run_intro(self):
		"""
		Start menu of the tic tac toe game.
		"""

		intro = True
		while intro:
			for event in self.view.pygame.event.get():
				if event.type is self.view.pygame.QUIT or event.type is 2:
					intro = False
					pygame.quit()
					quit()
					break
				if event.type is self.view.pygame.MOUSEBUTTONDOWN:
					mouse = self.view.pygame.mouse.get_pos()
					if 790 + 200 >= mouse[0] >= 790 and 540 + 30 >= mouse[1] >= 540:
						intro = False
						self.view.display.fill((255, 255, 215))
						self.run_game()
					if 790 + 200 >= mouse[0] >= 790 and 640 + 30 >= mouse[1] >= 640:
						intro = False
						self.view.display.fill((255, 255, 215))
						self.ai = True
						self.run_game()
			self.view.draw_start_menu()
			self.view.pygame.display.update()
			self.view.clock.tick(60)


	def run_game(self):
		"""
		Main game loop of the tic-tac-toe game
		"""
		self.view.draw_grid()
		while not self.model.gameOver() or self.quit:
			for event in self.view.pygame.event.get():
				if event.type is self.view.pygame.QUIT or event.type is 2:
					self.quit = True
					pygame.quit()
					quit()
					break
				if event.type is self.view.pygame.MOUSEBUTTONDOWN:
					if self.ai:
						self.move_AI()
					else:
						self.move()
						self.player = not self.player
			self.view.draw(self.model)
			self.view.pygame.display.update()
			self.view.clock.tick(60)

		if self.model.gameOver():
			self.view.display.fill((255, 255, 215))
			self.run_end_game()

	def run_end_game(self):
		end_game = True
		player = "No one"

		if self.model.score() == 10:
			player = 'Player X'

		if self.model.score() == -10:
			player = 'Player O'

		while end_game:
			for event in self.view.pygame.event.get():
				if event.type is self.view.pygame.QUIT or event.type is 2:
					end_game = False
					pygame.quit()
					quit()
					break
				if event.type is self.view.pygame.MOUSEBUTTONDOWN:
					mouse = self.view.pygame.mouse.get_pos()
					if 790 + 200 >= mouse[0] >= 790 and 540 + 30 >= mouse[1] >= 540:
						end_game = False
						self.view.display.fill((255, 255, 215))
						#self.model = Model()
						self.__init__(Model(), GuiView(), MinimaxAlphaBetaAgent())
						self.run_intro()
					if 790 + 200 >= mouse[0] >= 790 and 640 + 30 >= mouse[1] >= 640:
						end_game = False
						pygame.quit()
						quit()
						break
			self.view.draw_win_state(player)
			self.view.pygame.display.update()
			self.view.clock.tick(60)




	def move(self):
		"""
		Player Input method.
		"""
		mouse = self.view.pygame.mouse.get_pos()
		for pos in range(1, len(self.view.positions) + 1):
			position = self.view.positions[pos]
			if position[0][0] + 200 >= mouse[0] >= position[0][0] and position[0][1] + 200 >= mouse[1] >= position[0][1]:
				if pos in self.agent.get_all_next_moves(self.model):
					player = 'X' if self.player else 'O'
					self.model.move(player, pos)


	def move_AI(self):
		"""
		Player Input method v/s AI
		"""
		mouse = self.view.pygame.mouse.get_pos()
		for pos in range(1, len(self.view.positions) + 1):
			position = self.view.positions[pos]
			if position[0][0] + 200 >= mouse[0] >= position[0][0] and position[0][1] + 200 >= mouse[1] >= position[0][1]:
				if pos in self.agent.get_all_next_moves(self.model):
					self.model.move('X', pos)
					if len(self.agent.get_all_next_moves(self.model)) > 0:
						move = self.agent.choose(self.model, False)[0]
						self.model.move('O', move)




