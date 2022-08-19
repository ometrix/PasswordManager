import typer
from rich.console import Console
from rich.table import Table
from password_manager.model import Entry
from password_manager.database import create, read, update, delete
from password_manager.pass_gen import passwd

console = Console()
app = typer.Typer()

@app.command(short_help='adds a contact')
def add(plataform: str, user: str):
    password = passwd
    typer.echo(f"Adding {plataform}, {user}, {password}")
    entry = Entry (plataform, user, password)
    create(entry)
    show()

@app.command(short_help='shows all entrys')
def show():
    typer.echo(f"All Entrys")
    entrys = read()

    console.print("[bold magenta]Password Manager[/bold magenta]", "?")

    if len(entrys) == 0:
        console.print("[bold red] No entrys to show [/bold red]")
    else:
        table = Table(show_header=True, header_style="bold blue", show_lines=True)
        table.add_column("#", style="dim", width=3, justify="center")
        table.add_column("Plataform", min_width=20, justify="center")
        table.add_column("User", min_width=20, justify="center")
        table.add_column("Password", min_width=12, justify="center")

        for idx, entry in enumerate(entrys, start=1):
            table.add_row(str(idx), f'[cyan]{entry.plataform}[/cyan]', f'[cyan]{entry.user}[/cyan]', f'[green]{entry.password}[/green]')
        console.print(table)

@app.command(short_help='edits a entry')
def edit(position: int, plataform: str = None, user: str = None, password: str = None):
    typer.echo(f"Editing {position}")
    update(position, plataform, user, password)
    show()

@app.command(short_help='removes a entry')
def remove(position: int):
    typer.echo(f"Removing {position}")
    delete(position)
    show()

if __name__ == "__main__":
    app()

