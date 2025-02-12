
from datetime import datetime


if __name__ == "__main__":

    print('Format: hours:minutes:seconds')
    first = datetime.strptime(
        input('Enter the first date: ', ), "%H:%M:%S"
    )
    second = datetime.strptime(
        input('Enter the second date: ', ), "%H:%M:%S"
    )

    print((max(first,second) - min(first,second)).total_seconds())
