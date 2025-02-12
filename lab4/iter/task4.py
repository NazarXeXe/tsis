
def sqrs(a: int, b: int):

    for i in range(min(a, b), max(a, b)+1):
        yield i**2


if __name__ == "__main__":
    a = int(input('A: '))
    b = int(input('B: '))
    print(
        list(
            sqrs(a, b)
        )
    )