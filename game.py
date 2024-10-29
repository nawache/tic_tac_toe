from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    current_player = 'X'
    running = True

    game.display()

    while running:

        print(f'Сейчас ходит {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 1 or row > game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 1 or column > game.field_size:
                    raise FieldIndexError
            except FieldIndexError:
                print(f'Значение должно быть от 1 до {game.field_size}.')
                continue
            except ValueError:
                print(
                    'Буквы вводить нельзя. Только числа.'
                    '\nПожалуйста, введите значения заново.')
            except Exception as e:
                print(f'Возникла ошибка: {e}.')
            else:
                break

        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
