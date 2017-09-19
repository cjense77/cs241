def main():
    with open("text.txt","r") as f:
        read = [line.split() for line in f]
        lines = len(read)
        words = len([word for line in read for word in line])

    print("The file contains {} lines and {} words.".format(lines,words))

if __name__ == "__main__":
    main()