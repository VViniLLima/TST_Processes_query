import psycopg2

class DBConnection:
    def create_connection(self, credentials):
        try:
            connection = psycopg2.connect(
                database = credentials['database'], 
                user = credentials['user'],
                password = credentials['password'],
                host = credentials['host'],
                port = credentials['port']
            )
            print('Connected!')

        except Exception as E :
            print('An error has ocurred.: ', E)
        return connection