from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    current_player = 'X'

    print('Добро пожаловать в игру "крестики-нолики"!\n')
    game.display()

    while True:

        print(f'\nСейчас ходят {current_player}')

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
                break

        game.make_move(row, column, current_player)
        game.display()

        if game.check_win(current_player):
            print(f'\nПобедили {current_player}!')
            break

        if game.is_board_full():
            print('\nНичья!')
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
