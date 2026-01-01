from data.database import *
import json



async def get_user(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM templates WHERE user_id = ?", (user_id,))
    user = cur.fetchone()
    con.close()
    return user

async def register_user(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("INSERT INTO templates (user_id) VALUES (?)", (user_id,))
    con.commit()
    con.close()

async def get_balance(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT balance FROM templates WHERE user_id = ?", (user_id,))
    userbalance = cur.fetchone()
    con.close()
    return userbalance

async def get_rekla(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT wantsreklama FROM templates WHERE user_id = ?", (user_id,))
    userrecla = cur.fetchone()
    con.close()
    return userrecla

async def get_price(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT pricereklama FROM templates WHERE user_id = ?", (user_id,))
    userrecla = cur.fetchone()
    con.close()
    return userrecla

async def get_aktiv(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT issub FROM templates WHERE user_id = ?", (user_id,))
    usersub = cur.fetchone()
    con.close()
    return usersub

async def get_repos(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT snoscount FROM templates WHERE user_id = ?", (user_id,))
    userrepos = cur.fetchone()
    con.close()
    return userrepos

async def get_do(user_id):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT subto FROM templates WHERE user_id = ?", (user_id,))
    dolboyob = cur.fetchone()
    con.close()
    return dolboyob

async def get_reports(user_id):
    con = sqlite3.connect("reports.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM templates WHERE user_id = ?", (user_id,))
    count = cur.fetchone()[0]
    con.close()
    return count


async def get_reports_list(user_id, page=1, per_page=5):
    con = sqlite3.connect("reports.db")
    cur = con.cursor()
    cur.execute("SELECT id, reason FROM templates WHERE user_id = ? ORDER BY id DESC LIMIT ? OFFSET ?",
                (user_id, per_page, (page - 1) * per_page))
    reports = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM templates WHERE user_id = ?", (user_id,))
    total_reports = cur.fetchone()[0]
    con.close()
    return reports, total_reports

def get_users():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT user_id FROM templates WHERE wantsreklama='Имеется'")
    users = [row[0] for row in cur.fetchall()]
    con.close()
    return users

