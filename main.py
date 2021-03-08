from Database.User import *
from Database.Firm import *
from Database.Comments import *
from Database.Ratings import *


def join_user_by_firm(firm_id):
    query = """SELECT User.first_name, Firm.name,description  FROM Firm
                JOIN User ON User.id = Firm.user_id
                JOIN Ratings ON Ratings.id = Firm.rating_id
                WHERE firm_id = %s"""
    params = [firm_id]
    select_query(query, params)


def rate_and_comment(firm_id, user_id, comment, vote):
    create_comment(firm_id, user_id, comment)
    create_rating(vote)


def firm_answering(comment_id, editing_firm, answer):
    get_comment_firm_id_query = """Select firm_id FROM Comments WHERE id = %s"""
    get_comment_firm_id_params = [comment_id]
    comment_user_id = select_function(get_comment_firm_id_query, get_comment_firm_id_params)
    if editing_firm == comment_user_id[0]:
        edit_comment_query = """ UPDATE Comments
        SET answer = %s
        WHERE id = %s"""
        edit_comment_params = [answer, comment_id]

        CUD_query(edit_comment_query, edit_comment_params)
    else:
        print("Selected wrong comment")
