from re import findall, compile
if __name__ == "__main__":
    print(
        findall(
            compile("a.+b"),
            input()
        )
    )
    