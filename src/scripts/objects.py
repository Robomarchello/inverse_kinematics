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

    def follow_point(self):
        # imposter function
        pass


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

        if distance == 0:
            return

        diff_norm = diff.normalize()

        stretch = (distance - self.length)

        self.position -= diff_norm * stretch


class JointChain:
    def __init__(self, position, joint_num, joint_length):
        self.position = position
        self.target_point = Point((0, 0))

        # generate joints
        self.joints = []
        
        for i in range(joint_num):
            if i == 0:
                joint = Joint(self.target_point, joint_length)
            else:
                joint = Joint(self.joints[i - 1], joint_length)
            self.joints.append(joint)

    def update(self):
        for joint in self.joints:
            joint.follow_point()
        
        displacement = self.position - self.joints[-1].position
        for joint in self.joints:
            joint.position += displacement

        self.target_point.position += displacement

    def get_points(self):
        points = []
        
        points.append(self.target_point.position)

        for joint in self.joints:
            points.append(joint.position)

        return points

    def draw(self, surface):
        for joint in self.joints:
            joint.draw(surface)

        self.target_point.draw(surface)

    def set_target(self, position):
        self.target_point.update(position)