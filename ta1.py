def main():
    seq1 = input("Please enter you DNA sequence: ").upper()
    numA = seq1.count('A')
    print("The sequence {0} has {1} A's".format(seq1,numA))
    
    seq2 = input("\nPlease enter you friend's DNA sequence: ").upper()
    
    matches = 0
    for item1,item2 in zip(seq1,seq2):
        if item1 == item2:
            matches += 1
    percent = matches/len(seq1) * 100
        
    print("You and your friend had {0} matches for {1}%".format(matches,percent))
    
    
if __name__ == "__main__":
    main()