import unittest
import os
import pandas as pd

from sqlalchemy import create_engine


class TestDatabaseImport(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        os.remove('test_finpy_database.db')

    def test_all_data_imported_into_database(self):
        # Test reading from database
        test_finpy_database = create_engine('sqlite:///test_finpy_database.db')
        df = pd.read_sql_query('SELECT * FROM data', test_finpy_database)
        # There are 6 rows in the test data.
        self.assertEqual(len(df), 6)


if __name__ == '__main__':
    unittest.main()
