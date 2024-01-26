import random
import time

game_state = True
draw = False
player_id = 0
player_item_type = {1: "", 2: ""}
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]
winning_states = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

move_sequence = []
move_count = {1: 0, 2: 0}

def initialise():
    global game_state
    global draw
    global player_id
    global player_item_type
    global board
    global winning_states
    global move_sequence
    global move_count

    game_state = True
    draw = False
    player_id = 0
    player_item_type = {1: "", 2: ""}
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"],
    ]
    winning_states = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    move_sequence = []
    move_count = {1: 0, 2: 0}

def otherPlayer():
    if player_id == 1:
        return 2
    elif player_id == 2:
        return 1
    else:
        return 0


def otherPlayerItem():
    if player_item_type[player_id] == "X":
        return "O"
    elif player_item_type[player_id] == "O":
        return "X"
    else:
        return 0


def printBoard():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
    print()


# Returns an integer from -6 (worst case) to 5 (best case)
def getWinningStates(player_id):
    count_item = 0
    player_winning_states = []
    for x in winning_states:
        temp = 0
        for y in x:
            row, col = y
            if board[row][col] == player_item_type[player_id]:
                temp += 2
            elif board[row][col] == "_":
                temp += 1
            elif board[row][col] == player_item_type[otherPlayer()]:
                temp -= 2
        if temp > count_item:
            count_item = temp
            player_winning_states.clear()
            player_winning_states.append(x)
        elif temp == count_item:
            count_item = temp
            player_winning_states.append(x)
    return count_item, player_winning_states


def aiPlay():
    print("AI", player_id, "(" + player_item_type[player_id] + ") is thinking...")
    player_count_item, player_winning_states = getWinningStates(otherPlayer())
    ai_count_item, ai_winning_states = getWinningStates(player_id)
    freeSlots = []

    if ai_count_item >= 5:
        #       print("AI leading so trying to win")
        for x in ai_winning_states:
            for y in x:
                a, b = y
                if board[a][b] == "_":
                    freeSlots.append(y)
    elif player_count_item >= 5:
        #       print("Player leading so trying to stop them from winning")
        for x in player_winning_states:
            for y in x:
                a, b = y
                if board[a][b] == "_":
                    freeSlots.append((a, b))
    else:
        for x in ai_winning_states:
            for y in x:
                a, b = y
                if board[a][b] == "_":
                    freeSlots.append(y)

    if len(freeSlots) == 0:
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == "_":
                    freeSlots.append((x, y))

    row, col = random.choice(freeSlots)
    board[row][col] = player_item_type[player_id]

    move_sequence.append((row, col))
    move_count[player_id] += 1

    printBoard()
def play_game():
    # Main game logic
    global game_state
    global player_id
    while game_state:
        if player_id == 1:
            aiPlay()

        elif player_id == 2:
            aiPlay()
        else:
            print("Invalid player id")
            game_state = False
            quit()

        # checking each time for game win logic
        for x in winning_states:
            count_x = 0
            count_o = 0
            for y in x:
                a, b = y
                if board[a][b] == "X":
                    count_x += 1
                if board[a][b] == "O":
                    count_o += 1
            if count_x == 3 or count_o == 3:
                print("AI", player_id, "(" + player_item_type[player_id] + ")", "HAS WON THE GAME!")
                game_state = False
                break

        # DRAW condition check game logic
        for x in board:
            if "_" in x:
                draw = False
                break
            else:
                draw = True
        if draw:
            print("GAME IS A DRAW!")
            game_state = False
            break

        # Switching play chance to other player if the game is not over
        if otherPlayer() != 0:
            player_id = otherPlayer()
        else:
            print("Invalid player id")
            game_state = False
            quit()
    print("Moves list:", move_sequence)
    print("Moves count", move_count)
    print()

while True:
    initialise()
    printBoard()
    player_id = random.randint(1, 2)
    player_item_type[player_id] = random.choice(["X", "O"])
    player_item_type[otherPlayer()] = otherPlayerItem()
    print("AI", player_id, " is starting first and has chosen " + player_item_type[player_id])
    play_game()
    break

print("TicTacToe by Hara <3")