from datetime import datetime, timedelta

if __name__ == "__main__":

    dur = timedelta(days=1)
    current = datetime.today()
    print(
        current - dur,
        current,
        current + dur
    )
