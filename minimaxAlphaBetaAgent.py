from math import inf
import copy

class MinimaxAlphaBetaAgent():

	def __init__(self):
		return
	
	def staticEval(self, state):
		return state.score

	def minimax_alpha_beta(self, state, depth, alpha, beta, isMax):
		if state.gameOver() or depth is 0:
			return 0, self.staticEval(state)
		if isMax:
			value = 0, -inf
		else:
			value = 0, inf

		for s in self.get_all_next_moves(state):
			if isMax:
				value = s, max(value[1], self.minimax_alpha_beta(state, depth - 1, alpha, beta, False)[1])
				alpha = max(alpha, value[1])
				if alpha >= beta:
					return s, alpha
			else:
				value = s, min(value[1], self.minimax_alpha_beta(state, depth - 1, alpha, beta, True)[1])
				beta = s, min(beta, value[1])
				if alpha >= beta:
					return s, beta
		return value

	def choose(self, state, player):
		return self.minimax_alpha_beta(state, state.depth, -inf, inf, player)

	def get_all_next_moves(self, state):
		moves = []
		for row in state.empty_tiles():
			for tile in row:
				moves.append(tile)
		return moves
