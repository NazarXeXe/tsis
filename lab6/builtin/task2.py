from re import findall, compile
if __name__ == "__main__":
    s = input()
    print(
        f"Upper: {len(findall(compile("[A-Z]"), s))}",
        f"Lower: {len(findall(compile("[a-z]"), s))}",
        sep="\n"
    )
