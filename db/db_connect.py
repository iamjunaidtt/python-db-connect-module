import mysql.connector


class MySQLConnecter:
    def __init__(self, host, username, password, database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        cursor.close()
        return data

    def fetch_data(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        cursor.close()
        return data
