import pygame
from pygame.locals import MOUSEMOTION
from objects import JointChain
from constants import *


class Stickman:
    def __init__(self):
        self.body = pygame.Rect(300, 100, 75, 200)
        
        self.leg_left_rect = pygame.Rect(0, 0, 25, 25)
        self.leg_right_rect = pygame.Rect(0, 0, 25, 25)

        self.leg_left_rect.bottomleft = self.body.bottomleft        
        self.leg_right_rect.bottomright = self.body.bottomright

        self.leg_left = JointChain(self.leg_left_rect.center, 2, 100)
        self.leg_right = JointChain(self.leg_right_rect.center, 2, 100)

        self.leg_left_target = (
            self.body.left - 40, 
            self.body.bottom + 150
        )
        self.leg_right_target = (
            self.body.right + 40, 
            self.body.bottom + 130
        )

        self.legs = []

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.body, border_radius=25)

        self.draw_leg(surface, self.leg_left.get_points())
        self.draw_leg(surface, self.leg_right.get_points())

    def draw_leg(self, surface, points):
        for i in range(len(points) - 1):
            pygame.draw.line(surface, BLACK, points[i], points[i + 1], 25)

            pygame.draw.circle(surface, BLACK, points[i], 12)
            #pygame.draw.circle(surface, BLACK, points[i + 1], 12)

    def update(self):
        self.leg_left_rect.bottomleft = self.body.bottomleft        
        self.leg_right_rect.bottomright = self.body.bottomright

        self.leg_left.position = self.leg_left_rect.center
        self.leg_right.position = self.leg_right_rect.center

        self.leg_left.set_target(self.leg_left_target)
        self.leg_right.set_target(self.leg_right_target)
        
        self.leg_left.update()
        self.leg_right.update()
        



    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.body.center = event.pos