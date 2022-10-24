from connectfour import connectfour
import math

emptyboard = {
    0: [" ", " ", " ", " ", " ", " "],
    1: [" ", " ", " ", " ", " ", " "],
    2: [" ", " ", " ", " ", " ", " "],
    3: [" ", " ", " ", " ", " ", " "],
    4: [" ", " ", " ", " ", " ", " "],
    5: [" ", " ", " ", " ", " ", " "],
    6: [" ", " ", " ", " ", " ", " "]
}

game = connectfour(emptyboard, "R")


def boardNotFull(gameState):
    for column in gameState.board:
        for row in range(len(gameState.board[column])):
            if gameState.board[column][row] == " ":
                return True

    return False


while boardNotFull(game):
    print(f"Current Player: {game.currentPlayer}")

    if game.currentPlayer == "R":
        try:
            move_to_make = int(input("What move do you want to make? (1-7)\n"))
        except ValueError:
            print("Please input a number! \n")
            continue

        if (move_to_make - 1) not in range(0, 7):
            print("Not a possible move! \n")
            continue

        if " " not in game.board[move_to_make - 1]:
            print("Column full! \n")
            continue

        game = game.play(move_to_make - 1)

    else:
        move_to_make = connectfour.minimax(game, 3, True)[0]

        game = game.play(move_to_make)

    print(f"Score: {game.totalScore}")

    if game.totalScore > 999999:
        print(game)
        print("Red Player Wins!!!")
        break

    elif game.totalScore < -999999:
        print(game)
        print("Yellow Player Wins!!!")
        break

    print(game)
