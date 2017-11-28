"""
File: velocity.py
Author: Colin Jensen
Contains class to store a moving object's velocity
"""

class Velocity:
    """
    Class to store x, y, and angular components of velocity
    """
    def __init__(self, dx=0, dy=0, da=0):
        """
        Initialize Velocity object
        :param dx: int
        :param dy: int
        :param da: int angular velocity in degrees/frame
        """
        self.dx = dx
        self.dy = dy
        self.da = da
