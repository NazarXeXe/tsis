from functools import reduce
if __name__ == "__main__":
    print(
        reduce(lambda a,b: a*b, map(lambda x: int(x), input().split(" ")))
    )

