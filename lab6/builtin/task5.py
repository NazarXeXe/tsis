from functools import reduce

def allElementsAreTrue(tuple: tuple[bool, ...]):
    return reduce(lambda a,b: a and b, tuple)

if __name__ == "__main__":
    print(
        allElementsAreTrue(tuple(map(lambda x: x.lower() == "true", input().split(" "))))
    )