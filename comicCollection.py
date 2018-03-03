#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os
import sqlite3
from hanziconv import HanziConv

PATH = r'G:/漫画/文件名整理完成/'

def get_namelist(path):
    namelist = os.listdir(path)



def have_table(table, conn):
    str = "select count(*) from sqlite_master where type='table' and name='%s'" % table
    cursor = conn.cursor()
    cursor.execute(str)
    values = cursor.fetchall()
    cursor.close()
    return values[0][0]

def create_books(conn):
    str = """CREATE TABLE books
        (ID INTEGER PRIMARY KEY, 
         Bookname TEXT NOT NULL,
         Author TEXT,
         Publisher TEXT,
         Scaner TEXT,
         Number TEXT NOT NULL)"""
    conn.execute(str)
    print("Create table books success")


if __name__ == "__main__":
    conn = sqlite3.connect('comic.db')
    if not have_table('books',conn):
        create_books(conn)
    print(have_table('books',conn))
    conn.close()




