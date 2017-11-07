def main():
    valid_number = False
    while not valid_number:
        try:
            num = int(input('Enter a number: '))
            valid_number = True
        except:
            print('The value entered is not valid')

    print('Result: {}'.format(num * 2))

if __name__ == '__main__':
    main()