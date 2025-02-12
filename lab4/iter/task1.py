def genSqr(n: int):
    for i in range(n , 1):
        yield i**2

if __name__ == "__main__":
    n = int(input('N: '))
    print(list(genSqr(n)))