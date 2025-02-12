
def gen(n: int):
    for i in range(n+1):
        if i % 4 == 0 and i % 3 == 0:
            yield i


if __name__ == "__main__":
    n = int(input('N: '))
    print(list(gen(n)))
