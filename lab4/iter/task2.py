
if __name__ == "__main__":

    n = int(input("N: "))
    print(
        list(
            filter(
                lambda x: x % 2 == 0,
                [x for x in range(n)]
            )
        )
    )
