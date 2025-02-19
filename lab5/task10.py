from functools import reduce
from re import compile, findall

if __name__ == "__main__":

    print(
        reduce(
            lambda a, b: f"{a}_{b[0].lower() + b[1:len(b)]}",
            findall(
                compile('[A-Z][^A-Z]+'),
                input()
            )
        )
    )
