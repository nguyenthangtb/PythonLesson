from flask import Flask
import pymysql

class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "123"
        db = "demo"

        self.con = pymysql.connect(host=host, user=user, 
        password=password, db=db, 
        cursorclass=pymysql.cursors.DictCursor)
        
        self.cur = self.con.cursor()