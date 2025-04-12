from typing import Annotated

import typer
import db
app = typer.Typer()

@app.command()
def delete(user: Annotated[
    str, typer.Option(prompt="User")
]):
    with db.connect() as connection:
        db.delete(connection, user)

if __name__ == "__main__":
    app()
