#!/usr/bin/env python

"""
Salary cli
"""
import os
import click
from databricks import sql


@click.group()
def cli():
    """
    Salary cli
    """
    pass


@cli.command()
@click.option("--year", default=2020, help="Year to get salary data for [2020-2022]")
def get_salary(year):
    """Get salary"""
    if year < 2020 or year > 2022:
        print("Year must be between 2020 and 2022")
        return

    print("Getting salary data for year: ", year)
    with sql.connect(
        server_hostname=os.environ["DATABRICKS_SERVER_HOSTNAME"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKSTOKEN"],
    ) as conn:

        with conn.cursor() as cursor:
            statement = (
                "SELECT AVG(SalaryUSD) FROM default.ds_salaries_csv WHERE year = "
                + str(year)
            )
            cursor.execute(statement)
            result1 = cursor.fetchall()

            print(result1[0]["avg(SalaryUSD)"], "USD")


if __name__ == "__main__":
    cli()
