from Database.__init__ import CUD_query, select_query, select_function


def create_comments_table():
    query = """CREATE TABLE IF NOT EXISTS Comments(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                firm_id INTEGER,
                user_id INTEGER,
                comment TEXT,
                answer TEXT NULL,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (firm_id) REFERENCES Firm(id))"""
    CUD_query(query)


def create_comment(firm_id, user_id, comment):
    query = """INSERT INTO Comments(firm_id, user_id, comment) VALUES (%s, %s, %s)"""
    params = [firm_id, user_id, comment]
    CUD_query(query, params)


def select_comment(comment_id):
    query = """SELECT * FROM Comments WHERE id = %s"""
    params = [comment_id]
    select_query(query, params)


def update_comment_text(comment_id, editing_user, comment_text):
    get_comment_user_id_query = """Select user_id FROM Comments WHERE id = %s"""
    get_comment_user_id_params = [comment_id]
    comment_user_id = select_function(get_comment_user_id_query, get_comment_user_id_params)
    if editing_user == comment_user_id[0]:
        edit_comment_query = """ UPDATE Comments
        SET comment = %s
        WHERE id = %s"""
        edit_comment_params = [comment_text, comment_id]

        CUD_query(edit_comment_query, edit_comment_params)
    else:
        print("You cant edit this comment!!")


def update_answer(comment_id, answer):
    query = """UPDATE Comments SET answer = %s WHERE id = %s"""
    params = [answer, comment_id]
    CUD_query(query, params)


def delete_comment_by_id(comment_id):
    query = """DELETE FROM Comments WHERE id = %s"""
    params = [comment_id]
    CUD_query(query, params)
