from dotenv import load_dotenv
import os

class Properties:
    load_dotenv()
    
    conexion_psql = None
    executor = None
    
    
    def __init__(self):
        self.get_executor(self)

  
    def get_executor(self):
        self.executor = eval(os.getenv("executor"))
        self.conexion_psql = self.executor['conexion_psql']
        #print (self.conexion_psql['host'])


    def get_conexion_psql(self):
        return self.conexion_psql





        


