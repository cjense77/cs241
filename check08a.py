class GPA:
    def __init__(self):
        self.gpa = 0.0

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, new_gpa):
        if new_gpa < 0:
            new_gpa = 0
        elif new_gpa > 4.0:
            new_gpa = 4.0
        self.gpa = new_gpa

    def get_letter(self):
        if self.gpa == 4.0:
            return 'A'
        elif 3.0 <= self.gpa < 4.0:
            return 'B'
        elif 2.0 <= self.gpa < 3.0:
            return 'C'
        elif 1.0 <= self.gpa < 2.0:
            return 'D'
        else:
            return 'F'

    def set_letter(self, value):
        value = value.upper()
        if value == 'A':
            self.gpa = 4.0
        elif value == 'B':
            self.gpa = 3.0
        elif value == 'C':
            self.gpa = 2.0
        elif value == 'D':
            self.gpa = 1.0
        else:
            self.gpa = 0.0


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()
