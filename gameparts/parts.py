from random import randint


# Объявить класс.
class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for i in range(self.field_size)]
                      for i in range(self.field_size)]

    # Метод, который обрабатывает ходы человека.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который выбирает поле для хода компьютера.
    def ai_cell_picker(self):
        # Создаём пустой список
        free_cells = []

        # Ищем свободные ячейки, вносим их координаты в список
        for row in range(self.field_size):
            for column in range(self.field_size):
                if self.board[row][column] == ' ':
                    free_cells.append((row, column))

        # Возвращаем пару координат, выбранных случайным образом
        return free_cells[randint(0, len(free_cells) - 1)]

    # Метод, который обрабатывает ходы комрьютера.
    def ai_make_move(self, player):
        row, column = self.ai_cell_picker()
        self.make_move(row, column, player)

    # Метод, который проверяет, остались ли свободные ячейки.
    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    # Метод, который проверяет, есть ли победитель.
    def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[i][j] == player
                     for j in range(self.field_size)]) or
                all([self.board[j][i] == player
                     for j in range(self.field_size)])):
                return True

        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
