import os
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from .csv_import import IMPORT_DIR, EXPORT_DIR


def import_csv_list_into_database(csv_list):

    # Connecting to the database
    finpy_database = create_engine('sqlite:///finpy_database.db')

    # Adding data to database
    for filename in csv_list:
        df = pd.read_csv('{}{}'.format(IMPORT_DIR, filename))
        df.to_sql('data', finpy_database, if_exists='append')

        # Move the imported csv file to the data_imported dir
        os.replace('{}{}'.format(IMPORT_DIR, filename),
                   '{}{}'.format(EXPORT_DIR, filename))
