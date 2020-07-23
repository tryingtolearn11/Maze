import pygame
import random
pygame.init()
screenWidth = 404
screenHeight = 404
FPS = 4
# Colors
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 200, 0)
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

    def index(self, i, j):
        # Test edge
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return -1
        else:
            return i + j * cols

    def checkN(self):
        neighbors = []
        # Indexing
        top = grid[self.index(i, j - 1)]
        right = grid[self.index(i + 1, j)]
        bottom = grid[self.index(i, j + 1)]
        left = grid[self.index(i - 1, j)]

        # List of Unvisited Cells, cells must be defined and Unvisited
        if top != -1 and top.visited is False:
            neighbors.append(top)
        if right != -1 and right.visited is False:
            neighbors.append(right)
        if bottom != -1 and bottom.visited is False:
            neighbors.append(bottom)
        if left != -1 and left.visited is False:
            neighbors.append(left)
        # pick at random
        if len(neighbors) > 0:
            r = random.randrange(0, len(neighbors))
            print(neighbors[r])
            return neighbors[r]


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
current = grid[0]


def display(surface):
    global current
    for i in range(len(grid)):
        grid[i].draw(surface)
    # Mark first cell as visited
    current.visited = True
    next = current.checkN()
    if next:
        next.visited = True
        current = next


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
