import mysql.connector


class MySqlDatabase:
    def __init__(self, host, user, password, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.connection = None
        self.port = port
        self.connect()

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
        )
        if self.connection != None:
            print(f"LOG: connected to db: {self.host}:{self.port}, {self.user}")
        else:
            print(f"LOG: failed connection to db: {self.host}:{self.port}, {self.user}")

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def getExecute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def __close_connection(self):
        if self.connection.is_connected():
            self.connection.close()

    def __del__(self):
        self.__close_connection()
