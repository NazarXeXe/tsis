from re import compile, findall
if __name__ == "__main__":
    print(
        findall(
            compile("[a-z]+_[a-z]+"),
            input(),
        )
    )