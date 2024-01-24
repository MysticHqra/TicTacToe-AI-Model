game_state = True
player_id = 1
flag = False
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

for i in board:
    for j in i:
        print(j, end=" ")
    print()

# Choosing X or O for PLAYER 1
choice = input("Input TYPE for PLAYER " + str(player_id) + " (X/O): ")
if choice == "X":
    player_type[player_id] = "X"
    player_type[player_id + 1] = "O"
elif choice == "O":
    player_type[player_id] = "O"
    player_type[player_id + 1] = "X"
else:
    print("Invalid choice! Game will end now.")
    quit()

# Main game logic
while game_state:
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
        continue

    if board[row][col] == "_":
        board[row][col] = player_type[player_id]
    else:
        print("Invalid position, please try again!")
        continue

    for i in board:
        for j in i:
            print(j, end=" ")
        print()

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
            quit()

    # DRAW condition game logic
    for x in board:
        if "_" in x:
            flag = False
            break
        else:
            flag = True
    if flag:
        print("GAME IS DRAW!")
        game_state = False
        quit()

    # switching player chance if game not over
    if player_id == 1:
        player_id = 2
    elif player_id == 2:
        player_id = 1
    else:
        print("Invalid Player ID")
        game_state = False
        quit()
