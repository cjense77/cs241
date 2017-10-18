class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def prompt(self):
        self.x = input("Enter x: ")
        self.y = input("Enter y: ")

    def display(self):
        print("Center:\n({}, {})".format(self.x, self.y))

class Circle:
    def __init__(self):
        self.radius = 0
        self.center = Point()

    def prompt(self):
        self.center.prompt()
        self.radius = input("Enter radius: ")

    def display(self):
        self.center.display()
        print("Radius: {}".format(self.radius))

def main():
    c = Circle()
    c.display()
    c.prompt()
    c.display()

if __name__ == "__main__":
    main()