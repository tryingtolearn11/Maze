import pygame
import random
pygame.init()
screenWidth = 604
screenHeight = 604
FPS = 30
# Colors
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 200, 100, 100)
White = (255, 255, 255)


class Cell:
    def __init__(self, i, j):
        self.i = i  # Row
        self.j = j  # Column
        self.visited = False
        # Checks to see if wall(s) of the cell exists
        # Order:   Top,  Right, Bottom, Left
        self.wall = [True, True, True, True]

    def draw(self, surface):
        x = self.i * length
        y = self.j * length
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
        if self.visited:
            pygame.draw.rect(displayWindow, Green, (x, y, length, length))

    # Function adds the Unvisited to the 2D array and returns the next cell
    def checkN(self):
        neighbors = [[]*cols]*rows
        for i in range(len(neighbors)):
            for j in range(len(neighbors[i])):
                x = len(neighbors)
                y = len(neighbors[i])
                # Indexing
                top = grid[(((i + 1) + x) % x)][j]
                right = grid[i][(((j + 1) + y) % y)]
                bottom = grid[(((i - 1) + x) % x)][j]
                left = grid[i][(((j - 1) + y) % y)]
                # List of Unvisited Cells, cells must be defined and Unvisited
                if top.visited is False:
                    neighbors[i].append(top)
                if right.visited is False:
                    neighbors[i].append(right)
                if bottom.visited is False:
                    neighbors[i].append(bottom)
                if left.visited is False:
                    neighbors[i].append(left)
                if len(neighbors) > 0:
                    r = random.randrange(0, len(neighbors))
                    m = random.randrange(0, len(neighbors[i]))
                    return neighbors[r][m]


# Rows and Columns, length will be our width of each cell
length = 40
rows = screenWidth // length
cols = screenHeight // length
# store cells
grid = []
for i in range(rows):
    for j in range(cols):
        cell = Cell(i, j)
        grid.append(cell)
current = grid[0]


def display(surface):
    global current
    for i in range(len(grid)):
        grid[i].draw(surface)
    # Mark first cell as visited
    current.visited = True
    # Check neighbors of current cell
    nextCell = current.checkN()
    if nextCell:
        nextCell.visited = True
        current = nextCell


displayWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Maze Generator")


def main():
    global FPS
    FPSclock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        FPSclock.tick(FPS)
        display(displayWindow)
        pygame.display.update()


if __name__ == '__main__':
    main()
