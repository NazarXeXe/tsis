import typer
import db

import delete
import push
import query

app = typer.Typer()

app.add_typer(query.app, name='query')
app.add_typer(push.app, name='push')
app.add_typer(delete.app, name='delete')

@app.command(help='Initialize table.')
def init():
    with db.connect() as c:
        db.init_table(c)

if __name__ == "__main__":
    app()
