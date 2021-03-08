from Database.__init__ import CUD_query, select_query


def create_user_table():
    query = """CREATE TABLE IF NOT EXISTS User(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                username TEXT,
                password TEXT,
                first_name TEXT,
                last_name TEXT)"""
    CUD_query(query)


def create_user(username, password, first_name, last_name, residence):
    query = """INSERT INTO User(username,password,first_name, last_name, residence) VALUES (%s, %s, %s, %s, %s)"""
    params = [username, password, first_name, last_name, residence]
    CUD_query(query, params)


def select_user(user_id):
    query = """SELECT * FROM User WHERE id = %s"""
    params = [user_id]
    select_query(query, params)


def update_user_first_name(user_id, new_first_name):
    query = """UPDATE User SET first_name = %s WHERE id = %s"""
    params = [new_first_name, user_id]
    CUD_query(query, params)


def delete_user_by_id(user_id):
    query = """DELETE FROM User WHERE id = %s"""
    params = [user_id]
    CUD_query(query, params)
