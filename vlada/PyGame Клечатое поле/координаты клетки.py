from typing import List, Tuple, Optional

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

    def get_cell_position(self, pos: Tuple[float]) -> Optional[Tuple[int]]:
        """
        Метод вернёт координаты клетки в формате x, y
        или None
        """
        output = None
        x, y = pos[0] - self.left, pos[1] - self.top
        pos_x, pos_y = x // self.cell_size, y // self.cell_size
        if pos_x in range(self.width) and pos_y in range(self.height):
            output = (pos_x, pos_y)
        return output


def main():
    pygame.init()
    pygame.display.set_caption('Координаты клетки')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_cell_position(event.pos))
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
