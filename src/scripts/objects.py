from typing import Union
import pygame
from constants import *


class Point:
    def __init__(self, position):
        self.position = pygame.Vector2(position)

    def draw(self, surface):
        pygame.draw.circle(surface, RED, self.position, 3)

    def update(self, position):
        self.position.update(position)


class Joint:
    def __init__(self, parent: Union['Joint', Point], length):
        self.position = pygame.Vector2(0, 0)
        self.parent = parent

        self.length = length

    def draw(self, surface):
        pygame.draw.circle(surface, RED, self.position, 3)
        pygame.draw.line(surface, RED, self.position, self.parent.position)

    def follow_point(self):
        diff = self.position - self.parent.position
        distance = diff.length()
        diff_norm = diff.normalize()

        self.position -= diff_norm * (distance - self.length)


class JointChain:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass