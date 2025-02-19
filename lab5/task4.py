from re import compile, findall
if __name__ == "__main__":
    print(
        findall(
            compile("[A-Z]+_[a-z]+"),
            input(),
        )
    )