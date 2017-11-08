class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__("error message")


def get_inverse(n):
    try:
        n = int(n)
        if n < 0:
            raise NegativeNumberError
        print('The result is: {}'.format(1/n))
    except ValueError:
        print('Error: The value must be a number')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
    except NegativeNumberError:
        print('Error: The value cannot be negative')


def main():
    num = input('Enter a number: ')
    get_inverse(num)


if __name__ == '__main__':
    main()
