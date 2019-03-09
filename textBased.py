from model import Model
from minimaxAlphaBetaAgent import MinimaxAlphaBetaAgent
import copy

class TextView():
	def __init__(self, state):
		self.currState = state
		self.initState = state
		self.gameRepr = ""
		self.rules = ""
		self.rules +="\n\n"
		for row in self.currState.board:
			for tile in row:
				self.rules +="| {} |".format(tile["position"])
			self.rules += "\n"
		self.rules += "\n"

	def draw(self):
		"""
		Creates a text representation of the tic tac toe board, Also displays positions on the board the player can choose..
		"""
		self.gameRepr = ""		
		for row in self.currState.board:
			for tile in row:
				if tile["value"] is not 0:
					self.gameRepr +="| {} |".format('X' if tile["value"] is 1 else 'O')
				else:
					self.gameRepr +="|   |"
			self.gameRepr += "\n"
		return self.gameRepr

	def reset():
		"""
		Resets the game to its initial state.
		"""
		self.currState = self.initState

def main(view, agent):
	player = 1
	temp = ''
	while not view.currState.gameOver():
		temp = 'X' if player is 1 else 'O'
		print("=======================================================================================")
		print(view.rules)
		print("=======================================================================================\n\n")
		move = 0
		if player is 1:
			move = input("Player {}' turn:\n".format(temp))
		else:
			print("Player O's turn:")
			prev = copy.deepcopy(view.currState)
			choose = agent.choose(prev, False)
			print(choose)
			move = choose[0]
		view.currState.move(temp, int(move))
		print("=======================================================================================")
		print(view.draw())
		print(view.currState.empty_tiles())
		player = -player
	if view.currState.score is 3:
		print("Player X wins!")

	elif view.currState.score is -3:
		print("Player O wins!")

	else:
		print("It's a draw!")

game = Model()
text = TextView(game)
agent = MinimaxAlphaBetaAgent()
main(text, agent)

