# Prompt the user for a positive number and keep prompting
# until a positive number is entered
def prompt_number():
    valid = False
    while(not valid):
        num = int(input("Enter a positive number: "))
        if num < 0:
            print("Invalid entry. The number must be positive.")
        else:
            print("")
            valid = True
    return num

# Return the sum of a list of numbers
def compute_sum(numbers):
    return sum(numbers)
    
def main():
    numbers = []
    while(len(numbers) < 3):
        numbers.append(prompt_number())
        
    print("The sum is: {}".format(compute_sum(numbers)))

if __name__ == "__main__":
    main()
#fav_num = int(input("What is you favourite number? ")) * 2
#print(fav_num)