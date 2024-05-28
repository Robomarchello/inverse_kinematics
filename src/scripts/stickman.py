import pygame
from pygame.locals import MOUSEMOTION
from .objects import JointChain, PhysicsJointChain
from .constants import *


class Stickman:
    def __init__(self):
        self.body = pygame.Rect(300, 300, *BODY_SIZE)
        self.shoulders = pygame.Rect(300, 300, 140, 32)

        self.head = pygame.Rect(0, 0, HEAD_RADIUS * 2, HEAD_RADIUS * 2)
        self.head.bottom = self.body.top - 10
        self.head.centerx = self.body.centerx

        self.hand_left_point = (
            self.body.left - 20,
            self.body.top
            )
        
        self.hand_right_point = (
            self.body.right + 20,
            self.body.top
            )
        
        self.hand_left = PhysicsJointChain(self.hand_left_point, 2, 65)
        self.hand_right = PhysicsJointChain(self.hand_right_point, 2, 65)
        
        leg_rect = pygame.Rect(0, 0, LEG_WIDTH, LEG_WIDTH)
        self.leg_left_rect = leg_rect.copy()
        self.leg_right_rect = leg_rect.copy()

        self.leg_left_rect.bottomleft = self.body.bottomleft        
        self.leg_right_rect.bottomright = self.body.bottomright

        self.leg_left = JointChain(self.leg_left_rect.center, 2, 100)
        self.leg_right = JointChain(self.leg_right_rect.center, 2, 100)

        self.leg_left_target = (
            self.body.left, 
            self.body.bottom + 150
        )
        self.leg_right_target = (
            self.body.right + 30,
            self.body.bottom + 130
        )

        self._update_hands()
        self._update_legs()

    def draw(self, surface):
        pygame.draw.rect(
            surface, 
            BLACK, 
            self.body,
            border_bottom_left_radius=BODY_RADIUS,
            border_bottom_right_radius=BODY_RADIUS
            )
        
        pygame.draw.rect(surface, BLACK, self.shoulders)

        self.draw_limb(surface, self.leg_left.get_points(), LEG_WIDTH)
        self.draw_limb(surface, self.leg_right.get_points(), LEG_WIDTH)

        self.draw_limb(surface, self.hand_left.get_points(), HAND_WIDTH)
        self.draw_limb(surface, self.hand_right.get_points(), HAND_WIDTH)

        pygame.draw.circle(surface, BLACK, self.head.center, HEAD_RADIUS)

    def draw_limb(self, surface, points, limb_width):
        for i in range(len(points)):
            if i < len(points) - 1:
                pygame.draw.line(surface, BLACK, points[i], points[i + 1], limb_width)

            pygame.draw.circle(surface, BLACK, points[i], limb_width // 2)

    def update(self):
        self.head.bottom = self.body.top - 5
        self.head.centerx = self.body.centerx

        self._update_legs()
        self._update_hands()

        self.shoulders.left = self.hand_left_point[0]
        self.shoulders.top = self.body.top - 3

    def _update_legs(self):
        self.leg_left_rect.bottomleft = self.body.bottomleft        
        self.leg_right_rect.bottomright = self.body.bottomright

        self.leg_left.origin = self.leg_left_rect.center
        self.leg_right.origin = self.leg_right_rect.center

        self.leg_left.set_target(self.leg_left_target)
        self.leg_right.set_target(self.leg_right_target)
        
        self.leg_left.update()
        self.leg_right.update()
    
    def _update_hands(self):
        self.hand_left_point = (
            self.body.left - 32,
            self.body.top + 10
            )

        self.hand_right_point = (
            self.body.right + 32,
            self.body.top + 10
            )
        
        self.hand_left.target_point.update(self.hand_left_point)
        self.hand_right.target_point.update(self.hand_right_point)

        self.hand_left.velocity.y += 1
        self.hand_right.velocity.y += 1

        self.hand_left.update()
        self.hand_right.update()

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.body.center = event.pos