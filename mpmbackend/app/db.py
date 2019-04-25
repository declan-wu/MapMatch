import os
import psycopg2

HOST = os.environ["POSTGRES_HOST"]
DBNAME = os.environ["POSTGRES_DB"]
USER = os.environ["POSTGRES_USER"]
PASSWORD = os.environ["POSTGRES_PASSWORD"]

class DBConnection:
    def __init__(self):
        self.conn =psycopg2.connect("host={} dbname='{}' user='{}' password='{}'".format(HOST, DBNAME, USER, PASSWORD))
        
        cur = self.conn.cursor()
        cur.execute("""
        CREATE SCHEMA IF NOT exists mapmatch
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS mapmatch.mpm_interests (
            id UUID PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            interests VARCHAR(50) NOT NULL,
            longitude Decimal(9,6) NOT NULL,
            latitude Decimal(9,6) NOT NULL,
            imgurl TEXT NOT NULL
        )
        """)

    def __del__(self):
        self.conn.cursor().close()
        self.conn.close()

    def exec_statement(self, query_str):
        cur = self.conn.cursor()
        try:
            cur.execute(query_str)
        except Exception:
            cur.rollback()


    def exec_query(self, query_str):
        cur = self.conn.cursor()
        cur.execute(query_str)
        return cur.fetchall()
