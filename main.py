import pygame

pygame.init()
screenWidth = 600
screenHeight = 600

# Colors
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
White = (255, 255, 255)


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def draw(self, surface):
        x = self.i * length
        y = self.j * length
        pygame.draw.rect(displayWindow, White, (x, y, length, length), 2)


# Rows and Colums
global rows, cols, length
length = 40
rows = screenWidth // length
cols = screenHeight // length
# store cells
grid = []
for i in range(rows):
    for j in range(cols):
        cell = Cell(i, j)
        grid.append(cell)


def display(surface):
    for i in range(len(grid)):
        grid[i].draw(surface)


displayWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Maze")


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display(displayWindow)
        pygame.display.update()


if __name__ == '__main__':
    main()
