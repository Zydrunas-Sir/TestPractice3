import pymysql


class DatabaseContextManager:
    def __init__(self, select_query=False):
        self.select_query = select_query

    def __enter__(self):
        self.connection = pymysql.connect(user="root", password="root", host="localhost", database="task")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.select_query:
            self.connection.commit()
        self.connection.close()


def CUD_query(query, params=None):
    with DatabaseContextManager() as cursor:
        cursor.execute(query, params)


def select_query(query, params=None):
    with DatabaseContextManager(select_query=True) as cursor:
        cursor.execute(query, params)
        for record in cursor.fetchall():
            print(record)


def select_function(query, params=None):
    with DatabaseContextManager(is_select=True) as db:
        db.execute(query, params)
        return db.fetchall()
