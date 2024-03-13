table_size = 3

table = list(range(1, 10))

print('Welcome to Naughts and crosses!')

def bring_out_table():
    print('_' * 4 * table_size)
    for i in range(table_size):
     print((' ' * 3 + '|') * 3)
     print('', table[i * 3], '|', table[1 + i * 3], '|', table[2 + i * 3], '|')
     print(('_' * 3 + '|') * 3)
bring_out_table()

def move_gamer(enter, reach):
    if (enter > 9 or enter < 1 or table[enter-1] in ('X', 'O')):
        return False

    table[enter-1] = reach
    return True

def check_winner():

    return False

def actual_player():

    game_player = 'X'

    move = 1


    while (move<10) and (check_winner() == False):
        enter = input('player move ' + game_player + ' Enter field number (0 - exit)')

        if (enter == '0'):
            break
        if enter >= '10':
            print('Number is too high!')


        if (move_gamer(int(enter), game_player)):
          print('Coup!')

          bring_out_table()

          if (game_player == 'X'):
                game_player = 'O'
          else:
                game_player = 'X'
          move += 1
        print()
    else:
        print('Wrong number! Please, repeat!')


actual_player()



