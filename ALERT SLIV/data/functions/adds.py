from data.database import *
import json


async def add_snos(user_id, reason, links_str):
    con = sqlite3.connect("reports.db")
    cur = con.cursor()
    query = """
        INSERT INTO templates (user_id, reason, user)
        VALUES (?, ?, ?)
    """
    cur.execute(query, (user_id, reason, links_str))
    con.commit()
    con.close()