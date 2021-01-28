import unittest
import os
import finpy.database_utils.csv_import as csv_import

from shutil import copyfile


class TestCsvImport(unittest.TestCase):

    def setUp(self):
        self.test_csv_list = ['test_data_one.csv',
                              'test_data_two.csv']
        for csv_file in self.test_csv_list:
            copyfile('{}{}'.format('./tests/test_data/', csv_file),
                     '{}{}'.format('./data/data_to_import/', csv_file))

    def tearDown(self):
        for csv_file in self.test_csv_list:
            os.remove('{}{}'.format('./data/data_to_import/', csv_file))

    def test_import_all_csvs(self):
        csv_list = csv_import.import_all_csvs()
        self.assertEqual(self.test_csv_list, csv_list,
                         'The csv lists should be the same.')


if __name__ == '__main__':
    unittest.main()
