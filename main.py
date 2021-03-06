import pygame
import random
screenWidth = 1000
screenHeight = 1000
FPS = 40


# TODO: IMPLEMENT A* Pathfinding Algorithm
# Colors
Red = (200, 5, 50, 50)
Blue = (0, 100, 200, 50)
Green = (0, 200, 100, 50)
White = (255, 255, 255)
Black = (0, 0, 0)
bgcolor = (5, 55, 75)
BASICFONTSIZE = 20


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.visited = False
        # Order:   Top,  Right, Bottom, Left
        self.wall = [True, True, True, True]
        self.backtrackPathColor = False

    def draw(self, surface):
        x = self.i * length + xmargin
        y = self.j * length + ymargin
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

        if top and not top.visited:
            self.neighbors.append(top)
        if right and not right.visited:
            self.neighbors.append(right)
        if bottom and not bottom.visited:
            self.neighbors.append(bottom)
        if left and not left.visited:
            self.neighbors.append(left)
        # pick random unvisted cell
        if len(self.neighbors):
            p = random.randrange(len(self.neighbors))
            return self.neighbors[p]

    def marker(self):
        x = self.i * length + xmargin
        y = self.j * length + ymargin
        if self.i == 0 and self.j == 0:
            pygame.draw.rect(displayWindow, Black, (x, y, length, length))
        else:
            pygame.draw.rect(displayWindow, Blue, (x, y, length, length))

    def resetCells(self):
        self.visited = False
        self.wall = [True, True, True, True]
        self.backtrackPathColor = False


# Rows and Columns
length = 40
borderWidth = 800
borderHeight = 800
rows = borderWidth // length
cols = borderHeight // length
print(rows, cols)

# Add cells to stack
stack = []

xmargin = int((screenWidth - (length * rows + (cols - 1))) / 2)
ymargin = int((screenHeight - (length * cols + (rows - 1))) / 2)

# store cells
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


# Tile -> Pixel Coords
def leftTopofTile(a, b):
    left = xmargin + (a * length) + (a - 1)
    top = ymargin + (b * length) + (b - 1)
    return (left, top)


def display(surface):
    global current
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw(surface)

    # Drawing the border
    left, top = leftTopofTile(0, 0)
    width = cols * length
    height = rows * length
    pygame.draw.rect(displayWindow, Blue, (left - 3, top - 3, width + 10, height + 10), 5)
    # Draw Buttons
    drawButtons()
    if START:
        update()


def update():
    global current
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


def reset(surface):
    global current
    for i in range(x):
        for j in range(y):
            grid[i][j].resetCells()
    current = grid[0][0]


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


def makeTextBox(text, color, bgcolor, top, left):
    textSurface = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurface.get_rect()
    textRect.topleft = (top, left)
    return (textSurface, textRect)


def drawButtons():
    displayWindow.blit(RESET_SURF, RESET_RECT)
    displayWindow.blit(START_SURF, START_RECT)


def getMouseClick(surface, xpos, ypos):
    for i in range(x):
        for j in range(y):
            left, top = leftTopofTile(xpos, ypos)
            tileRect = pygame.Rect(left, top, length, length)
            if tileRect.collidepoint(xpos, ypos):
                return(xpos, ypos)
    return (None, None)


def main():
    global displayWindow, START, FPS, BASICFONT, RESET_SURF, RESET_RECT, START_SURF, START_RECT
    pygame.init()
    FPSclock = pygame.time.Clock()
    displayWindow = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Maze Generator")
    BASICFONT = pygame.font.SysFont('arial', BASICFONTSIZE)
    RESET_SURF, RESET_RECT = makeTextBox('Reset', White, Black, screenWidth - 150, screenHeight - 90)
    START_SURF, START_RECT = makeTextBox('Start', White, Black, screenWidth - 910, screenHeight - 90)
    START = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START = True
            if event.type == pygame.MOUSEBUTTONUP:
                x_spot, y_spot = getMouseClick(displayWindow, event.pos[0], event.pos[1])
                if (x_spot, y_spot) == (None, None):
                    if START_RECT.collidepoint(event.pos):
                        START = True
                    if RESET_RECT.collidepoint(event.pos):
                        START = False
                        pygame.time.wait(500)
                        reset(displayWindow)

        display(displayWindow)
        pygame.display.update()
        FPSclock.tick(FPS)
        displayWindow.fill(bgcolor)


if __name__ == '__main__':
    main()
