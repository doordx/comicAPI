import mysql.connector
from mysql.connector import Error
from config import (MYSQL_HOST, MYSQL_USER_NAME,
                    MYSQL_PASSWORD, MYSQL_DATABASE)


class Dao(object):

    def __init__(self):
        self.connection = None

    def get_connection(self):
        self.connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER_NAME,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        return self.connection

    def bulk_insert(self, records):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            if connection.is_connected():
                print("Connected to MySQL")
                sql = """INSERT INTO comics (name, num, altText, imageLink) VALUES (%s, %s, %s, %s)"""
                if len(records) > 0:
                    cursor.executemany(sql, records)
                    connection.commit()
                    print(cursor.rowcount, "comics inserted")
        except Error as e:
            print("Error while connecting to MySQL", e)
            connection.rollback()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
