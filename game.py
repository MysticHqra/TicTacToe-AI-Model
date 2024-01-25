import random
import time

game_state = True
player_id = 1
opponent_type = ""
draw = False
player_type = {1: "", 2: ""}
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
def otherPlayer():
    if player_id == 1:
        return 2
    elif player_id == 2:
        return 1
    else:
        return 0

def otherPlayerType():
    if player_type[player_id] == "X":
        return "O"
    elif player_type[player_id] == "O":
        return "X"
    else:
        return 0

def printBoard():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

#Returns an integer from -6 (worst case) to 5 (best case)
def winningChance(player_id):
    count_item = 0
    player_winning_states = []
    for x in winning_states:
        temp = 0
        for y in x:
            row, col = y
            if board[row][col] == player_type[player_id]:
                temp += 2
            elif board[row][col] == "_":
                temp += 1
            elif board[row][col] == player_type[otherPlayer()]:
                temp -= 2
        if temp > count_item:
            count_item = temp
            player_winning_states.clear()
            player_winning_states.append(x)
        elif temp == count_item:
            count_item = temp
            player_winning_states.append(x)
    return count_item, player_winning_states

#playCountAI = 0
def aiPlay():
    '''
        #First I tried to make the AI play in random slots of the board
        #but it was not a good way for the AI to play, so I discarded this logic
        #feel free to check it out though

            freeSlots = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == "_":
                    freeSlots.append((x,y))
        if playCountAI == 0:
            row, col = random.choice(freeSlots)
            board[row][col] = player_type[player_id]
            playCountAI += 1
        freeState = []
        for x in winning_states:
            playerItem = 0
            for y in x:
                row, col = y
                if player_type[1] in board[row][col]:
                    playerItem += 1
            if playerItem == 0:
                freeState.append(x)
        if len(freeState) != 0:
            playStyle = random.choice(freeState)
            row, col = random.choice(playStyle)
            board[row][col] = player_type[player_id]
            playCountAI += 1
        '''

    print("AI is thinking...")
    count_item, player_winning_states = winningChance(otherPlayer())
    ai_count_item, ai_winning_states = winningChance(player_id)
    freeSlots = []

    if ai_count_item >= 5:
 #       print("AI leading so trying to win")
        for x in ai_winning_states:
            for y in x:
                a, b = y
                if board[a][b] == "_":
                    freeSlots.append(y)
    else:
 #       print("Player leading so trying to stop them from winning")
        for x in player_winning_states:
            for y in x:
                a, b = y
                if board[a][b] == "_":
                    freeSlots.append((a, b))
        if len(freeSlots) == 0:
            for x in ai_winning_states:
                for y in x:
                    a, b = y
                    if board[a][b] == "_":
                        freeSlots.append(y)

    row, col = random.choice(freeSlots)
    board[row][col] = player_type[player_id]

    time.sleep(random.randint(1, 3))
    printBoard()

def playerPlay():
    pos = int(input(
        "Input where you want to place " + player_type[player_id] + " for player " + str(player_id) + " [0-8]: "))

    row, col = 0, 0
    if 0 <= pos <= 2:
        row = 0
        col = pos
    elif 3 <= pos <= 5:
        row = 1
        col = pos - 3
    elif 6 <= pos <= 8:
        row = 2
        col = pos - 6
    else:
        print("Invalid input. Please try again!")
        return 0

    if board[row][col] == "_":
        board[row][col] = player_type[player_id]
    else:
        print("Invalid position, please try again!")
        return 0

    printBoard()

print("""
1. Play against a player
2. Play against the computer
""")
opponent_choice = int(input("Enter your choice (1/2): "))
if opponent_choice == 1:
    opponent_type = "P"
elif opponent_choice == 2:
    opponent_type = "C"
else:
    print("Invalid choice, game ending now.")
    game_state = False
    quit()

# Choosing X or O for PLAYER 1
choice = input("Input TYPE for PLAYER " + str(player_id) + " (X/O): ")
if choice == "X":
    player_type[player_id] = "X"
    player_type[otherPlayer()] = "O"
elif choice == "O":
    player_type[player_id] = "O"
    player_type[otherPlayer()] = "X"
else:
    print("Invalid choice! Game will end now.")
    quit()


printBoard()
# Main game logic
while game_state:
    if player_id == 1:
        status = playerPlay()
        if status == 0:
            continue

    elif player_id == 2:
        if opponent_type == "P":
            status = playerPlay()
            if status == 0:
                continue
        elif opponent_type == "C":
            aiPlay()
        else:
            game_state = False
            quit()
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
            print("PLAYER", player_id, "(" + player_type[player_id] + ")", "HAS WON THE GAME!")
            game_state = False

    # DRAW condition game logic
    for x in board:
        if "_" in x:
            draw = False
            break
        else:
            draw = True
    if draw:
        print("GAME IS A DRAW!")
        game_state = False

    # Switching play chance to other player if the game is not over
    if otherPlayer() != 0:
        player_id = otherPlayer()
    else:
        print("Invalid player id")
        game_state = False
        quit()

print("TicTacToe by Hara <3")