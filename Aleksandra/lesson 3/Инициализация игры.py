class Board:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.w = 1
        self.surface = screen

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

