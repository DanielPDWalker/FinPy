import unittest
import os
import pandas as pd
import finpy.database_utils.csv_import as csv_import
import finpy.database_utils.database_import as database_import

from shutil import copyfile, move
from pathlib import Path
from sqlalchemy import create_engine


class TestDatabaseImport(unittest.TestCase):

    def setUp(self):
        self.test_csv_list = ['test_data_one.csv',
                              'test_data_two.csv']
        for csv_file in self.test_csv_list:
            copyfile('{}{}'.format('./tests/test_data/', csv_file),
                     '{}{}'.format('./data/data_to_import/', csv_file))
        self.csv_list = csv_import.import_all_csvs()
        if os.path.isfile('finpy_database.db'):
            os.replace('finpy_database.db',
                       './database_backup/finpy_database.db')

    def tearDown(self):
        for csv_file in self.test_csv_list:
            os.remove('{}{}'.format('./data/data_imported/', csv_file))
        if os.path.isfile('./database_backup/finpy_database.db'):
            os.replace('./database_backup/finpy_database.db',
                       'finpy_database.db')

    def test_import_csv_list_into_database(self):
        database_import.import_csv_list_into_database(self.csv_list)
        if os.path.isfile('finpy_database.db'):
            copyfile('finpy_database.db', 'test_finpy_database.db')
            os.remove('finpy_database.db')
        self.assertTrue(Path('test_finpy_database.db').is_file())


if __name__ == '__main__':
    unittest.main()
