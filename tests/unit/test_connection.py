import unittest
import mysql.connector
from src.config import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER_NAME


class TestMySqlConnection(unittest.TestCase):
    connection = None

    def setUp(self):
        config = {"user": MYSQL_USER_NAME,
                  "password": MYSQL_PASSWORD,
                  "host": MYSQL_HOST,
                  "database": MYSQL_DATABASE
                  }
        self.connection = mysql.connector.connect(**config)

    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):
        self.assertTrue(self.connection.is_connected())



if __name__ == '__main__':
    unittest.main()
