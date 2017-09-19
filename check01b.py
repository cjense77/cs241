###################################################
# Checkpoint 01b
#
# Colin Jensen
###################################################

def main():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    age1 = int(age) + 1
    
    print("\nHello {0}, you are {1} years old.".format(name, age))
    print("On your next birthday, you will be {0}.".format(age1))
    
if __name__ == '__main__':
    main()