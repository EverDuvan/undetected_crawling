from dotenv import load_dotenv
import os
load_dotenv()

class Properties:
    _conexion_psql = None
    _executor = None

    @classmethod
    def get_executor(cls):
        cls._executor = eval(os.getenv("executor"))
        cls._conexion_psql = cls._executor['conexion_psql']
        #print (cls._conexion_psql['host'])
        return cls._conexion_psql    

    @classmethod
    def get_conexion_psql(cls):
        return cls._conexion_psql

''' 
if __name__ == '__main__':
    con = Properties.get_executor()
    print(con['host'])

 '''




