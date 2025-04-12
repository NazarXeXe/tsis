import db
from typing import Annotated

import os
import csv as csvlib
import typer
from rich import print
from rich.progress import track

app = typer.Typer()

@app.command()
def csv(path: str):
    if os.path.exists(path) and os.path.isfile(path):
        with db.connect() as connection:
            with open(path) as csvFile:
                reader = csvlib.DictReader(csvFile)
                try:
                    for row in track(list(reader), show_speed=False):
                        db.push(connection, row['user'], row['phone'])
                    print("[green]Pushed into database.")
                except Exception as e:
                    connection.rollback()
                    raise e
    else:
        print("[red]Invalid path.")

@app.command()
def pair(
        user: Annotated[str, typer.Option(prompt=True)],
        phone: Annotated[str, typer.Option(prompt=True)]
):
    with db.connect() as connection:
        db.push(connection, user, phone)
        print("[green]Pushed into database.")

if __name__ == "__main__":
    app()
