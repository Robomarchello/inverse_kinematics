import pygame
from pygame.locals import MOUSEMOTION
from objects import JointChain
from constants import *


class Stickman:
    def __init__(self):
        self.body = pygame.Rect(300, 100, 75, 175)
        self.head = pygame.Rect(0, 0, HEAD_RADIUS, HEAD_RADIUS)
        self.head.bottom = self.body.top - 10
        self.head.centerx = self.body.centerx
        
        self.leg_left_rect = pygame.Rect(0, 0, 25, 25)
        self.leg_right_rect = pygame.Rect(0, 0, 25, 25)

        self.leg_left_rect.bottomleft = self.body.bottomleft        
        self.leg_right_rect.bottomright = self.body.bottomright

        self.leg_left = JointChain(self.leg_left_rect.center, 2, 100)
        self.leg_right = JointChain(self.leg_right_rect.center, 2, 100)

        self.leg_left_target = (
            self.body.left,# - 40, 
            self.body.bottom + 150
        )
        self.leg_right_target = (
            self.body.right,# + 40, 
            self.body.bottom + 130
        )

    def draw(self, surface):
        pygame.draw.rect(
            surface, 
            (0, 0, 0), 
            self.body, 
            border_top_left_radius=25,
            border_top_right_radius=25
            )

        self.draw_leg(surface, self.leg_left.get_points())
        self.draw_leg(surface, self.leg_right.get_points())

        pygame.draw.circle(surface, BLACK, self.head.center, HEAD_RADIUS / 2)

    def draw_leg(self, surface, points):
        for i in range(len(points)):
            if i < len(points) - 1:
                pygame.draw.line(surface, BLACK, points[i], points[i + 1], 30)

            pygame.draw.circle(surface, BLACK, points[i], 15)

    def update(self):
        self.head.bottom = self.body.top - 5
        self.head.centerx = self.body.centerx

        self._update_legs()

    def _update_legs(self):
        self.leg_left_rect.bottomleft = self.body.bottomleft        
        self.leg_right_rect.bottomright = self.body.bottomright

        self.leg_left.origin = self.leg_left_rect.center
        self.leg_right.origin = self.leg_right_rect.center

        self.leg_left.set_target(self.leg_left_target)
        self.leg_right.set_target(self.leg_right_target)
        
        self.leg_left.update()
        self.leg_right.update()

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.body.center = event.pos