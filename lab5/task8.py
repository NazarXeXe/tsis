from re import compile, findall, sub
if __name__ == "__main__":
    print(
        findall(
            compile('[A-Z][^A-Z]+'),
            input()
        )
    )
