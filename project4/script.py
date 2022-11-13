#!/usr/bin/env python
"""
proj 4 script
"""
import requests
import click
import numpy as np


@click.group()
def cli():
    """
    Coursera Rank Cli
    """


@cli.command()
@click.option("--n", default=10, help="The number of courses to return")
@click.option("--subject", default="", help="The subject name of the courses to return")
def get_top_n_best_courses(n, subject):
    """Returns the top N best courses"""

    payload = {"n": n, "subject": subject}
    response = requests.get(
        "https://08th92b4b8.execute-api.us-east-1.amazonaws.com/Prod",
        params=payload,
        timeout=5,
    )
    print(response.text)


if __name__ == "__main__":
    cli()