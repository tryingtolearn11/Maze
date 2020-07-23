import pygame


pygame.init()
screenWidth = 400
screenHeight = 400
displayWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Maze")


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.update()


if __name__ == '__main__':
    main()
