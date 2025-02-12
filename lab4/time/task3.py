
from datetime import datetime


if __name__ == "__main__":

    print('Format: hours:minutes:seconds')
    date = datetime.strptime(
        input('Enter the date: ', ), "%H:%M:%S"
    )
    print(
        date.hour * (60 * 60  * 1000) +
        date.minute * (60 * 1000) +
        date.second * 1000
    )