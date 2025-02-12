
def downTrend(to: int):
    for i in range(to, -1, -1):
        yield i

if __name__ == "__main__":
    n = int(input('N: '))
    print(
        list(
            downTrend(n)
        )
    )