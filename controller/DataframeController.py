import pandas as pd
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
        a = eval(os.getenv("executor"))
        credentials = a[self._credentials]
        engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(
            credentials['user'], credentials['password'], credentials['host'], credentials['database']))
        query = f'SELECT * from {self._table}'
        dataframe = pd.read_sql_query(query, engine)
        if self._column != []:
            dataframe = dataframe[self._column]
        return dataframe

    @staticmethod
    def get_excel(df, table):
        if table == '':
            table = 'file'
        full_path = f'{table}.xlsx'
        with pd.ExcelWriter(full_path,
                            engine='xlsxwriter',
                            options={'strings_to_urls': False}) as writer:
            df.to_excel(writer, index=False)


class SetDateFrame(GetDataFrame):
    def __init__(self, data_frame, table, credentials=''):
        super().__init__(table, credentials)
        self._dataframe = data_frame

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
        self._dataframe = dataframe

    @property
    def send_df_append(self):
        if self._credentials or self._table != '':
            a = eval(os.getenv("executor"))
            credentials = a[self._credentials]
            engine = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}', echo=False).format(
            credentials['user'], credentials['password'], credentials['host'], credentials['port'], credentials['database'])
            self._dataframe.to_sql(
                self._table, engine, schema='public', if_exists='append', index=False)
            print('¡Done!')

    @property
    def send_df_replace(self):
        if self._credentials or self._table != '':
            a = eval(os.getenv("executor"))
            credentials = a[self._credentials]
            engine = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}', echo=False).format(
            credentials['user'], credentials['password'], credentials['host'], credentials['port'], credentials['database'])
            self._dataframe.to_sql(
                self._table, engine, schema='public', if_exists='replace', index=False)
            print('¡Done!')
