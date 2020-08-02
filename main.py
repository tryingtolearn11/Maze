import pygame
import random
screenWidth = 800
screenHeight = 800
FPS = 50

# Colors
Red = (255, 0, 0)
Blue = (0, 100, 200, 50)
Green = (0, 200, 100, 50)
White = (255, 255, 255)
Black = (0, 0, 0)


class Cell:
    def __init__(self, i, j):
        self.i = i  # Row
        self.j = j  # Column
        self.visited = False
        # Order:   Top,  Right, Bottom, Left
        self.wall = [True, True, True, True]
        self.backtrackPathColor = False

    def draw(self, surface):
        x = self.i * length
        y = self.j * length

        if self.backtrackPathColor:
            pygame.draw.rect(displayWindow, Black, (x, y, length, length))
        elif self.visited:
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
        if self.j > 0:
            top = grid[self.i][self.j - 1]
        else:
            top = None
        if self.i < x - 1:
            right = grid[self.i + 1][self.j]
        else:
            right = None
        if self.j < y - 1:
            bottom = grid[self.i][self.j + 1]
        else:
            bottom = None
        if self.i > 0:
            left = grid[self.i - 1][self.j]
        else:
            left = None

        # If the neighbor cell is unvisited add to array
        if top and not top.visited:
            self.neighbors.append(top)
        if right and not right.visited:
            self.neighbors.append(right)
        if bottom and not bottom.visited:
            self.neighbors.append(bottom)
        if left and not left.visited:
            self.neighbors.append(left)
        # pick random unvisted cell as our next
        if len(self.neighbors):
            p = random.randrange(len(self.neighbors))
            return self.neighbors[p]

    def marker(self):
        x = self.i * length
        y = self.j * length
        pygame.draw.rect(displayWindow, Blue, (x, y, length, length))


# Rows and Columns, length will be our width of each cell
length = 40
borderWidth = 800
borderHeight = 800
rows = borderWidth // length
cols = borderHeight // length

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

x = len(grid)
y = len(grid[i])


def display(surface):
    global current
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw(surface)

    current.visited = True
    current.marker()
    next = current.countNeighbors(grid)
    if next:
        stack.append(current)
        deleteWall(current, next)
        next.visited = True
        current = next
    elif len(stack):
        current.backtrackPathColor = True
        current = stack.pop()


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
    pygame.init()
    FPSclock = pygame.time.Clock()
    start = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True
        if(start):
            display(displayWindow)
            pygame.display.update()
            FPSclock.tick(FPS)


if __name__ == '__main__':
    main()
