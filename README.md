[![Python application test with Github Actions](https://github.com/nogibjj/IDS706_Cirun_Test/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/IDS706_Cirun_Test/actions/workflows/main.yml)
# IDS706_Cirun_Test

Test the GitHub Codespace
# Project 1

Project 1 shows a data script with Databricks. In this project I build a new repo, scaffolding files, and connect it to github actions. I used the databricks in Azure, a new database was created. The database was initialized using the csv file I found in Kaggle. The table shows the salaries for data science student. Then I used Click to create a CLI program. It can be used to calculate the average salary for a specific year.

# Project 2

Project 2 aims to build a REST API and a command line tool. I created a python script `proj2.py`, it was used to parse the csv input file with numpy API, and send the file content to the API endpoint via HTTP Get. The REST API was build with AWS Lambda and AWS API Gateway, it read the input numbers, sort them, and returns the sorted result.

# Project 3

Project 3 aims to generate a script that queries a database. In this project I created a MySQL database in AWS RDS, and I initialized the database with the csv file I found in Kaggle. 
```
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
```
The database stores the information of coursera course. Then I build a script `db.py`, it queries the database with SQL and MySQLdb API. I also made it as a command line tool with Click. It retireve the info for a specific course or top N best courses.

# Project 4

Project 4 is a further step of project 3. It created a REST API to query the database, and build the continuous delivery pipeline with github actions. The REST API was created using AWS Lambda and AWS API Gateway, it will parse the input instruction and query the MySQL database. Then I modified the `main.yaml`, when the new change is pushed to the repo, github actions will also be triggered and push the change to AWS, thus it can automatically update the API.
