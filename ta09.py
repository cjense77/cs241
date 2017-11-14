class BalanceError(Exception):
    def __init__(self, message=''):
        super().__init__(message)

class OutOfChecks(Exception):
    def __init__(self, message=''):
        super().__init__(message)

class CheckingAccount:
    def __init__(self, starting_balance=0, num_checks=0):
        if starting_balance < 0:
            raise BalanceError('Negative account balance :(')
        self.balance = starting_balance
        self.check_count = num_checks

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount

    def write_check(self, amount):
        if self.check_count < 1:
            raise OutOfChecks('You\'re out of checks!')
        elif amount > self.balance:
            raise BalanceError('Can\'t write a check that large!')
        self.balance -= amount
        self.check_count -= 1

    def display(self):
        print('Balance: ${:.2f}\nChecks left: {}'.format(self.balance,
                                                    self.check_count))

    def apply_for_credit(self, amount):
        raise NotImplementedError


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))

            try:
                acc = CheckingAccount(balance, num_checks)
            except BalanceError as e:
                print(e)
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            amount = float(input("Amount: "))

            try:
                acc.write_check(amount)
            except BalanceError:
                print('You can\'t write a check that large!')
            except OutOfChecks:
                more_checks = input('You\'re out of checks. Would you like to purchase more? (y/n) ')
                if more_checks == 'y':
                    acc.balance -= 5
                    acc.check_count += 25
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()