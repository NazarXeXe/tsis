import re
if __name__ == "__main__":
    s = input()
    print(re.sub(re.compile("[ ,.]"), ":", s))