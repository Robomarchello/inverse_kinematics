import pygame
from pygame.locals import *
from constants import * 
from objects import Point, Joint, JointChain


class App():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREENSIZE)

        self.point = Point((1, 0))
        self.joint = Joint(self.point, 100)
        self.joint1 = Joint(self.joint, 100)
        self.joint2 = Joint(self.joint1, 100)

        self.center = pygame.Vector2(384, 384)

    def loop(self):
        while True:
            self.handle_events()

            self.screen.fill((255, 255, 255))

            self.point.draw(self.screen)
            self.joint.draw(self.screen)
            self.joint.follow_point()
            self.joint1.draw(self.screen)
            self.joint1.follow_point()
            self.joint2.draw(self.screen)
            self.joint2.follow_point()

            displacement = self.center - self.joint2.position
            self.joint.position += displacement
            self.joint1.position += displacement
            self.joint2.position += displacement
            
            pygame.display.update()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
            
            if event.type == MOUSEMOTION:
                self.point.update(event.pos)

    def get_dt(self):
        delta_time = self.clock.get_time() / 1000

        if delta_time > 0.1:
            delta_time = 0.1

        return delta_time

if __name__ == '__main__':
    App().loop()