"""Console script for sumtools."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("sumtools")
    click.echo("=" * len("sumtools"))
    click.echo("a suite for summary level GWAS downstream analysis")


if __name__ == "__main__":
    main()  # pragma: no cover

