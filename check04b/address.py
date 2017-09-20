"""
This file contains the following classes:
    CreditCard
    Address

and then it contains a main function.

Your task it to break it into three files, then tar them up, and submit.
"""

class Address:
    """ Contains a street address """
    def __init__(self):
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    def display(self):
        print(self.street)
        print("{}, {} {}".format(self.city, self.state, self.zip))