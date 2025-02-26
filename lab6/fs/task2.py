from os import path, access, R_OK, W_OK, X_OK

if __name__ == "__main__":
    thePath = input("Enter directory path to check: ")
    if not path.exists(thePath):
        print("Invalid path to check.")
        exit(0)

    print(
        f"Is readable: {access(thePath, R_OK)}",
        f"Is writable: {access(thePath, W_OK)}",
        f"Is executable: {access(thePath, X_OK)}",
        sep="\n"
    )
