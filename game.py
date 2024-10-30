from datetime import datetime
from time import sleep

import pygame

from gameparts import Board


PALETTE = {
    'LIGHT_ORANGE': (255, 218, 185),
    'APRICOT': (251, 196, 171),
    'MELON': (248, 173, 157),
    'CORAL_PINK': (244, 151, 142),
    'LIGHT_CORAL': (240, 128, 128),
    'DARK_SPRING_GREEN': (34, 111, 84),
    'TYRIAN_PURPLE': (100, 17, 63)
}
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = PALETTE['LIGHT_ORANGE']
LINE_COLOR = PALETTE['MELON']
X_COLOR = PALETTE['TYRIAN_PURPLE']
O_COLOR = PALETTE['DARK_SPRING_GREEN']
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)


def draw_lines():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def next_player(player):
    return 'O' if player == 'X' else 'X'


def save_game_result(result):
    game_date = datetime.now().strftime('%d/%m/%Y %H:%M')
    winner = '' if result == 'Ничья!' else f' Победитель: {
        input('Введите имя победителя: ')}'
    log_text = f'{game_date} {result}{winner}\n'
    with open('results.txt', 'a') as results:
        results.write(log_text)


def check_for_game_over(game, player):
    if game.check_win(player):

        result = f'Победили {player}!'
        print(f'\n{result}')

        save_game_result(result)

        return False

    if game.is_board_full():

        result = 'Ничья!'
        print(f'\n{result}')

        save_game_result(result)

        return False

    return True


def main():
    print('Добро пожаловать в игру "крестики-нолики"!\n')

    game = Board()
    draw_lines()

    current_player = 'X'

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)
                    running = check_for_game_over(game, current_player)
                    current_player = next_player(current_player)
                    draw_figures(game.board)

        pygame.display.update()

    sleep(1)
    pygame.quit()


if __name__ == '__main__':
    main()
