
import math

if __name__ == "__main__":
    n = int(input('Num of sides: '))
    s = int(input('Len of sides: '))

    A = 1/4 * math.sqrt(n*(n+(2*math.sqrt(n)))) * (s*s)
    print(A)