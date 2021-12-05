import pygame

def draw(screen):
    screen.fill((0, 0, 0))
    line1 = pygame.draw.line(screen, (255, 255, 255), (0, 0), (n1, n2), 5)
    line2 = pygame.draw.line(screen, (255, 255, 255), (n1, 0), (0, n2), 5)
    screen.blit(screen, line1, line2)


try:
    n = list(map(int, input().split()))
    n1, n2 = n[0], n[1]

    if __name__ == '__main__':
        pygame.init()
        size = width, height = n1, n2
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.set_caption("Крест")
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()

except Exception:
    print("Неверный формат ввода")