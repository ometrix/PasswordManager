import typer 

def greeting(name: str):
    print(f'Hello {name}!')

if __name__ == '__main__':
    typer.run(greeting)