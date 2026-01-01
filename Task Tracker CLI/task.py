import click
@click.command()
def hello():
    click.echo("Task Tracker CLI Ready!")
if __name__=="__main__":
    hello()