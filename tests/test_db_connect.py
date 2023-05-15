import unittest
import sys
sys.path.append("..")

from db.db_connect import MySQLConnecter


class TestMySQLConnecter(unittest.TestCase):
    def setUp(self):
        self.db = MySQLConnecter('localhost', 'root', 'password', 'mydatabase')
        self.db.connect()

    def tearDown(self):
        self.db.disconnect()

    def test_create_record(self):
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        params = ('John Doe', 'john@example.com')
        self.db.execute_query(query, params)

    def test_read_record(self):
        query = "SELECT * FROM users WHERE name = %s"
        params = ('John Doe',)
        result = self.db.fetch_data(query, params)
        # Add assertions to verify the fetched data

    def test_update_record(self):
        query = "UPDATE users SET email = %s WHERE name = %s"
        params = ('new_email@example.com', 'John Doe')
        self.db.execute_query(query, params)
        # Add assertions to verify the record is updated

    def test_delete_record(self):
        query = "DELETE FROM users WHERE name = %s"
        params = ('John Doe',)
        self.db.execute_query(query, params)
        # Add assertions to verify the record is deleted


if __name__ == '__main__':
    unittest.main()
