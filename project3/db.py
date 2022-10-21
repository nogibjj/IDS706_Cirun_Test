'''
Project 3
'''
import pandas as pd
import MySQLdb

def get_connection():
    '''Returns a connection to the database'''
    connection = MySQLdb.connect(
        host="rds-mysql.ccpbwcnz4url.us-east-2.rds.amazonaws.com",
        user="admin",
        passwd="Qq13701377246",
        db="ids706")
    return connection

def save_data(connection, id, title, link, price, subscribers, reviews, levels, rating, subjectName):
    '''Saves the data to the database'''

    cursor = connection.cursor()
    str = "INSERT INTO udemy VALUES (" + id + ", \'" + title + "\',\'" + link + "\'," + price + "," + subscribers + "," + reviews + ",\'" + levels + "\'," + rating + ",\'" + subjectName + "\');"
    #print(str)
    cursor.execute(str)
    connection.commit()

def save_all_data():
    '''Saves the csv data to the database'''
    df = pd.read_csv('./udemy.csv', encoding='utf-8')
    connection = get_connection()
    for index, row in df.iterrows():
        save_data(connection, str(row['id']), row['title'], row['link'], str(row['price']), str(row['subscribers']), str(row['reviews']), row['levels'], str(row['rating']), row['subjectName'])
        

if __name__ == "__main__":
    save_all_data()
    print("ok");