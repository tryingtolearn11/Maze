import pygame
import random
pygame.init()
screenWidth = 604
screenHeight = 604
FPS = 60

# Colors
Red = (255, 0, 0)
Blue = (0, 100, 200, 50)
Green = (0, 200, 100, 50)
White = (255, 255, 255)
Black = (0, 0, 0)

# TODO: FIX THE COUNTING FUNCTION- MESSES UP THE PATHING


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
        if self.visited:
            pygame.draw.rect(displayWindow, Green, (x, y, length, length))
        # Top Line
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

    # Function adds the Unvisited to the 2D array and returns the next cell
    def countNeighbors(self, grid):
        global x, y
        self.neighbors = []
        # Edge Cases
        # Top Cell
        if self.j == 0:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i][self.j - 1])
        # Right
        if self.i == x - 1:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i + 1][self.j])
        # Bottom
        if self.j == y - 1:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i][self.j + 1])
        # Left
        if self.i == 0:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i - 1][self.j])

    def marker(self):
        x = self.i * length
        y = self.j * length
        pygame.draw.rect(displayWindow, Blue, (x, y, length, length))


# Rows and Columns, length will be our width of each cell
length = 40
rows = screenWidth // length
cols = screenHeight // length

# Add cells to stack
stack = []

# store cells in the grid
grid = []
for i in range(rows):
    column = []
    for j in range(cols):
        cell = Cell(i, j)
        column.append(cell)
    grid.append(column)


current = grid[0][0]
stack.append(current)
x = len(grid)
y = len(grid[i])


def display(surface):
    global current
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw(surface)
            grid[i][j].countNeighbors(grid)

    current.visited = True
    current.marker()
    next = random.choice(current.neighbors)
    if len(stack):
        current = stack.pop()
    if next and not next.visited:
        next.visited = True
        stack.append(current)
        deleteWall(current, next)
        current = next


def deleteWall(a, b):
    # Right and Left Walls
    p = a.i - b.i
    if p == 1:      # neighbor to the left
        a.wall[3] = False
        b.wall[1] = False
    elif p == -1:  # neighbor to the right
        a.wall[1] = False
        b.wall[3] = False
    # Top and Bottom Walls
    q = a.j - b.j
    if q == 1:     # neighbor above
        a.wall[0] = False
        b.wall[2] = False
    elif q == -1:  # neighbor below
        a.wall[2] = False
        b.wall[0] = False


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
