import os

IMPORT_DIR = "./data/data_to_import/"
EXPORT_DIR = "./data/data_imported/"


def import_all_csvs():

    # Get a list of all files in the import dir
    csv_list = os.listdir(IMPORT_DIR)
    # Make list of ONLY csv files in the import dir
    csv_list = [
        filename for filename in csv_list if filename.endswith(".csv")]
    return csv_list
