# Объявить класс.
class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(self.field_size)]
                      for _ in range(self.field_size)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row-1][col-1] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for i, row in enumerate(self.board):
            print('|'.join(row))
            if i < self.field_size-1:
                print('-' * 5)

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
