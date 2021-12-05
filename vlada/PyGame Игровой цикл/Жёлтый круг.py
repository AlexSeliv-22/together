from typing import Tuple

import pygame


def draw(
    screen: pygame.display,
    pos: tuple,
    fps: int,
    clock: pygame.time
) -> Tuple[pygame.Color, int, int, int]:
    yellow: pygame.Color = pygame.Color('yellow')
    x, y = pos
    r: int = 0
    screen.fill((0, 0, 255))
    return yellow, x, y, r


def main():
    pygame.init()

    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)

    screen.fill((0, 0, 255))
    pygame.display.flip()

    pygame.display.set_caption('Жёлтый круг')

    fps = 10  # кол-во кадров в секунду
    clock = pygame.time.Clock()
    running = True
    is_ready = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_ready = True
                yellow, x, y, r = draw(screen, event.pos, fps, clock)
        if is_ready:
            clock.tick(fps)
            pygame.draw.circle(screen, yellow, (x, y), r)
            pygame.display.flip()
            r += 5


if __name__ == '__main__':
    main()
