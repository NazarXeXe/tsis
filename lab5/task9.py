from functools import reduce
from re import compile, findall, sub
if __name__ == "__main__":
    print(
        reduce(
            lambda a, b: f"{a} {b}",
            findall(
                compile('[A-Z][^A-Z]+'),
                input()
            )
        )
    )