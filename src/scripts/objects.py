from typing import Union
import pygame
from .constants import *


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

        if distance == 0:
            return

        diff_norm = diff.normalize()

        stretch = (distance - self.length)

        self.position -= diff_norm * stretch


class JointGroup:
    def __init__(self, origin, target_point:Point, joints):
        self.origin = origin

        self.target_point = target_point
        self.joints = joints

    def draw(self, surface):
        pass

    def update(self):
        for joint in self.joints:
            joint.follow_point()
        
        displacement = self.origin - self.joints[-1].position
        for joint in self.joints:
            joint.position += displacement
        self.target_point.position += displacement

    def get_points(self):
        points = []
        
        points.append(self.target_point.position)
        for joint in self.joints:
            points.append(joint.position)

        return points

    def set_target(self, position):
        self.target_point.update(position)


class JointChain(JointGroup):
    def __init__(self, origin, joint_num, joint_length):
        target_point = Point((0, 0))

        # generate joints
        joints = []
        
        for i in range(joint_num):
            if i == 0:
                joint = Joint(target_point, joint_length)
            else:
                joint = Joint(joints[i - 1], joint_length)
            joints.append(joint)

        super().__init__(origin, target_point, joints)

    def draw(self, surface):
        for joint in self.joints:
            joint.draw(surface)

        self.target_point.draw(surface)


class PhysicsJointChain(JointGroup):
    def __init__(self, origin, joint_num, joint_length):
        self.target_point = Point(origin)

        # generate joints
        joints = []
        
        for i in range(joint_num):
            if i == 0:
                joint = Joint(self.target_point, joint_length)
            else:
                joint = Joint(joints[i - 1], joint_length)

            joints.append(joint)

        self.velocity = pygame.Vector2(0, 0)

        super().__init__(origin, self.target_point, joints)

    def draw(self, surface):
        self.target_point.draw(surface)

        for joint in self.joints:
            joint.draw(surface)

    def update(self):
        for joint in self.joints:
            joint.position += self.velocity

            joint.follow_point()
        
        self.velocity *= 0
