from Database.__init__ import CUD_query, select_query


def create_firm_table():
    query = """CREATE TABLE IF NOT EXISTS Firm(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                user_id INTEGER,
                rating_id INTEGER,
                name TEXT,
                description TEXT,
                worker_number INTEGER,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (rating_id) REFERENCES Ratings(id))"""
    CUD_query(query)


def create_firm(user_id, rating_id, name, desc, worker_number):
    query = """INSERT INTO Firm(user_id, rating_id, name, description, worker_number) VALUES (%s, %s, %s, %s, %s)"""
    params = [user_id, rating_id, name, desc, worker_number]
    CUD_query(query, params)


def select_firm(firm_id):
    query = """SELECT * FROM Firm WHERE id = %s"""
    params = [firm_id]
    select_query(query, params)


def update_firm_desc(firm_id, new_desc):
    query = """UPDATE Firm SET description = %s WHERE id = %s"""
    params = [new_desc, firm_id]
    CUD_query(query, params)


def delete_firm_by_id(firm_id):
    query = """DELETE FROM Firm WHERE id = %s"""
    params = [firm_id]
    CUD_query(query, params)
