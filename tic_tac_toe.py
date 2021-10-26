from IPython.display import clear_output

def set_board():
    global d
    d = {1: '1',2: '2',3: '3',
         4: '4',5: '5',6: '6',
         7: '7',8: '8',9: '9'}

def print_board():
    clear_output()
    print('\n')
    print(f'|  {d[1]}  |  {d[2]}  |  {d[3]}  |    ')
    print(f'-------------------')
    print(f'|  {d[4]}  |  {d[5]}  |  {d[6]}  |    ')
    print(f'-------------------')
    print(f'|  {d[7]}  |  {d[8]}  |  {d[9]}  |    ')
    print('\n')
    
def check():
    win =  any(
        [[d[1], d[2], d[3]] in (['X', 'X', 'X'], ['O', 'O', 'O']),
        [d[4], d[5], d[6]] in (['X', 'X', 'X'], ['O', 'O', 'O']),
        [d[7], d[8], d[9]] in (['X', 'X', 'X'], ['O', 'O', 'O']),

        [d[1], d[4], d[7]] in (['X', 'X', 'X'], ['O', 'O', 'O']),
        [d[2], d[5], d[8]] in (['X', 'X', 'X'], ['O', 'O', 'O']),
        [d[3], d[6], d[9]] in (['X', 'X', 'X'], ['O', 'O', 'O']),

        [d[3], d[5], d[7]] in (['X', 'X', 'X'], ['O', 'O', 'O']),
        [d[1], d[5], d[9]] in (['X', 'X', 'X'], ['O', 'O', 'O'])])
    if win == True:
        return True
    else:
        if set([d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9]]) == {'X','O'}:
            return "tie"
            play_again()
    
    
def player_name_sym():
    global player1, player2
    player1 = input("Hello, player 1! What's your name? ")
    player2 = input("Hello, player 2! What's your name? ")
    
    players = {player1 : "", player2 : ""}
    
    player1_sym = ""
    
    while player1_sym not in ["X", "O"]:
        player1_sym = input(f"{player1}, please choose X or O to play! ")
        if player1_sym == "X":
            players[player1] = 'X'
            players[player2] = 'O'
            
        else:
            players[player1] = 'O'
            players[player2] = 'X'

    
    return players

def play_again():
    replay = ""
    while replay not in ['y','n']:
        replay = input("Play again? (Y/N) ").lower()

        if replay == 'n':
            return 'Thank you for playing!'
        else:
            set_board()
            play_game()

def play_game():
    
    set_board()
    
    players = player_name_sym()
    
    control = True
    player1_turn = True
    player2_turn = True

    while control == True:
        print_board()
        while player1_turn == True:
            try:
                num_player1 = int(input(f"{player1}, choose a number from 1 to 9: "))
                if num_player1 in range(1,10):
                       if d[num_player1] not in ['X', 'O']:
                            d[num_player1] = players[player1]
                            player1_turn, player2_turn = False, True
                            if check() == True:
                                control, player2_turn = False, False
                                print_board()
                                print(f"Congratulations, {player1}! You won!")
                            elif check() == 'tie':
                                control, player2_turn = False, False
                                print_board()
                                print("It's a tie!")                                
            except ValueError:
                print("Please, choose a valid number.")

        while player2_turn == True:
            print_board()
            try:
                num_player2 = int(input(f"{player2}, choose a number from 1 to 9: "))
                if num_player2 in range(1,10):
                       if d[num_player2] not in ['X', 'O']:
                            d[num_player2] = players[player2]
                            player1_turn, player2_turn = True, False
                            if check() == True:
                                control, player1_turn = False, False
                                print_board()
                                print(f"Congratulations, {player2}! You won!")
                            elif check() == 'tie':
                                control, player1_turn = False, False
                                print_board()
                                print("It's a tie!")                                
            except ValueError:
                print("Please, choose a valid number.")
    
    play_again()
    