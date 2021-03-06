import main
import evaluator
from config import *
import copy

def getOpponentTileColor(tile):
	if tile == BLACK_TILE:
		return WHITE_TILE
	else:
		return BLACK_TILE

#player here will decide if its a maximizer or a minimizer
def minimax(board, player, depth, prune_depth, tile, computerTile):
	if main.getValidMoves(board, tile) == [] or depth == prune_depth:
		return evaluator.heuristic_eval(board, computerTile, getOpponentTileColor(computerTile)), None

	bestMove = (8,8) #aiween value
	if player == 0:
		bestScore = +INFINITY
	else:
		bestScore = -INFINITY

	for x,y in main.getValidMoves(board,tile):
		dupeBoard = copy.deepcopy(board)
		main.makeMove(dupeBoard, tile, x, y)
		score, bla = minimax(dupeBoard, 1-player, depth + 1, prune_depth, getOpponentTileColor(tile), computerTile)
		if player == 1:
			if ( score > bestScore ):
				bestScore = score  # max
				bestMove = (x,y)
		else:
			if ( score < bestScore ):
				bestScore = score # min
				bestMove = (x,y)

	return bestScore, bestMove