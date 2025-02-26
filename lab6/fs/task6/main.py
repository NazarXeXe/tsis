if __name__ == "__main__":
    theDir = input("Input directory path to generate: ")
    for path in map(lambda x: f"{theDir}{chr(x)}.txt",range(65, 91)):
        open(path, 'x').close()