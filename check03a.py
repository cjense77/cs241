class Student:
    def __init__(self, f_name, l_name, id_num):
        self.f_name = f_name
        self.l_name = l_name
        self.id_num = id_num
    
def prompt_student():
    f_name = input("Please enter your first name: ")
    l_name = input("Please enter your last name: ")
    id_num = input("Please enter your id number: ")
    
    return Student(f_name, l_name, id_num)
    
def display_student(user):
    print("\nYour information:\n{} - {} {}".format(user.id_num,
                                                 user.f_name,
                                                 user.l_name))
    
def main():
    user = prompt_student()
    
    display_student(user)
    
if __name__ == '__main__':
    main()