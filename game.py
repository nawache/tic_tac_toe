from datetime import datetime
from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    print('Добро пожаловать в игру "крестики-нолики"!\n')
    
    game = Board()
    game.display()

    current_player = 'X'

    running = True
    while running:
        print(f'\nСейчас ходят {current_player}')

        row, column = coordinates_input(game)
        game.make_move(row, column, current_player)
        game.display()

        running = check_for_game_over(game, current_player)
        current_player = change_player(current_player)


def coordinates_input(game):
    while True:
        try:

            row = int(input('Введите номер строки: '))
            if row < 1 or row > game.field_size:
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            if column < 1 or column > game.field_size:
                raise FieldIndexError
            if game.board[row-1][column-1] != ' ':
                raise CellOccupiedError
            
        except FieldIndexError:

            print(f'Значение должно быть от 1 до {game.field_size}.')
            continue

        except ValueError:

            print('Буквы вводить нельзя. Только числа.')
            print('Пожалуйста, введите значения заново.')

        except CellOccupiedError:

            print('Ячейка уже занята!')
            print('Введите другие координаты.')

        except Exception as e:

            print(f'Возникла ошибка: {e}.')

        else:

            print('\n')
            return row, column


def change_player(current_player):
    return 'O' if current_player == 'X' else 'X'


def save_game_result(result, winner_name=''):
    game_end_time = datetime.now().strftime('%d/%m/%Y %H:%M')
    log_text = f'{game_end_time} {result}{winner_name}\n'
    with open('results.txt', 'a') as result_log:
        result_log.write(log_text)


def check_for_game_over(game, current_player):
    if game.check_win(current_player):

        result = f'Победили {current_player}!'
        print(f'\n{result}')

        winner_name = f' Победитель: {input('Введите имя победителя: ')}'
        save_game_result(result, winner_name)

        return False

    if game.is_board_full():

        result = 'Ничья!'
        print(f'\n{result}')

        save_game_result(result)

        return False

    return True


if __name__ == '__main__':
    main()
