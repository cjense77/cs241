"""
File: velocity.py
Author: Colin Jensen
Contains class to store a moving object's velocity
"""

class Velocity:
    """
    Class to store x and y compnent of velocity
    """
    def __init__(self, dx = 0, dy = 0):
        """
        Initialize velocity
        :param dx:
        :param dy:
        """
        self.dx = dx
        self.dy = dy