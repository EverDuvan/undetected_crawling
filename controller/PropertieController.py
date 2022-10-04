from dotenv import load_dotenv
import os
load_dotenv()


def get_executor(credentials):
    executor = eval(os.getenv("executor"))
    properties = executor[credentials]
    return properties


def get_retailers():
    retailers = os.getenv('retailers')
    return retailers


def get_countries():
    countries = os.getenv('countries')
    return countries
