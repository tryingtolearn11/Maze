import pygame

pygame.init()
screenWidth = 604
screenHeight = 604

# Colors
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
White = (255, 255, 255)


class Cell:
    def __init__(self, i, j):
        self.i = i  # Row
        self.j = j  # Column
        # Checks to see if wall(s) of the cell exists
        # Order:   Top,  Right, Bottom, Left
        self.wall = [True, True, True, True]

    def draw(self, surface):
        x = self.i * length
        y = self.j * length
        # pygame.draw.rect(displayWindow, White, (x, y, length, length), 1)
        # Top Line                             Start Pos,  End Pos
        if self.wall[0]:
            pygame.draw.line(displayWindow, White, (x, y), (x + length, y), 1)
        # Right Line
        if self.wall[1]:
            pygame.draw.line(displayWindow, White, (x + length, y), (x + length, y + length), 1)
        # Bottom
        if self.wall[2]:
            pygame.draw.line(displayWindow, White, (x + length, y + length), (x, y + length), 1)
        # Left
        if self.wall[3]:
            pygame.draw.line(displayWindow, White, (x, y + length), (x, y), 1)


# Rows and Columns, length will be our width of each cell
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
pygame.display.set_caption("Maze Generator")


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
