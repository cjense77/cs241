class GPA:
    def __init__(self):
        self._set_gpa(0.0)

    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, new_gpa):
        if new_gpa < 0:
            new_gpa = 0
        elif new_gpa > 4.0:
            new_gpa = 4.0
        self._gpa = new_gpa

    gpa = property(_get_gpa, _set_gpa)

    def _get_letter(self):
        if self._gpa == 4.0:
            return 'A'
        elif 3.0 <= self._gpa < 4.0:
            return 'B'
        elif 2.0 <= self._gpa < 3.0:
            return 'C'
        elif 1.0 <= self._gpa < 2.0:
            return 'D'
        else:
            return 'F'

    def _set_letter(self, value):
        value = value.upper()
        if value == 'A':
            self._gpa = 4.0
        elif value == 'B':
            self._gpa = 3.0
        elif value == 'C':
            self._gpa = 2.0
        elif value == 'D':
            self._gpa = 1.0
        else:
            self._gpa = 0.0

    @property
    def letter(self):
        return self._get_letter()

    @letter.setter
    def letter(self, letter):
        self._set_letter(letter)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()
