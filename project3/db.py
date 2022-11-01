#!/usr/bin/env python
"""
Project 3

https://github.com/nogibjj/IDS706_Cirun_Test

# mysql -h rds-mysql.ccpbwcnz4url.us-east-2.rds.amazonaws.com -P 3306 -u admin -p

+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| id          | int           | NO   | PRI | NULL    |       |
| title       | varchar(255)  | NO   |     | NULL    |       |
| link        | varchar(255)  | NO   |     | NULL    |       |
| price       | decimal(10,2) | YES  |     | NULL    |       |
| subscribers | int           | YES  |     | NULL    |       |
| reviews     | int           | YES  |     | NULL    |       |
| levels      | varchar(255)  | NO   |     | NULL    |       |
| rating      | decimal(10,2) | YES  |     | NULL    |       |
| subjectName | varchar(255)  | NO   |     | NULL    |       |
+-------------+---------------+------+-----+---------+-------+
"""
import pandas as pd
import MySQLdb
import os
import click


@click.group()
def cli():
    """
    Udemy Courses CLI
    """


def get_connection():
    """Returns a connection to the database"""
    print(os.environ["DB_PASS"])
    connection = MySQLdb.connect(
        host="rds-mysql.ccpbwcnz4url.us-east-2.rds.amazonaws.com",
        user="admin",
        passwd=os.environ["DB_PASS"],
        db="ids706",
    )
    return connection


def save_data(
    connection,
    id,
    title,
    link,
    price,
    subscribers,
    reviews,
    levels,
    rating,
    subjectName,
):
    """Saves the data to the database"""

    cursor = connection.cursor()
    str = (
        "INSERT INTO udemy VALUES ("
        + id
        + ", '"
        + title
        + "','"
        + link
        + "',"
        + price
        + ","
        + subscribers
        + ","
        + reviews
        + ",'"
        + levels
        + "',"
        + rating
        + ",'"
        + subjectName
        + "');"
    )
    cursor.execute(str)
    connection.commit()


@cli.command()
@click.option("--n", default=10, help="The number of courses to return")
@click.option("--subject", default="", help="The subject name of the courses to return")
def get_top_n_best_courses(n, subject):
    """Returns the top N best courses"""
    connection = get_connection()
    cursor = connection.cursor()
    where = ""
    if subject != "":
        where = " WHERE subjectName = '" + subject + "'"

    sql = (
        "SELECT id, title, subjectName, rating FROM udemy"
        + where
        + " ORDER BY rating DESC limit "
        + str(n)
        + ";"
    )
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    print("id     subjectName      rating      title")
    for row in data:
        print(
            str(row[0])
            + "    "
            + str(row[2])
            + "    "
            + str(row[3])
            + "    "
            + str(row[1])
        )


@cli.command()
@click.option("--n", default=10, help="The number of courses to return")
@click.option("--subject", default="", help="The subject name of the courses to return")
def get_top_n_subscribers_courses(n, subject=""):
    """Returns the top N courses with most susbrcribers"""
    connection = get_connection()
    cursor = connection.cursor()

    where = ""
    if subject != "":
        where = " WHERE subjectName = '" + subject + "'"

    sql = (
        "SELECT id, title, subjectName, subscribers FROM udemy"
        + where
        + " ORDER BY subscribers DESC limit "
        + str(n)
        + ";"
    )
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    print("id        subjectName        subscribers          title")
    for row in data:
        print(
            str(row[0])
            + "    "
            + str(row[2])
            + "     "
            + str(row[3])
            + "    "
            + str(row[1])
        )


@cli.command()
@click.option("--course_id", default=41295, help="course id")
def get_review(course_id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM udemy where id = " + str(course_id) + ";"
    cursor.execute(sql)
    data = cursor.fetchall()
    for (
        id,
        title,
        link,
        price,
        subscribers,
        reviews,
        levels,
        rating,
        subjectName,
    ) in data:
        print("id: " + str(id))
        print("title: " + str(title))
        print("link: " + str(link))
        print("price: " + str(price))
        print("subscribers: " + str(subscribers))
        print("reviews: " + str(reviews))
        print("levels: " + str(levels))
        print("rating: " + str(rating))
        print("subjectName: " + str(subjectName))
    connection.close()


def save_all_data():
    """Saves the csv data to the database"""
    df = pd.read_csv("./udemy.csv", encoding="utf-8")
    connection = get_connection()
    for index, row in df.iterrows():
        save_data(
            connection,
            str(row["id"]),
            row["title"],
            row["link"],
            str(row["price"]),
            str(row["subscribers"]),
            str(row["reviews"]),
            row["levels"],
            str(row["rating"]),
            row["subjectName"],
        )


if __name__ == "__main__":
    cli()
