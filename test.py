from dotenv import load_dotenv
import os
load_dotenv()

class Properties:
    _conexion_psql = None
    _executor = None
    _credentials = None

    @classmethod
    def get_executor(cls, _credentials):
        cls._executor = eval(os.getenv("executor"))
        cls._conexion_psql = cls._executor[_credentials]
        return cls._conexion_psql    

''' 
if __name__ == '__main__':
    con = Properties.get_executor('conexion_mysql')
    print(con['port'])

 '''







