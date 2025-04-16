
import typer
import phonenumbers
import db
from rich import print
from rich.progress import track
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def one(
        user: Annotated[str, typer.Option(prompt=True)],
        phone: Annotated[str, typer.Option(prompt=True)]
):
    if not phonenumbers.is_possible_number(phonenumbers.parse(phone)):
        print("[red]Invalid number.")
        return
    with db.connect() as connection:
        if db.exist(connection, user):
            db.replace(connection, phone, user)
            print(f"[green]Replaced {user}'s number into {phone}")
        else:
            db.push(connection, user, phone)
            print(f"[green]Created new entry for {user}.")

@app.command()
def multi(times: int):
    pairs = list(
        map(
            lambda _: (input('Enter username: '), input('Enter phone: ')),
            range(0, times)
        )
    )
    with db.connect() as connection:
        for pair in track(pairs):
            if not phonenumbers.is_possible_number(phonenumbers.parse(pair[1])):
                print(f"[yellow] {pair[1]}'s phone number {pair[1]} is invalid skipping....")
            else:
                if db.exist(connection, pair[0]):
                    db.replace(connection, pair[1], pair[0])
                    print(f"[yellow]Replacing {pair[0]}'s phone number to {pair[1]}.")
                else:
                    db.push(connection, pair[0], pair[1])

if __name__ == "__main__":
    app()