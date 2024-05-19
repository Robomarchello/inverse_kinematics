import pygame
from constants import *


class Point:
    def __init__(self, position):
        self.position = position


class Joint:
    def __init__(self, parent: 'Joint' | Point, length):
        self.position = pygame.Vector2(0, 0)
        self.parent = parent

        self.length = length

    def draw(self, surface):
        pygame.draw.line(surface, RED, self.positon, self.parent.position)

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