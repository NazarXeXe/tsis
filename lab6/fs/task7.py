from os import path

if __name__ == "__main__":

    a = input("From: ")
    b = input("To: ")

    if not (path.exists(a) and path.exists(b)):
        print("Invalid path(s).")
        exit(0)

    with open(a, 'r') as frm:
        with open(b, 'w') as to:
            to.write(frm.read())