#!/usr/bin/python

# file that contain the game of life engine

from random import randrange

class World(object):

	"""World for a game of life"""


	def __init__(self, width = 20, height = 20, nbBirth = 3, neutralNumber = 2):
		"""
		Constructor of the game of life world.
		@param width The width of the board.
		@param height The Height of the board.
		@param nbBirth The number of neighbor to make the cell alive.
		@param neutralNumber The Number of neighbor cell that doesn't change the cell state.
		@param displayFunc Expect a lamda to display the world. Give it False if you want to use the built in fucntion.
		"""

		super(World, self).__init__()
		self.__board = [[randrange(100) > 50 for i in range(height)] for j in range(width)]

		#deep copy of list
		self.__nextStepBoard = [[self.__board[i][j] for j in range(len(self.__board[i]))] for i in range(len(self.__board))]
		self.__nbBirth = nbBirth
		self.__neutralNumber = neutralNumber
		self.__cellChecker = []
					




	def iterate(self):

		"""
		Make the world iterate of the number of iteration, passed in parameter.
		"""

		if self.__stillLife() == True:

			self.__cellChecker = [[False for j in range(len(self.__board[i]))] for i in range(len(self.__board))]
			for i in range(len(self.__board)):

				for j in range(len(self.__board[i])):
					self.__iterateCell(i,j)

			self.__board = [[self.__nextStepBoard[i][j] for j in range(len(self.__nextStepBoard[i]))] for i in range(len(self.__nextStepBoard))]
		else:
			exit()





	def getBoard():
		return self.__board


	def __iterateCell(self, line, column):

		"""
		Iterate this cell.
		"""

		if self.__cellChecker[line][column] == False:

			closeCell = self.__numberOfCell(line, column)
			if len(closeCell) == self.__nbBirth or len(closeCell) == self.__neutralNumber:

				if self.__board[line][column] == False:

					if len(closeCell) == self.__nbBirth:

						self.__nextStepBoard[line][column] = True

			else:	
				self.__nextStepBoard[line][column] = False

			self.__cellChecker[line][column] = True

			#check recursively the
			for nextCell in closeCell:

				self.__iterateCell(nextCell[0],nextCell[1])







	def __stillLife(self):
		for i in range(len(self.__board)):
			if True in self.__board[i]:
				return True
		return False







	def __numberOfCell(self, line, column):
		"""
		Check the number of direct cell of the location.
		"""

		closeCell = []
		for i in range(3):

			testedLine = line + (i - 1)
			if (testedLine) < len(self.__board) and testedLine >= 0:

				for j in range(3):

					testedColumn = column + (j - 1)
					if testedColumn < len(self.__board[0]) and testedColumn >= 0:

						if testedLine != line or testedColumn != column: #not the tested cell

							if self.__board[testedLine][testedColumn] == True: #meaning neighbor

								closeCell.append([testedLine, testedColumn])

		return closeCell


	def __str__(self):
		#have to find a better way
		text = ""
		for i in range(len(self.__board)):
			for j in range(len(self.__board[i])):
				if self.__board[i][j] == True:
					text += " O "
				else:
					text += "   "
			text += "\n"
		return text
