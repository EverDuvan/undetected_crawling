from dotenv import load_dotenv
import os
load_dotenv()

class Properties:
    _properties = None
    _executor = None
    _credentials = None
    _retailers = None
    _countries = None

    @classmethod
    def get_executor(cls, _credentials):
        cls._executor = eval(os.getenv("executor"))
        cls._properties = cls._executor[_credentials]
        return cls._properties

    @classmethod
    def get_retailers(cls):
        cls._retailers = os.getenv('retailers')
        return cls._retailers

    @classmethod
    def get_countries(cls):
        cls._countries = os.getenv('countries')
        return cls._countries
        

''' 
if __name__ == '__main__':
    con = Properties.get_executor('conexion_mysql')
    print(con['port'])

 '''