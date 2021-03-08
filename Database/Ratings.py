from Database.__init__ import CUD_query, select_query


def create_ratings_table():
    query = """CREATE TABLE IF NOT EXISTS Ratings(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                vote INTEGER(1))"""
    CUD_query(query)


def create_rating(vote):
    query = """INSERT INTO Ratings(vote) VALUES (%s)"""
    params = [vote]
    CUD_query(query, params)


def select_rating(rating_id):
    query = """SELECT * FROM Ratings WHERE id = %s"""
    params = [rating_id]
    select_query(query, params)


def update_vote_number(rating_id, new_vote_number):
    query = """UPDATE Ratings SET vote = %s WHERE id = %s"""
    params = [new_vote_number, rating_id]
    CUD_query(query, params)


def delete_rating_by_id(rating_id):
    query = """DELETE FROM Ratings WHERE id = %s"""
    params = [rating_id]
    CUD_query(query, params)
