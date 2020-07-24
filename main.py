import pygame
import random
pygame.init()
screenWidth = 604
screenHeight = 604
FPS = 30
# Colors
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 200, 100, 50)
White = (255, 255, 255)
Black = (0, 0, 0)


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


    # Function adds the Unvisited to the 2D array and returns the next cell
    def countNeighbors(self):
        global x, y
        neighbors = []

        for i in range(x):
            for j in range(y):
                top = grid[(((i + 1) + x) % x)][j]
                right = grid[i][(((j + 1) + y) % y)]
                bottom = grid[(((i - 1) + x) % x)][j]
                left = grid[i][(((j - 1) + y) % y)]

                if not top.visited:
                    neighbors.append(top)
                if not right.visited:
                    neighbors.append(right)
                if not bottom.visited:
                    neighbors.append(bottom)
                if not left.visited:
                    neighbors.append(left)
        # pick random unvisted cell as our next
        if len(neighbors) > 0:
            p = random.randrange(0, len(neighbors))
            return neighbors[p]


# Rows and Columns, length will be our width of each cell
length = 40
rows = screenWidth // length
cols = screenHeight // length
print(rows, cols)
# store cells
grid = [[]*cols]*rows
for i in range(rows):
    for j in range(cols):
        cell = Cell(i, j)
        grid[i].append(cell)
current = grid[0][0]
x = len(grid)
y = len(grid[i])


def display(surface):
    global current
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw(surface)
    # Mark first cell as visited
    current.visited = True
    # Check neighbors of current cell
    nextCell = current.countNeighbors()
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
