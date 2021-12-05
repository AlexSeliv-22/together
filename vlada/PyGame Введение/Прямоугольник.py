import logging
import sys

import pygame

# TODO: добрый человек, я в упор не понимаю, что делает сия функция, просвети :)
def create_logger(
    name: str,
    format_line: str = '%(levelname)s — %(message)s',
    stream_out: sys = sys.stderr,
    level: str = 'INFO'
) -> logging:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(format_line)
    handler = logging.StreamHandler(stream=stream_out)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger

# TODO: не очень понятно, зачем отдельно упоминать тип переменной. И "-> None" тоже нуждается в объяснении - что это и зачем.
def draw(screen: pygame.display, width: int, height: int) -> None:
    color: pygame.Color = pygame.Color('red')
    screen.fill((0, 0, 0))

    screen.fill(color, (1, 1, width - 2, height - 2))


logger = create_logger(__name__)

if __name__ == '__main__':
    pygame.init()
    width, height = input().split()

    if width.isdigit() and height.isdigit():
        size = width, height = int(width), int(height)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Прямоугольник')

        draw(screen, width, height)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    else:
        logger.error('Неправильный формат ввода')
        pygame.quit()
