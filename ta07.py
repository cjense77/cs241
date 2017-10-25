from abc import ABC
from abc import abstractmethod


class Employee(ABC):
    def __init__(self, name=''):
        self.name = name

    @abstractmethod
    def display(self):
        print(self.name)

    @abstractmethod
    def get_paycheck(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name='', hourly_wage=0, hours=0):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours = hours

    def display(self):
        print('{} - ${}/hour'.format(self.name,
                                     self.hourly_wage))

    def get_paycheck(self):
        return self.hourly_wage * self.hours

class SalaryEmployee(Employee):
    def __init__(self, name='', salary=0):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print('{} - ${}/year'.format(self.name,
                                     self.salary))

    def get_paycheck(self):
        return self.salary / 24.0

def display_employee_data(employee):
    employee.display()
    print('Paycheck: ${:.2f}'.format(employee.get_paycheck()))


def main():
    employees = []

    command = ''
    while (command != 'q'):
        command = input('Enter command (h/s/q): ')

        if command == 'h':
            name = input('Enter name: ')
            wage = int(input('Enter wage: '))
            hours = int(input('Enter hours: '))
            employees.append(HourlyEmployee(name, wage, hours))
        elif command == 's':
            name = input('Enter name: ')
            salary = int(input('Enter salary: '))
            employees.append(SalaryEmployee(name, salary))
        print()

    for employee in employees:
        display_employee_data(employee)


if __name__ == '__main__':
    main()