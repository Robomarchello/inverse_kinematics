import pygame
from pygame.locals import *
from constants import * 
from objects import Point, Joint, JointChain
from stickman import Stickman


class App():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREENSIZE)

        self.center = pygame.Vector2(384, 384)
        #self.joint_chain = JointChain(self.center, 3, 100)

        self.stickman = Stickman()

    def loop(self):
        while True:
            self.handle_events()

            self.screen.fill((255, 255, 255))
            
            # self.joint_chain.update()
            # self.joint_chain.draw(self.screen)

            self.stickman.draw(self.screen)
            self.stickman.update()

            pygame.display.update()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
            
            self.stickman.handle_event(event)
            
            # if event.type == MOUSEMOTION:
            #     self.joint_chain.set_target(event.pos)

    def get_dt(self):
        delta_time = self.clock.get_time() / 1000

        if delta_time > 0.1:
            delta_time = 0.1

        return delta_time


if __name__ == '__main__':
    App().loop()