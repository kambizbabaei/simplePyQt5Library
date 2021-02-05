import sqlite3 as sq
from os.path import isfile
from typing import overload

from common.PATH.PATH import local_database

class dbHelper:
    def __init__(self) -> None:
        super().__init__()
        self.db = local_database+"database.db"
        self.initialize_db()

    def initialize_db(self):
        if not isfile(self.db) :
            self.create_tables()

    def create_tables(self):
        connection = sq.connect(self.db)
        c = connection.cursor()

        c.execute(""" 
        CREATE TABLE users(
            username TEXT NOT NULL UNIQUE PRIMARY KEY,
            password TEXT NOT NULL,
            securityQustion TEXT,
            securityQustionAnswer TEXT,
            active  INTEGER
         )""")
        connection.commit()
        c.execute("""
        INSERT INTO users VALUES('ADMIN','ADMIN','ADMIN','ADMIN',1)
        """)

        c.execute("""
        CREATE TABLE books (
            name                 TEXT NOT NULL,
            author               TEXT NOT NULL,
            pages                TEXT NOT NULL,
            edition              TEXT,
            isbn                 TEXT UNIQUE,
            publisher            TEXT,
            language             TEXT,
            translator           TEXT,
            uploaded_by          TEXT,
            uploaded_in          TEXT,
            first_publish_date   TEXT,
            edition_publish_date TEXT,
            desc                 TEXT,
            image                BLOB,
            FOREIGN KEY (uploaded_by)
            REFERENCES users (username) 
        )""")
        connection.commit()
        connection.close()
    def get_books(self):
        connection = sq.connect(self.db)
        c = connection.cursor()
        books = c.execute("""
        SELECT rowid FROM books
        """).fetchall()
        connection.commit()
        connection.close()
        return books
        
    def get_book(self,uid) -> tuple:
        connection = sq.connect(self.db)
        c = connection.cursor()
        book = c.execute("""
        SELECT * FROM books WHERE rowid = "%s"
        """%uid).fetchone()
        connection.commit()
        connection.close()
        return book

    def mybooks(self,usename):
        connection = sq.connect(self.db)
        c = connection.cursor()
        books = c.execute("""
        SELECT rowid FROM books WHERE uploaded_by = "%s"
        """%usename).fetchall()
        connection.commit()
        connection.close()
        return books

    def get_book_by_isbn(self,isbn):
        connection = sq.connect(self.db)
        c = connection.cursor()
        book = c.execute("""
        SELECT * FROM books WHERE isbn = "%s"
        """%isbn).fetchone()
        connection.commit()
        connection.close()        
        return book

    def add_book(self,name,author,pages,isbn,edition=None,publisher=None,language=None,translator=None,uploaded_by=None,uploaded_in=None,first_publish_date=None,edition_pubishdate=None,desc=None,img=None):
        connection = sq.connect(self.db)
        c = connection.cursor()
        c.execute("""INSERT INTO books VALUES(
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?)
        """,(name,author,pages,edition,isbn,publisher,language,translator,uploaded_by,uploaded_in,first_publish_date,edition_pubishdate,desc,img))
        connection.commit()
        connection.close()

    def editbook(self,_book_name,_book_author_name,_book_pages,_book_edition,_book_isbn,_book_publisher,_book_language,_book_translator,_book_release_date,_book_editionpublishdate,_book_desc,_book_image,_uid):
        connection = sq.connect(self.db)
        c = connection.cursor()
        c.execute("""
        UPDATE books
        SET 
            name                 =?,
            author               =?,
            pages                =?,
            edition              =?,
            isbn                 =?,
            publisher            =?,
            language             =?,
            translator           =?,

            first_publish_date   =?,
            edition_publish_date =?,
            desc                 =?,
            image                =?
        WHERE
            rowid = ?

        """,(_book_name,_book_author_name,_book_pages,_book_edition,_book_isbn,_book_publisher,_book_language,_book_translator,_book_release_date,_book_editionpublishdate,_book_desc,_book_image,_uid))
        connection.commit()
        connection.close()
        
    def add_user(self,username :str, password:str,sec_q:str,sec_q_a) ->None:
        connection = sq.connect(self.db)
        c = connection.cursor()
        row_id = c.execute("""
        SELECT rowid FROM users WHERE username = "%s"
        """%username).fetchone()
        if row_id is not None:
            return None
        c.execute("""
        INSERT INTO users VALUES (
            ?,
            ?,
            ?,
            ?,
            ?
            )""",(username,password,sec_q,sec_q_a,0))
        connection.commit()
        row_id = c.execute("""
        SELECT rowid FROM users WHERE username = "%s"
        """%username).fetchone()
        
        c.execute("""
        CREATE TABLE user_%s_books(
            books TEXT,
            FOREIGN KEY (books)
            REFERENCES books (rowid) 
        )
        """%row_id[0])
        connection.commit()
        connection.close()
        return row_id

    def active_user(self,rowid):
        
        connection = sq.connect(self.db)
        c = connection.cursor()
        c.execute(
            """ 
            UPDATE users
            set 
                active = ?
            WHERE
                rowid = ?

            """ , (1,rowid[0])
        )
        connection.commit()
        connection.close()

    def deactive_user(self,rowid):
        connection = sq.connect(self.db)
        c = connection.cursor()
        c.execute(
            """ 
            UPDATE users
            set 
                active = ?
            WHERE
                rowid = ?

            """ , (0,rowid[0])
        )
        connection.commit()
        connection.close()

    def get_user_by_uid(self,uid) ->tuple:
        connection = sq.connect(self.db)
        c = connection.cursor()
        user = c.execute("""
        SELECT * FROM users WHERE rowid = "%s"
        """%uid).fetchone()
        connection.commit()
        connection.close()
        return user
        
    def update_password(self,username,newpassword):
        connection = sq.connect(self.db)
        c = connection.cursor()
        c.execute("""
        UPDATE users
        SET 
            password = ?
        WHERE
            username = ?

        """,(newpassword,username))
        connection.commit()
        connection.close()

    def update_user(self,currentuser,username,password,s_q,s_a):
        connection = sq.connect(self.db)
        c = connection.cursor()
        if self.get_user_by_username(username) is not None:
            return -1
        c.execute("""
        UPDATE users
        SET 
            username = ?,
            securityQustion =?,
            securityQustionAnswer = ?
        WHERE
            username = ?

        """,(username,s_q,s_a,currentuser))
        connection.commit()
        if password != "":
            c.execute(
                """
            UPDATE users
            SET 
                password = ?
            WHERE
                username = ?
                """
            ,(password,username))
            connection.commit()
        connection.close()

    def get_user_by_username(self,username):
        connection = sq.connect(self.db)
        c = connection.cursor()
        user = c.execute("""
        SELECT rowid FROM users WHERE username = "%s"
        """%username).fetchone()
        connection.commit()
        connection.close()
        return user

    def get_users(self):
        connection = sq.connect(self.db)
        c = connection.cursor()
        user = c.execute("""
        SELECT * FROM users
        """).fetchall()
        connection.commit()
        connection.close()
        return user

    def get_user(self,username,password) ->tuple:
        connection = sq.connect(self.db)
        c = connection.cursor()
        user = c.execute("""
        SELECT * FROM users WHERE username = "%s" AND password = "%s"
        """%(username,password)).fetchone()
        connection.commit()
        connection.close()
        return user

    def delete_book(self,uid):
        connection = sq.connect(self.db)
        c = connection.cursor()
        c.execute("""
                DELETE FROM books
                WHERE rowid = '%s'
        """%uid)
        connection.commit()
        connection.close()

    def search(self,text):
        connection = sq.connect(self.db)
        c = connection.cursor()
        search=c.execute("""
                SELECT rowid
                FROM books
                WHERE name LIKE '%{}%'""".format(text)
        ).fetchall()
        connection.commit()
        connection.close()
        return search
