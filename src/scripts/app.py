import pygame
from pygame.locals import *
from constants import * 


class App():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREENSIZE)

        self.point_1 = pygame.Vector2(384, 384)
        self.point_2 = pygame.Vector2(384, 384)
        self.radius = 120

    def loop(self):
        while True:
            self.handle_events()

            self.screen.fill((255, 255, 255))

            pygame.draw.circle(self.screen, RED, self.point_1, 5)
            pygame.draw.circle(self.screen, RED, self.point_2, 5)

            diff = self.point_2 - self.point_1
            distance = diff.length()
            diff_norm = diff.normalize()

            self.point_2 -= diff_norm * (distance - self.radius)

            pygame.display.update()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
            
            if event.type == MOUSEMOTION:
                self.point_1.update(event.pos)

    def get_dt(self):
        delta_time = self.clock.get_time() / 1000

        if delta_time > 0.1:
            delta_time = 0.1

        return delta_time

if __name__ == '__main__':
    App().loop()