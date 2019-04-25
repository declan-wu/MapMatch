import os
import psycopg2

HOST = os.environ["POSTGRES_HOST"]
DBNAME = os.environ["POSTGRES_DB"]
USER = os.environ["POSTGRES_USER"]
PASSWORD = os.environ["POSTGRES_PASSWORD"]

conn =psycopg2.connect("host={} dbname='{}' user='{}' password='{}'".format(HOST, DBNAME, USER, PASSWORD))

cur = conn.cursor()
cur.execute("""
CREATE SCHEMA IF NOT exists mapmatch
""")
cur.execute("""
DROP TABLE IF EXISTS exists mapmatch.mpm_interests
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