from functools import reduce
from typing import List

import typer
import db

import push
import query

app = typer.Typer()

app.add_typer(push.app, name="push")
app.add_typer(query.app, name="query")

@app.command(help="Initialize table.")
def init():
    with db.connect() as connection:
        db.init(connection)


if __name__ == "__main__":
    app()