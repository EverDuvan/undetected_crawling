from dotenv import load_dotenv
import os
load_dotenv()


class PropertieController:
    executor = None
    properties = None
    credentials = None
    retailers = None
    countries = None

    @classmethod
    def get_executor(cls, credentials):
        cls.executor = eval(os.getenv("executor"))
        cls.properties = cls.executor[credentials]
        return cls.properties

    @classmethod
    def get_retailers(cls):
        cls.retailers = os.getenv('retailers')
        return cls.retailers

    @classmethod
    def get_countries(cls):
        cls.countries = os.getenv('countries')
        return cls.countries
