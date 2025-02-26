if __name__ == "__main__":

    thePath = input("Enter file path: ")
    with open(thePath, 'r') as file:
        print(len(file.readlines()))