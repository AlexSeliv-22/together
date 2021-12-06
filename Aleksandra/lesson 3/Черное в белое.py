import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 100
        self.top = 20
        self.cell_size = 80
        self.w = 1
        self.surface = screen
        self.on_click = (0, 0)
        self.x = -1
        self.y = -1

    def render(self, surface):
        self.surface = surface
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(self.surface, "white", (self.left + (j * self.cell_size),
                                                         self.top + (i * self.cell_size),
                                                         self.cell_size, self.cell_size), self.w)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(self.surface, "white", (self.left + (i * self.cell_size),
                                                         self.top + (j * self.cell_size),
                                                         self.cell_size, self.cell_size), self.w)

    def get_click(self, mouse_pos):
        # self.on_click = mouse_pos
        pass

    def get_cell(self, mouse_pos):
        a, b = mouse_pos[0], mouse_pos[1]
        if a > self.left and a < self.left + (self.width*self.cell_size):
            if b > self.top and b < self.top + (self.height*self.cell_size):
                for i in range(self.height):
                    for j in range(self.width):
                        if a in range(self.left+j*self.cell_size, self.left+(j+1)*self.cell_size):
                            if b in range(self.top+i*self.cell_size, self.top+(i+1)*self.cell_size):
                                self.x, self.y = j, i
                                break
            else:
                self.x, self.y = -1, -1
        else:
            self.x, self.y = -1, -1


    def change(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == self.y:
                    if self.board[i][j] == 0:
                        self.board[i][j] = 1
                    else:
                        self.board[i][j] = 0
                elif j == self.x:
                    if self.board[i][j] == 0:
                        self.board[i][j] = 1
                    else:
                        self.board[i][j] = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(self.surface, "white", (self.left + (j * self.cell_size),
                                                             self.top + (i * self.cell_size), self.cell_size,
                                                             self.cell_size), self.w)
                else:
                    pygame.draw.rect(self.surface, "white", (self.left + (j * self.cell_size),
                                                             self.top + (i * self.cell_size), self.cell_size,
                                                             self.cell_size))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    pygame.display.set_caption("Черное в белое и наоборот")
    screen.fill((0, 0, 0))
    board.render(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                board.get_click(pos)
                board.get_cell(pos)
                screen.fill((0, 0, 0))
                board.change()
        pygame.display.flip()
    pygame.quit()
