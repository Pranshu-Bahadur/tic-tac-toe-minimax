from math import inf
import copy

class MinimaxAlphaBetaAgent():

	def __init__(self):
		return
	
	def staticEval(self, state):
		return state.score

	def minimax_alpha_beta(self, state, depth, alpha, beta, isMax):
		if state.gameOver() or depth is 0:
			return -1, state.score() - depth
		if isMax:
			bestValue = -1, -inf
		else:
			bestValue = -1, inf

		for s in self.get_all_next_moves(state):
			if isMax:
				state.move('X', s)
				value = s, max(bestValue[1], self.minimax_alpha_beta(state, depth - 1, alpha, beta, False)[1])
				state.undo_move('X', s)

				if value[1] > bestValue[1]:
					bestValue = value
				
				alpha = max(alpha, value[1])
				if alpha >= beta:
					return s, alpha
				
			else:
				state.move('O', s)
				value = s, min(bestValue[1], self.minimax_alpha_beta(state, depth - 1, alpha, beta, True)[1])
				state.undo_move('O', s)

				if value[1] < bestValue[1]:
					bestValue = value
				
				beta = min(beta, value[1])
				if alpha >= beta:
					return s, beta
				
		return bestValue

	def choose(self, state, player):
		return self.minimax_alpha_beta(state, len(self.get_all_next_moves(state)), -inf, inf, player)

	def get_all_next_moves(self, state):
		moves = []
		for row in state.empty_tiles():
			for tile in row:
				moves.append(tile)
		return moves
