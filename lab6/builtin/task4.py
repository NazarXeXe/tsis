from time import sleep
from math import sqrt
if __name__ == "__main__":
    tosqr, sleepIn = tuple(map(lambda x: float(x), input().split(" ")))

    sleep(sleepIn / 1000)

    print(sqrt(tosqr))