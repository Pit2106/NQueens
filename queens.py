# QUEENS GAMES
# BY PETER CHICAIZA
"""
Given a N number of queen pieces you have to analyze the distribution
of this N pieces on a chessboard  of NxN dimentions. This will work with 
numbuer over 5.
"""

def locateNextQueen(row, chessboard, queens):
    """
        Recursive function that locates the queens pieces one by one
        
        Parameters
        -----------
            row: int with the current analyzed row
            queens: number of queens to be located
            chessboard: array with the positions of the queens

        Returns:
        --------
            An array with a posible solution.
    """
    col = 0
    while (col < queens and row < queens):
        chessboard.append([row, col])
        if isValidState(chessboard):
            chessboard = locateNextQueen(row+1, chessboard, queens)
            if len(chessboard) == queens:
                return chessboard
        chessboard.pop()
        col += 1
    return chessboard

def isValidState(chessboard):
    """
        It validates that the last position added to the chessboard
        doesn't belong to a piece that can be intercepted by another queen.

        Parameters
        -----------
            chessboard: array with the positions of the queens

        Returns:
        --------
            True; if the new position is valid an doesnt match the range of another queen.
            False; if the new position can be intercepted by another queen.
    """

    newQueen = chessboard[-1]
    for oldQueen in chessboard[:-1]:
        if (abs(oldQueen[0] - newQueen[0]) == abs(oldQueen[1] - newQueen[1]) or
            oldQueen[0] == newQueen[0] or oldQueen[1] == newQueen[1]):
            return False
    return True

def mainLocate(queens):
    """
        This function creates the array chessboard and initializates the 
        queens location process.

        It'll iterate until it finds a solution with the given nomber of queens.

            Parameters
            -----------
                queens: int that indicates the quantity of queens to locate on the chessboard.

            Returns:
            --------
                An array with the valid position of the queens on the board.
    """
    chessboard = []
    col = 0
    row = 0

    while(col < queens):
        chessboard.append([row, col])
        if isValidState(chessboard):
            chessboard = locateNextQueen(row+1, chessboard, queens)
            if len(chessboard) == queens:
                return chessboard
        
        chessboard.pop()
        col += 1

    return chessboard        
    
print(mainLocate(9))