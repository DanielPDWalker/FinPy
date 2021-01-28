import unittest
import os
import finpy.data_cleaning.csv_import as csv_import

from shutil import copyfile


class TestCsvImport(unittest.testcase):

    def setUp(self):
        test_csv_list = ['test_data_one.csv',
                         'test_data_two.csv',
                         'test_incorrect_file.png']
        for csv_file in test_csv_list:
            copyfile('{}{}'.format('../test_data/', csv_file),
                     '{}{}'.format(csv_import.IMPORT_DIR, csv_file))

    def tearDown(self):
        for csv_file in test_csv_list:
            os.remove('{}{}'.format(csv_import.IMPORT_DIR, csv_file))

    def test_import_all_csvs(self):
        csv_list = csv_import.import_all_csvs()
        self.assertEqual(test_csv_list, csv_list,
                         'The csv lists should be the same.')


if __name__ == '__main__':
    unittest.main()
