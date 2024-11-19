import random

import pygame
from pygame import Color

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        image = pygame.image.load("whackamole-template/mole.png")
        mole = [0, 0]
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] // 32 == mole[0] // 32) and (event.pos[1] // 32 == mole[1] // 32):
                        mole[0] = random.randrange(0, 20) * 32
                        mole[1] = random.randrange(0, 16) * 32
            screen.fill("light green")
            grid(screen, image, mole)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

def grid(screen, mole_image, mole):
    for i in range(16):
        pygame.draw.line(screen, Color(0, 0, 0), (0, i * 32), (640, i * 32), 1)

    for x in range(20):
        pygame.draw.line(screen, Color(0, 0, 0), (x * 32, 0), (x * 32, 512), 1)
    screen.blit(mole_image, mole_image.get_rect(topleft=(mole[0],mole[1])))

if __name__ == "__main__":
    main()