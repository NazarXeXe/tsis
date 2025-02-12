
FORMULA = lambda a,b,h: ((a+b)/2)*h

if __name__ == "__main__":
    a = int(input('A: '))
    b = int(input('B: '))
    h = int(input('h: '))

    print(FORMULA(a,b,h))