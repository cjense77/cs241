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

    def move(self, dx, dy):
        if self.fuel >= 5:
            self.fuel -= 5

            self.x += dx
            self.y += dy
        else:
            print("Insufficient fuel to perform action")


    
    def left(self):
        self.move(-1, 0)
        
    def right(self):
        self.move(1, 0)
        
    def up(self):
        self.move(0, -1)
        
    def down(self):
        self.move(0, 1)
        
    def fire(self):
        if self.fuel >= 15:
            self.fuel -= 15
            print("Pew! Pew!")
        else:
            print("Insufficient fuel to perform action")

        
    def status(self):
        print("({}, {}) - Fuel: {}".format(self.x,
                                           self.y,
                                           self.fuel))

# Create a robot object and interpret commands from
# the user.
def main():
    robot = Robot()

    # Dictionary storing robot commands
    command_index = {'left': robot.left,
                     'right': robot.right,
                     'up': robot.up,
                     'down': robot.down,
                     'status': robot.status,
                     'fire': robot.fire}
    
    again = True
    while(again):
        command = input('Enter command: ')
        if command == "quit":
            again = False
        elif command in command_index:
            command_index[command]()



    print('Goodbye.')

if __name__ == "__main__":
    main()