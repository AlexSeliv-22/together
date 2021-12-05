from typing import List

import pygame


class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.board: List[List[int]] = [[0] * width for _ in range(height)]

        self.left: int = 10
        self.top: int = 10
        self.cell_size: int = 30

    def set_view(self, left: int, top: int, cell_size) -> None:
        self.left: int = left
        self.top: int = top
        self.cell_size: int = cell_size

    def render(self, screen: pygame.display) -> None:
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (
                    self.cell_size * x + self.left,
                    self.cell_size * y + self.top,
                    self.cell_size,
                    self.cell_size), 1)


def main():
    pygame.init()
    pygame.display.set_caption('Инициализация игры')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
