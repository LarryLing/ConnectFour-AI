import math
import copy

class connectfour:
    def __init__(self, board, currentPlayer, totalScore=None):
        self.board = board
        self.currentPlayer = currentPlayer
        self.totalScore = totalScore or 0

    def __str__(self):
        board = ""
        for row in range(5, -1, -1):
            printRow = ""
            for column in self.board:
                printRow += f"({self.board[column][row]})"
            printRow += "\n"
            board += printRow
        return board

    def calculateScore(board, player):
        chart = {(1, 3): 10, (2, 2): 100, (3, 1): 1000, (4, 0): 99999999}

        score = 0

        #Vertical Checking
        for column in board:
            for row in range(len(board[column]) - 3):
                part = board[column][row:row+4]
                  
                combo = (part.count(player), part.count(" "))

                score += chart.get(combo, 0)

        #Horizontal Checking
        for column in range(len(board) - 3):
            for row in range(len(board[column])):
                if row == 0:
                    part = [board[column + i][row] for i in range(4)]

                else:
                    part = ["N" if board[column + i][row - 1] == " " else board[column + i][row] for i in range(4)]

                combo = (part.count(player), part.count(" "))

                score += chart.get(combo, 0)

        #Diagonal Right Checking
        for column in range(len(board) - 3):
            for row in range(len(board[0]) - 3):
                if row == 0:
                    part = [board[column][row]]
                    part += ["N" if board[column + i][row + i - 1] == " " else board[column + i][row + i] for i in range(1, 4)]
                  
                else:
                    part = ["N" if board[column + i][row + i - 1] == " " else board[column + i][row + i] for i in range(4)]

                combo = (part.count(player), part.count(" "))

                score += chart.get(combo, 0)

        #Diagonal Left Checking
        for column in range(6, 2, -1):
            for row in range(len(board[0]) - 3):
                if row == 0:
                    part = [board[column][row]]
                    part += ["N" if board[column - i][row + i - 1] == " " else board[column - i][row + i] for i in range(1, 4)]
                  
                else:
                    part = ["N" if board[column - i][row + i - 1] == " " else board[column - i][row + i] for i in range(4)]

                combo = (part.count(player), part.count(" "))

                score += chart.get(combo, 0)

        return score

    def play(self, xpos):
        newboard = self.board.copy()

        for row in range(len(newboard[xpos])):
            if newboard[xpos][row] == " ":
                newboard[xpos][row] = self.currentPlayer
                break

        if self.currentPlayer == "R":
            nextPlayer = "Y"
        else:
            nextPlayer = "R"

        redScore = connectfour.calculateScore(newboard, "R")
        yellowScore = connectfour.calculateScore(newboard, "Y")
      
        newScore = redScore - yellowScore

        return connectfour(newboard, nextPlayer, newScore)

    def minimax(gamestate, depth, minimizingPlayer, position = None):
        # print("-------------------------")
        # print(f"position {position}")
        # print(f"score {gamestate.totalScore}")
        if depth == 0 or abs(gamestate.totalScore) >= 999999:
            return (position, gamestate.totalScore)

        maxEval = -math.inf
        minEval = math.inf
        tupleAns = (0,0)
        
        if minimizingPlayer:
            for i in gamestate.board:
                if " " in gamestate.board[i]:
                    position = i
                        
                    dummyStateBoard = copy.deepcopy(gamestate.board)
                    
                    dummyState = connectfour(dummyStateBoard, gamestate.currentPlayer)
                    dummyState = dummyState.play(i)

                    eval = connectfour.minimax(dummyState, depth - 1, not(minimizingPlayer), position)

                    if minEval > min(minEval, eval[1]):
                        minEval = min(minEval, eval[1])
                        tupleAns = (position, minEval)
            
            # print(tupleAns)
            return tupleAns
            
        else:
            for i in gamestate.board:
                if " " in gamestate.board[i]:
                    position = i
                        
                    dummyStateBoard = copy.deepcopy(gamestate.board)
                    
                    dummyState = connectfour(dummyStateBoard, gamestate.currentPlayer)
                    dummyState = dummyState.play(i)

                    eval = connectfour.minimax(dummyState, depth - 1, not(minimizingPlayer), position)

                    if maxEval < max(maxEval, eval[1]):
                        maxEval = max(maxEval, eval[1])
                        tupleAns = (position, maxEval)

            # print(tupleAns)
            return tupleAns