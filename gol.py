import pygame
import random

class Life(object):
    def __init__(self, screen):
        self.screen = screen

    def clear(self):
        self.screen.fill((0, 0, 0))

    def pixel(self, x, y, r, g, b):
        self.screen.set_at((x, y), (r, g, b))

    def copy(self):
        self.prev_turn = self.screen.copy()

    def initialContent(self):
        #Penta-decathlon
        self.pixel(30, 30, 255, 255, 255)
        self.pixel(30, 31, 255, 255, 255)

        self.pixel(29, 32, 255, 255, 255)
        self.pixel(31, 32, 255, 255, 255)

        self.pixel(30, 33, 255, 255, 255)
        self.pixel(30, 34, 255, 255, 255)
        self.pixel(30, 35, 255, 255, 255)
        self.pixel(30, 36, 255, 255, 255)

        self.pixel(29, 37, 255, 255, 255)
        self.pixel(31, 37, 255, 255, 255)

        self.pixel(30, 38, 255, 255, 255)
        self.pixel(30, 39, 255, 255, 255)

        #Random
        self.pixel(90, 70, 255, 255, 255)

        self.pixel(91, 71, 255, 255, 255)
        self.pixel(92, 71, 255, 255, 255)
        self.pixel(93, 71, 255, 255, 255)
        self.pixel(94, 71, 255, 255, 255)
        self.pixel(95, 71, 255, 255, 255)
        self.pixel(96, 71, 255, 255, 255)

        self.pixel(96, 72, 255, 255, 255)
        self.pixel(96, 73, 255, 255, 255)

        self.pixel(95, 74, 255, 255, 255)

        self.pixel(93, 75, 255, 255, 255)
        self.pixel(92, 75, 255, 255, 255)

        self.pixel(90, 74, 255, 255, 255)
        

    def checkPaint(self, x, y):
        alive = False
        around = 0
        if self.prev_turn.get_at((x, y)) != (0, 0, 0, 255):
            alive = True
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                a = x + i
                b = y + j
                if a == -1:
                    a = 99
                if a == 100:
                    a = 0
                if b == -1:
                    b = 99
                if b == 100:
                    b = 0
                if self.prev_turn.get_at((a, b)) != (0, 0, 0, 255):
                    around += 1
        

        if alive and around < 2:
            self.pixel(x, y, 0, 0, 0)
        if alive and (around == 2 or around == 3):
            self.pixel(x, y, 255, 255, 255)
        if alive and around > 3:
            self.pixel(x, y, 0, 0, 0)
        if not alive and around == 3:
            self.pixel(x, y, 255, 255, 255)
        

    def render(self):
        for x in range(0, 100):
            for y in range(0, 100):
                self.checkPaint(x, y)

        


pygame.init()
screen = pygame.display.set_mode((100, 100))

r = Life(screen)
r.initialContent()

running = True
while running:
  r.copy()
  r.clear()
  r.render()

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False