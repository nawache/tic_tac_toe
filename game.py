from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()

    while True:
        try:
            row = int(input('Введите номер строки: '))
            if row < 1 or row > game.field_size:
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            if column < 1 or column > game.field_size:
                raise FieldIndexError
        except FieldIndexError:
            print(f'Значение должно быть от 1 до {game.field_size}')
            continue
        else:
            break

    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main()
