def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

    def single_game(cur_player):

        values = [' ' for x in range(9)]

        player_pos = {'X': [], 'O': []}

        while True:
            print_tic_tac_toe(values)

            try:
                print("Player ", cur_player, " turn. Which box? : ", end="")
                move = int(input())
            except ValueError:
                print("Wrong Input!!! Try Again")
                continue

            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print("Wrong Input!!! Try Again")
                continue

            # Check if the box is not occupied already
            if values[move - 1] != ' ':
                print("Place already filled. Try again!!")
                continue

                values[move - 1] = cur_player

                player_pos[cur_player].append(move)

                if check_win(player_pos, cur_player):
                    print_tic_tac_toe(values)
                    print("Player ", cur_player, " has won the game!!")
                    print("\n")
                    return cur_player

                if check_draw(player_pos):
                    print_tic_tac_toe(values)
                    print("Game Drawn")
                    print("\n")
                    return 'D'

                def check_win(player_pos, cur_player):
                    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
                    for x in soln:
                        if all(y in player_pos[cur_player] for y in x):
                            return True
                        return False

                    def check_draw(player_pos):
                        if len(player_pos['X']) + len(player_pos['O']) == 9:
                            return True
                            return False

                        if cur_player == 'X':
                            cur_player = 'O'
                        else:
                            cur_player = 'X'

