import pygame

def draw(screen):
    screen.fill((0, 0, 0))
    i = 0
    if n % 2 == 1:
        j = s
    else:
        j = 0
    data = []
    flag = True
    while i <= a:
        while j <= a:
            data.append((j, i, s, s))
            j += 2 * s
        i += s
        if flag:
            if n % 2 == 1:
                j = 0
            else:
                j = s
        else:
            if n % 2 == 1:
                j = s
            else:
                j = 0
        flag = not flag
    for i in range(len(data)):
        pygame.draw.rect(screen, (255, 255, 255), data[i], 0)

try:
    numbers = list(map(int, input().split()))
    a, n = numbers[0], numbers[1]
    s = a // n

    if __name__ == '__main__':
        pygame.init()
        size = width, height = a, a
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.set_caption("Прямоугольник")
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()

except Exception:
    print("Неправильный формат ввода")
