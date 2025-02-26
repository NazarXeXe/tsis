from os import path

if __name__ == "__main__":

    thePath = input("Enter path: ")
    if not path.exists(thePath):
        print("Invalid path.")

    print(
        f"Absolute path: {path.abspath(thePath)}",
        f"Parent path: {path.dirname(thePath)}",
        sep="\n"
    )


