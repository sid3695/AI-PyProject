import main
from config import *
def heuristic_eval(board, computerTile, playerTile):
	#determines score of an intermediate state 
	#(used in games where we cant reach the bottom)

	V = [[0 for x in range(BOARDWIDTH)] for y in range(BOARDHEIGHT)] 
	#board wights
	V[0] = [20, -3, 11, 8, 8, 11, -3, 20];
	V[1] = [-3, -7, -4, 1, 1, -4, -7, -3];
	V[2] = [11, -4, 2, 2, 2, 2, -4, 11];
	V[3] = [8, 1, 2, -3, -3, 2, 1, 8];
	V[4] = [8, 1, 2, -3, -3, 2, 1, 8];
	V[5] = [11, -4, 2, 2, 2, 2, -4, 11];
	V[6] = [-3, -7, -4, 1, 1, -4, -7, -3];
	V[7] = [20, -3, 11, 8, 8, 11, -3, 20];
	
	scores = main.getScoreOfBoard(board) 
	comTileCount = scores[computerTile]
	playTileCount = scores[playerTile]

	comFrontierCount = 0
	plaFrontierCount = 0 
	#count frontier disks
	for i in range(BOARDWIDTH):
		for j in range(BOARDHEIGHT):
			if(board[i][j] != EMPTY_SPACE):
				for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
					x, y = i,j
					x += xdirection
					y += ydirection
					if main.isOnBoard(x, y) and board[x][y] == EMPTY_SPACE:
						if(board[i][j] == computerTile):
							comFrontierCount = comFrontierCount + 1
						else:
							plaFrontierCount = plaFrontierCount + 1
						break

	if(comTileCount > playTileCount):
		p = (100.0 * comTileCount)/(comTileCount + playTileCount)
	elif(comTileCount < playTileCount):
		p = -(100.0 * playTileCount)/(comTileCount + playTileCount)
	else:
		p = 0.0

	if(comFrontierCount > plaFrontierCount):
		f = -(100.0 * comFrontierCount)/(comFrontierCount + plaFrontierCount)
	elif(comFrontierCount < plaFrontierCount):
		f = (100.0 * plaFrontierCount)/(comFrontierCount + plaFrontierCount)
	else:
		f = 0.0

	#print comFrontierCount,plaFrontierCount, comTileCount, playTileCount

	#ugly hardcoded stuff begins here
	
	#corners occupied
	comTileCount = 0
	playTileCount = 0
	if(board[0][0] == computerTile):
		comTileCount = comTileCount + 1
	elif(board[0][0] == playerTile):
		playTileCount = playTileCount + 1

	if(board[0][7] == computerTile):
		comTileCount = comTileCount + 1
	elif(board[0][7] == playerTile):
		playTileCount = playTileCount + 1

	if(board[7][0] == computerTile):
		comTileCount = comTileCount + 1
	elif(board[7][0] == playerTile):
		playTileCount = playTileCount + 1

	if(board[7][7] == computerTile):
		comTileCount = comTileCount + 1
	elif(board[7][7] == playerTile):
		playTileCount = playTileCount + 1
	c = 25 * (comTileCount - playTileCount)

	#corner proximity
	comTileCount = 0
	playTileCount = 0
	if(board[0][0] == EMPTY_SPACE):
		if(board[0][1] == computerTile):
			comTileCount += 1;
		elif(board[0][1] == playerTile):
			playTileCount += 1;
		if(board[1][1] == computerTile):
			comTileCount += 1;
		elif(board[1][1] == playerTile):
			playTileCount += 1;
		if(board[1][0] == computerTile):
			comTileCount += 1;
		elif(board[1][0] == playerTile):
			playTileCount += 1;

	if(board[0][7] == EMPTY_SPACE):
		if(board[0][6] == computerTile):
			comTileCount += 1;
		elif(board[0][6] == playerTile):
			playTileCount += 1;
		if(board[1][6] == computerTile):
			comTileCount += 1;
		elif(board[1][6] == playerTile):
			playTileCount += 1;
		if(board[1][7] == computerTile):
			comTileCount += 1;
		elif(board[1][7] == playerTile):
			playTileCount += 1;
	
	if(board[7][0] == EMPTY_SPACE):
		if(board[7][1] == computerTile):
			comTileCount += 1;
		elif(board[7][1] == playerTile):
			playTileCount += 1;
		if(board[6][1] == computerTile):
			comTileCount += 1;
		elif(board[6][1] == playerTile):
			playTileCount += 1;
		if(board[6][0] == computerTile):
			comTileCount += 1;
		elif(board[6][0] == playerTile):
			playTileCount += 1;
	
	if(board[7][7] == EMPTY_SPACE):
		if(board[6][7] == computerTile):
			comTileCount += 1;
		elif(board[6][7] == playerTile):
			playTileCount += 1;
		if(board[6][6] == computerTile):
			comTileCount += 1;
		elif(board[6][6] == playerTile):
			playTileCount += 1;
		if(board[7][6] == computerTile):
			comTileCount += 1;
		elif(board[7][6] == playerTile):
			playTileCount += 1;
	

	l = -12.5 * (comTileCount - playTileCount)

	#mobility
	#print main.getValidMoves(board, computerTile), len(main.getValidMoves(board, computerTile))
	comTileCount = len(main.getValidMoves(board, computerTile))
	playTileCount = len(main.getValidMoves(board, playerTile))
	if(comTileCount > playTileCount):
		m = (100.0 * comTileCount)/(comTileCount + playTileCount)
	elif(comTileCount < playTileCount):
		m = -(100.0 * playTileCount)/(comTileCount + playTileCount)
	else:
		m = 0.0

	d = 0
	#disk difference
	for i in range(BOARDWIDTH):
		for j in range(BOARDHEIGHT):
			if(board[i][j] == computerTile):
				d += V[i][j]
			elif(board[i][j] == playerTile):
				d -= V[i][j]
	#print 'p c l m f d', p , c , l , m , f, d
	score = (10 * p) + (801.724 * c) + (382.026 * l) + (78.922 * m) + (74.396 * f) + (10 * d)
	return score
