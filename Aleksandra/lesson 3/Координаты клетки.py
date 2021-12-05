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
        self.on_click = (0, 0)

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

    def get_cell(self, mouse_pos):
        a, b = self.on_click[0], self.on_click[1]
        if a in range(self.left, self.left + (self.width*self.cell_size)) and b in range(self.top, self.top + (self.height*self.cell_size)):
            for i in range(self.width):
                for j in range(self.height):
                    if a in range(i*self.cell_size, (i+1)*self.cell_size) and b in range(j*self.cell_size, (j+1)*self.cell_size):
                        print((i, j))
                        break
        else:
            print("None")

