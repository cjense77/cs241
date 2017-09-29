"""
Colin Jensen
Assignment 03

Create and implement a robot class. Each object in the class
can move in all four directions, fire, and print out it's
position and fuel levels. 
"""

# Define Robot class with members functions to move, fire, and
# print status.
class Robot:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100
    
    def left(self):
        self.x = self.x - 1
        self.fuel = self.fuel - 5
        
    def right(self):
        self.x = self.x + 1
        self.fuel = self.fuel - 5
        
    def up(self):
        self.y = self.y - 1
        self.fuel = self.fuel - 5
        
    def down(self):
        self.y = self.y + 1
        self.fuel = self.fuel - 5
        
    def fire(self):
        print("Pew! Pew!")
        self.fuel = self.fuel - 15
        
    def status(self):
        print("({}, {}) - Fuel: {}".format(self.x,
                                           self.y,
                                           self.fuel))

# Create a robot object and interpret commands from
# the user.
def main():
    robot = Robot()

    # Dictionary storing robot commands
    command_index = {'left': [robot.left, 5],
                     'right': [robot.right, 5],
                     'up': [robot.up, 5],
                     'down': [robot.down, 5],
                     'status': [robot.status, 0],
                     'fire': [robot.fire, 15]}
    
    again = True
    while(again):
        command = input('Enter command: ')
        if command in command_index:
            if robot.fuel >= command_index[command][1]:
                command_index[command][0]()
            else:
                print('Insufficient fuel to perform action')
        elif command == 'quit':
            again = False

    print('Goodbye.')

if __name__ == "__main__":
    main()