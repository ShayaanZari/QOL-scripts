import click
import re
from pathlib import Path
from typing import Iterator

def get_md_files(path: Path) -> Iterator[Path]:
    # A generator that yields Path objects to prevent unaesthetic singleton array logic >:D
    if path.is_file():
        if path.suffix == '.md':
            yield path
    elif path.is_dir():
        yield from path.glob('*.md') # essentially ls
    else:
        print(f"{path} is not a valid directory or a Markdown file.")

def count_entities(path: Path) -> int:
    count = 0
    try:
        with path.open('r') as fd: # C still bright in my heart
            for line in fd:
                if re.match(r'^[-]\s+', line): # ^[-] matches line starting with dash, \s+ matches at least one space after dash
                    count += 1
    except Exception as e:
        click.echo(f"Error reading {path.name}: {e}", err=True) # what a fancy print statement
    return count

@click.command()
@click.argument('path', type=click.Path(exists=True, path_type=Path)) # much more concise than argparse
def cli(path: Path):
    """
    Count entities in markdown file(s).

    path: The path to a .md file or a directory containing .md files.
    """
    total_entities = 0
    results = []

    for file_path in get_md_files(path):
        count = count_entities(file_path)
        if count > 0:
            results.append((file_path.name, count))
            total_entities += count

    if not results:
        click.echo("No entities found.")
        return

    click.echo(f"{'FILENAME':<35} | {'ENTITIES'}") # width of 35
    click.echo("-" * 50) # print 50 times on a single line
    
    for name, count in sorted(results): # numerically sorted I think
        click.echo(f"{name:<35} | {count}")
    
    click.echo("-" * 50)
    click.secho(f"{'TOTAL':<35} | {total_entities}", fg='green', bold=True) # how convenient!

if __name__ == '__main__':
    cli()