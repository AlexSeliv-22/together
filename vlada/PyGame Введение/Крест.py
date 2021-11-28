import logging
import sys

import pygame


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


def draw(screen: pygame.display, width: int, height: int) -> None:
    color: pygame.Color = pygame.Color('#000000')
    screen.fill(color)

    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), 5)


logger = create_logger(__name__)

if __name__ == '__main__':
    pygame.init()
    width, height = input().split()
    if width.isdigit() and height.isdigit():
        size = width, height = int(width), int(height)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Крест')

        draw(screen, width, height)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    else:
        logger.error('Неправильный формат ввода')
        pygame.quit()
