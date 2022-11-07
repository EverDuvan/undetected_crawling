import pandas as pd
from urllib.parse import quote
from sqlalchemy.engine import create_engine
from dotenv import load_dotenv
import os
load_dotenv()


class GetDataFrame:
    def __init__(self, table=[], credentials='', column=[]):
        self._credentials = credentials
        self._table = table
        self._column = column

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, table):
        self._table = table

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        self._credentials = credentials

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, column):
        self._column = column

    @property
    def get_dataframe(self):
        try:
            a = eval(os.getenv("executor"))
            credentials = a[self._credentials]
            engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(
                credentials['user'], credentials['password'], credentials['host'], credentials['database']))
            query = f'SELECT * from {self._table}'
            dataframe = pd.read_sql_query(query, engine)
            if self._column != []:
                dataframe = dataframe[self._column]
            return dataframe
        except Exception as e:
            print(f'error en get_dataframe() in DataframeController.py: {e}')

    @staticmethod
    def get_excel(df, table):
        try:
            if table == '':
                table = 'file'
            full_path = f'{table}.xlsx'
            with pd.ExcelWriter(full_path,
                                engine='xlsxwriter',
                                options={'strings_to_urls': False}) as writer:
                df.to_excel(writer, index=False)
        except Exception as e:
            print(f'error en get_excel() in DataframeController.py: {e}')


class SetDateFrame(GetDataFrame):
    def __init__(self, dataframe, table, credentials=''):
        super().__init__(table, credentials)
        self._dataframe = dataframe

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
        self._dataframe = dataframe

    @property
    def send_df_append(self):
        try:
            if self._credentials or self._table != '':
                a = eval(os.getenv("executor"))
                credentials = a[self._credentials]
                engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.
                                       format(credentials['user'], credentials['password'], credentials['host'],
                                              credentials['port'], credentials['database']))
                self._dataframe.to_sql(
                    self._table, engine, schema='public', if_exists='append', index=False)
        except Exception as e:
            print(f'error en send_df_append() in DataframeController.py: {e}')

    @property
    def send_df_replace(self):
        try:
            if self._credentials or self._table != '':
                a = eval(os.getenv("executor"))
                credentials = a[self._credentials]
                engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.
                                       format(credentials['user'], credentials['password'], credentials['host'],
                                              credentials['port'], credentials['database']))
                self._dataframe.to_sql(
                    self._table, engine, schema='public', if_exists='replace', index=False)
        except Exception as e:
            print(f'error en send_df_append() in DataframeController.py: {e}')
