import pygame
import random
pygame.init()
screenWidth = 604
screenHeight = 604
FPS = 20

# Colors
Red = (255, 0, 0)
Blue = (0, 100, 200, 50)
Green = (0, 200, 100, 50)
White = (255, 255, 255)
Black = (0, 0, 0)

# TODO: FIX THE COUNTING FUNCTION- MESSES UP THE PATHING
# TODO: Now finish update function: have it move to the next cell


class Cell:
    def __init__(self, i, j):
        self.i = i  # Row
        self.j = j  # Column
        self.visited = False
        # Checks to see if wall(s) of the cell exists
        # Order:   Top,  Right, Bottom, Left
        self.wall = [True, True, True, True]
        self.randomNextCell = [0, 1, 2, 3]
        random.shuffle(self.randomNextCell)

    def draw(self, surface):
        x = self.i * length
        y = self.j * length
        # Our Path in Green
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
        self.changed = False

    # Function adds the Unvisited to the 2D array
    def countNeighbors(self, grid):
        global x, y
        self.neighbors = []
        if self.i == 0:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i - 1][self.j])
        if self.i == x - 1:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i + 1][self.j])
        if self.j == 0:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i][self.j - 1])
        if self.j == y - 1:
            self.neighbors.append(None)
        else:
            self.neighbors.append(grid[self.i][self.j + 1])

    # Function sets current cell to visited and gives us the next cell to visit
    def update(self, stack):
        self.visited = True
        if (len(self.randomNextCell)):
            stack.append(self)
            print(self.randomNextCell)
            next = self.randomNextCell.pop()
            # n is our next cell
            n = self.neighbors[next]
            print("neighbor size is ", len(self.neighbors))
            print("next number is ", next)
            print("Next cell is ", n)
            if n and not n.visited:
                n.visited = True
                stack.append(n)
            print("Current Cell is ", self)

    # Highlights the current cell
    def marker(self):
        x = self.i * length
        y = self.j * length
        pygame.draw.rect(displayWindow, Blue, (x, y, length, length))


# Rows and Columns, length will be our width of each cell
length = 40
rows = screenWidth // length
cols = screenHeight // length
print("Rows = ", rows, "Cols = ", cols)

# store cells
grid = [[]*cols]*rows
for i in range(rows):
    for j in range(cols):
        cell = Cell(i, j)
        grid[i].append(cell)
x = len(grid)
y = len(grid[i])

current = grid[0][0]
stack = []


def display(surface):
    global current
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw(surface)
    # current.marker()
    current.countNeighbors(grid)
    current.update(stack)
    if len(stack):
        stack.pop()
        print("Stack has :", stack)

    # if nextCell:
    #    nextCell.visited = True
    #    # deleteWall(current, nextCell)
    #    current = nextCell


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
