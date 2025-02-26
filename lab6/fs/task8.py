from shutil import rmtree
from os import path, remove, W_OK, access

if __name__ == "__main__":
    thePath = input("Enter the path to delete: ")
    if not path.exists(thePath):
        print("Invalid path.")
        exit()
    if not access(thePath, W_OK):
        print("Insufficient permission(s) to delete the file.")
        exit()
    if path.isdir(thePath):
        rmtree(thePath)
    else:
        remove(thePath)
