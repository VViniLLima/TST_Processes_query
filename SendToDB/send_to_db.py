import json
from db_connection import DBConnection
from db_credentials import DbCredentials
from queries import Queries

file = open('data/processes.json')
processes_data = json.load(file)

credentials = DbCredentials()
connection = DBConnection()

conn = connection.create_connection(credentials.local_db_credentials())
cursor = conn.cursor()

insert_data = Queries()

#insert_data.insert_data(cursor, processes_data)

conn.commit()
cursor.close()
