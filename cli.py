import click

@click.group()
def main():
    """simple CLI that will greet you"""
    pass

@main.command()
@click.argument('name')
def greet(name):
    """This will greet you back with your name"""
    click.echo(f"Hello, {name}")

if __name__ == "__main__":
    main()
