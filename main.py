import typer
from rich.console import Console
from rich.table import Table
from password_manager.model import Entry
from password_manager.database import create, read, update, delete
from password_manager.pass_gen import passwd

# Crea una consola y una aplicación de Typer
console = Console()
app = typer.Typer()

# Define una función de línea de comandos para agregar una entrada
@app.command(short_help='adds a contact')
def add(plataform: str, user: str):
    # Genera una contraseña
    password = passwd
    # Muestra un mensaje de confirmación y agrega la entrada a la base de datos
    typer.echo(f"Adding {plataform}, {user}, {password}")
    entry = Entry (plataform, user, password)
    create(entry)
    # Muestra todas las entradas
    show()

# Define una función de línea de comandos para mostrar todas las entradas
@app.command(short_help='shows all entrys')
def show():
    typer.echo(f"All Entrys")
    # Obtiene todas las entradas de la base de datos
    entrys = read()

    # Muestra el título de la aplicación
    console.print("[bold magenta]Password Manager[/bold magenta]", "?")

    # Si no hay entradas, muestra un mensaje de error
    if len(entrys) == 0:
        console.print("[bold red] No entrys to show [/bold red]")
    # Si hay entradas, las muestra en una tabla
    else:
        table = Table(show_header=True, header_style="bold blue", show_lines=True)
        table.add_column("#", style="dim", width=3, justify="center")
        table.add_column("Plataform", min_width=20, justify="center")
        table.add_column("User", min_width=20, justify="center")
        table.add_column("Password", min_width=12, justify="center")

        # Agrega cada entrada a la tabla
        for idx, entry in enumerate(entrys, start=1):
            table.add_row(str(idx), f'[cyan]{entry.plataform}[/cyan]', f'[cyan]{entry.user}[/cyan]', f'[green]{entry.password}[/green]')
        # Imprime la tabla en la consola
        console.print(table)

# Define una función de línea de comandos para editar una entrada
@app.command(short_help='edits a entry')
def edit(position: int, plataform: str = None, user: str = None, password: str = None):
    # Muestra un mensaje de confirmación y actualiza la entrada en la base de datos
    typer.echo(f"Editing {position}")
    update(position, plataform, user, password)
    # Muestra todas las entradas
    show()

# Define una función de línea de comandos para eliminar una entrada
@app.command(short_help='removes a entry')
def remove(position: int):
    # Muestra un mensaje de confirmación y elimina la entrada de la base de datos
    typer.echo(f"Removing {position}")
    delete(position)
    # Muestra todas las entradas
    show()

# Ejecuta la aplicación de Typer
if __name__ == "__main__":
    app()
