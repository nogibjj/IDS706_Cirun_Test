#!/usr/bin/env python
"""
proj 2
"""
import requests
import click
import numpy as np


@click.group()
def cli():
    """
    Sort cli
    """


@cli.command()
@click.option(
    "--file_path", default="list.csv", help="The path of the csv file to sort"
)
def get_sorted_arr(file_path):
    """Get sorted array"""
    with open(file_path, encoding="UTF-8") as file_name:
        array = np.loadtxt(file_name, delimiter=",")

    # print(array)
    payload = {"list": array}
    response = requests.get(
        "https://1l87dn65x0.execute-api.us-east-1.amazonaws.com/Prod/apiresource",
        params=payload,
        timeout=5,
    )
    print(response.text)


if __name__ == "__main__":
    cli()
