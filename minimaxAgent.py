from math import inf
import copy

class MinimaxAgent():

	def __init__(self):
		return
	
	def staticEval(self, state):
		return state.score

	def get_all_next_moves(self, state):
		moves = []
		for row in state.empty_tiles():
			for tile in row:
				moves.append(tile)
		return moves

	"""

	def minimax(self, state, depth, isMax):
		if state.gameOver():
			return depth - state.score()

		if isMax:
			bestVal = -inf
			for row in state.board:
				for tile in row:
					if tile["value"] is 0:
						state.move("X", tile["position"])
						bestVal = max(bestVal, self.minimax(state, depth - 1, False))
						state.undo_move('X', tile["position"])

		else:
			bestVal = inf
			for row in state.board:
				for tile in row:
					if tile["value"] is 0:
						state.move("O", tile["position"])
						bestVal = min(bestVal, self.minimax(state, depth - 1, True))
						state.undo_move('O', tile["position"])
		return bestVal


	def choose(self, state):
		bestVal = +inf
		bestMove = 0
		for row in state.board:
			for tile in row:
				if tile["value"] is 0:
					state.move("O", tile["position"])
					moveValue = self.minimax(state, len(self.get_all_next_moves(state)), False)
					state.undo_move('O', tile["position"])
					if moveValue < bestVal:
						bestMove = tile["position"]
						bestVal = bestVal
		return bestMove

	"""

	def minimax(self, state, depth, player):
		if depth == 0 or state.gameOver():
			score = state.score() - depth
			return [-1, score]

		if player:
			best = [-1, -inf]
		else:
			best = [-1, +inf]

		for move in self.get_all_next_moves(state):
			temp = 'X' if player else 'O'
			state.move(temp, move)
			score = self.minimax(state, depth - 1, not player)
			state.undo_move(temp, move)
			score[0] = move
			if player:
				if score[1] > best[1]:
					best = score  # max value
			else:
				if score[1] < best[1]:
					best = score  # min value
		return best




