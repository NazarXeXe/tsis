from re import findall, compile
if __name__ == "__main__":
    s = input()
    print(findall(
        compile("a{2}b{3}+"),
        s
    ))
    