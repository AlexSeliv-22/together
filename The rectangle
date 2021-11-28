import pygame

def draw(screen):
    screen.fill((0, 0, 0))
    screen.fill(pygame.Color('red'), pygame.Rect(1, 1, width - 2, height - 2))

try:
    n = list(map(int, input().split()))
    n1, n2 = n[0], n[1]

    if __name__ == '__main__':
        pygame.init()
        size = width, height = n1, n2
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.set_caption("Прямоугольник")
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()

except Exception:
    print("Неправильный формат ввода")
