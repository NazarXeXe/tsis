from functools import reduce
from typing import List

import db
import typer
from rich.table import Table
from rich import print
app = typer.Typer()

@app.command()
def search(q: List[str]):
    with db.connect() as connection:
        table = Table("user", "phone")
        for row in db.search(connection, reduce(lambda a,b: f"{a} {b}", q)):
            table.add_row(*row)
        print(table)

@app.command()
def all():
    with db.connect() as connection:
        table = Table("user", "phone")
        for row in db.all(connection):
            table.add_row(*row)
        print(table)

@app.command()
def page(thepage: int = 1):
    with db.connect() as connection:
        table = Table("user", "phone")
        for row in db.page(connection, 30, thepage-1):
            table.add_row(*row)
        print(table)

if __name__ == "__main__":
    app()
