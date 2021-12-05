import pygame

class Board:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 100
        self.top = 20
        self.cell_size = 80
        self.w = 1
        self.surface = screen
        self.on_click = (0, 0)
        self.x = 0
        self.y = 0

    def render(self, surface):
        self.surface = surface
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(self.surface, "white", (self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size, self.cell_size), self.w)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(self.surface, "white", (self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size, self.cell_size), self.w)

    def get_click(self, mouse_pos):
        self.on_click = mouse_pos

    def get_cell(self):
        a, b = self.on_click[0], self.on_click[1]
        if a in range(self.left, self.left + (self.width*self.cell_size)) and b in range(self.top, self.top + (self.height*self.cell_size)):
            for i in range(self.width):
                for j in range(self.height):
                    if a in range(i*self.cell_size, (i+1)*self.cell_size) and b in range(j*self.cell_size, (j+1)*self.cell_size):
                        self.x, self.y = i, j
                        break
        else:
            self.x, self.y = 0, 0

    def change(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == self.x - 1:
                    if self.board[i][j] == 0:
                        self.board[i][j] = 1
                    else:
                        self.board[i][j] = 0
                elif j == self.y:
                    if self.board[i][j] == 0:
                        self.board[i][j] = 1
                    else:
                        self.board[i][j] = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(self.surface, "white", (self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size, self.cell_size), self.w)
                else:
                    pygame.draw.rect(self.surface, "white", (self.left + (i * self.cell_size), self.top + (j * self.cell_size), self.cell_size, self.cell_size))


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
                board.get_cell()
                screen.fill((0, 0, 0))
                board.change()
        pygame.display.flip()
    pygame.quit()
