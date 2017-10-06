class Phone():
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")

    def dipslay(self):
        print("\nPhone info:\n({}){}-{}".format(self.area_code,
                                              self.prefix,
                                              self.suffix))

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ""

    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        super().dipslay()
        print("{}".format(self.email))


def main():
    print("Phone:")
    phone1 = Phone()
    phone1.prompt_number()
    phone1.dipslay()

    print("\nSmart phone:")
    sphone1 = SmartPhone()
    sphone1.prompt()
    sphone1.display()

if __name__ == "__main__":
    main()
