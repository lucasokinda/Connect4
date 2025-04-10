import random

#######This function allow to display the main menu##########
def afficher_menu():
    print("===== MENU PUISSANCE 4 =====")
    print("1. Jouer😁​")
    print("2. Quitter😢")

#######this function allow to print the game board#########
def print_game_board():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if game_board[x][y] == "🔵":
                print("", game_board[x][y], end=" |")
            elif game_board[x][y] == "🔴":
                print("", game_board[x][y], end=" |")
            else:
                print(" ", game_board[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

######this allow function to update the board with the player's move########
def modify_array(space_picked, turn):
    game_board[space_picked[0]][space_picked[1]] = turn

######this function to check if there's a winner (either '🔵' or '🔴')#######
def check_for_winner(chip):
    #######here we check horizontal spaces for 4 consecutive chips#######
    for y in range(rows):
        for x in range(cols - 3):
            if game_board[x][y] == chip and game_board[x+1][y] == chip and game_board[x+2][y] == chip and game_board[x+3][y] == chip:
                print("\nFin du jeu", chip, "Gagné! Merci d'avoir joué :)")
                return True

    #######here we check vertical spaces for 4 consecutive chips#######
    for x in range(rows):
        for y in range(cols - 3):
            if game_board[x][y] == chip and game_board[x][y+1] == chip and game_board[x][y+2] == chip and game_board[x][y+3] == chip:
                print("\nFin du jeu", chip, "Gagné! Merci d'avoir joué :)")
                return True

    #######here we check upper right to bottom left diagonal spaces for 4 consecutive chips######
    for x in range(rows - 3):
        for y in range(3, cols):
            if game_board[x][y] == chip and game_board[x+1][y-1] == chip and game_board[x+2][y-2] == chip and game_board[x+3][y-3] == chip:
                print("\nFin du jeu", chip, "Gagné! Merci d'avoir joué :)")
                return True

    #######here we check upper left to bottom right diagonal spaces for 4 consecutive chips######
    for x in range(rows - 3):
        for y in range(cols - 3):
            if game_board[x][y] == chip and game_board[x+1][y+1] == chip and game_board[x+2][y+2] == chip and game_board[x+3][y+3] == chip:
                print("\nFin du jeu", chip, "Gagné! Merci d'avoir joué :)")
                return True
    return False

#####this function allow to parse the coordinate input#######
def coordinate_parser(input_string):
    coordinate = [None] * 2
    if input_string[0] == "A":
        coordinate[1] = 0
    elif input_string[0] == "B":
        coordinate[1] = 1
    elif input_string[0] == "C":
        coordinate[1] = 2
    elif input_string[0] == "D":
        coordinate[1] = 3
    elif input_string[0] == "E":
        coordinate[1] = 4
    elif input_string[0] == "F":
        coordinate[1] = 5
    elif input_string[0] == "G":
        coordinate[1] = 6
    else:
        print("Invalid")
    coordinate[0] = int(input_string[1])
    return coordinate

######this function to check if the space on the board is available for a move########
def is_space_available(intended_coordinate):
    ########return False if the space is not empty#########
    if game_board[intended_coordinate[0]][intended_coordinate[1]] == '🔴':
        return False
    elif game_board[intended_coordinate[0]][intended_coordinate[1]] == '🔵':
        return False
    else:
        return True

#######this function allow to add a gravity effect######
def gravity_checker(intended_coordinate):
    # we calculate the space below the chosen coordinate
    space_below = [None] * 2
    space_below[0] = intended_coordinate[0] + 1
    space_below[1] = intended_coordinate[1]
    
    # If it's at the bottom row (index 6), it's automatically valid (last row)
    if space_below[0] == 6:
        return True
    
    # If there is a chip below, it means the current space is available
    if is_space_available(space_below) == False:
        return True
    return False

############################Main Game Loop#############################
while True:
    afficher_menu()  # Display the menu options to the user
    choix = input("Choisissez une option (1 ou 2): ")  # Get user input for menu choice
    
    # Option 1: Start the game
    if choix == "1":
        print("\nBienvenu sur le puissance 4!")
        print("--------------------------")
        
        # Initialize the game state
        possible_letters = ["A", "B", "C", "D", "E", "F", "G"]
        game_board = [["", "", "", "", "", "", ""] for _ in range(6)]
        rows = 6
        cols = 7
        leave_loop = False
        turn_counter = 0

        # Main game loop: runs until the game is won
        while not leave_loop:
            # Player's turn ('🔵')
            if turn_counter % 2 == 0:
                print_game_board()
                while True:
                    space_picked = input("\nChoisissez où jouer: ")
                    coordinate = coordinate_parser(space_picked)
                    try:
                        # Check if space is available and the chip will land correctly
                        if is_space_available(coordinate) and gravity_checker(coordinate):
                            modify_array(coordinate, '🔵')  
                            break
                        else:
                            print("Coordonnés invalides")
                    except:
                        print("Une ereur est survenu. Veuillez réessayer.")
                winner = check_for_winner('🔵')
                turn_counter += 1
            else:
                # Computer's turn ('🔴')
                while True:
                    cpu_choice = [random.choice(possible_letters), random.randint(0, 5)]
                    cpu_coordinate = coordinate_parser(cpu_choice)
                    if is_space_available(cpu_coordinate) and gravity_checker(cpu_coordinate):
                        modify_array(cpu_coordinate, '🔴')  
                        break
                turn_counter += 1
                winner = check_for_winner('🔴')

            if winner:  # End the game if a player wins
                print_game_board()
                break
    
    # Option 2: Quit the game
    elif choix == "2":
        print("À bientot!")
        break
    
    # Invalid option input
    else:
        print("Option invalide choisissez 1 ou 2.\n")
