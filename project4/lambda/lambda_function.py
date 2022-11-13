import json
import MySQLdb

def lambda_handler(event, context):
    # TODO implement
    print('ok')
    data = get_top_n_best_courses()
    print(data)
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }

def get_connection():
    """Returns a connection to the database"""
    connection = MySQLdb.connect(
        host="rds-mysql.ccpbwcnz4url.us-east-2.rds.amazonaws.com",
        user="admin",
        passwd="Qq13701377246",
        db="ids706"
    )
    return connection
    
def get_top_n_best_courses(n=10, subject=""):
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
  
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    
    result = {};
    result['id'] = []
    result['title'] = []
    result['subject'] = []
    result['rating'] = []
    
    for row in data:
        result['id'].append(str(row[0]))
        result['title'].append(str(row[1]))
        result['subject'].append(str(row[2]))
        result['rating'].append(str(row[3]))
    return result;