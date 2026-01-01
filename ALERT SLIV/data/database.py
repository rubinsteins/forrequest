import sqlite3
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def setup_db():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY,
            user_id INTEGER UNIQUE,
            issub TEXT DEFAULT Отсутствует,
            snoscount INTEGER DEFAULT 0,
            wantsreklama TEXT DEFAULT Имеется,
            pricereklama FLOAT DEFAULT 3,
            balance FLOAT DEFAULT 0,
            subto TEXT DEFAULT "Подписка отсутствует"
        )
    """)
    con.commit()
    con.close()

setup_db()

def snoses():
    con = sqlite3.connect("reports.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            reason TEXT,
            user TEXT
        )
    """)
    con.commit()
    con.close()

snoses()

def promos():
    con = sqlite3.connect("promo.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            promo TEXT,
            activations INTEGER,
            nominal INTEGER
        )
    """)
    con.commit()
    con.close()

promos()
