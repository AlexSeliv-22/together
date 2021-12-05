import pygame


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Желтый круг")
    running = True
    circle_width = 0
    circle_radius = 0
    circle_exists = False
    color_round = pygame.Color("yellow")
    color_surface = pygame.Color("blue")
    plus_radius = pygame.USEREVENT + 25
    pygame.time.set_timer(plus_radius, 10)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                circle_exists = True
                screen.fill(pygame.Color('blue'))
                circle_radius = 0
                circle_pos = event.pos
                pygame.draw.circle(screen, color_round, circle_pos, circle_radius, circle_width)
            if event.type == plus_radius and circle_exists:
                circle_radius += 1
                pygame.draw.circle(screen, color_round, circle_pos, circle_radius, circle_width)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()