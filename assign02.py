###########################################################
# Assignment 02
# Colin Jensen
###########################################################

# Take in a user-supplied filename and return a parsed list
# of lines from the data file. 
def parse_file(filename):
    with open(filename,'r') as f:
        return [line.split(",") for line in f][1:]

# Take in data about electricity rates and return the
# average of all the rates, the highest rate, and the 
# lowest rate.
def rate_info(data):
    comm_rates = [float(line[6]) for line in data]
    avg_comm_rate = sum(comm_rates)/len(comm_rates)
    
    highest = data[comm_rates.index(max(comm_rates))]
    highest_string = (highest[2] 
                      + ' (' 
                      + highest[0] 
                      + ', ' 
                      + highest[3] 
                      + ') - $' 
                      + str(float(highest[6])))
    
    lowest = data[comm_rates.index(min(comm_rates))]
    lowest_string = (lowest[2] 
                      + ' (' 
                      + lowest[0] 
                      + ', ' 
                      + lowest[3] 
                      + ') - $' 
                      + str(float(lowest[6])))
    
    return {'avg': avg_comm_rate, 'high': highest_string, 'low': lowest_string}

def main():
    # Get filname
    filename = input("Please enter the data file: ")

    # Parse file
    data = parse_file(filename)

    # Find the average commerical rate, highest rate, and lowest rate
    rates = rate_info(data)
    
    print("\nThe average commercial rate is: {}".format(rates['avg']))
    print("\nThe highest rate is:\n{}".format(rates['high']))
    print("\nThe lowest rate is:\n{}".format(rates['low']))

if __name__ == "__main__":
    main()