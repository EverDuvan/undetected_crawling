from dotenv import load_dotenv
import os
load_dotenv()


def get_executor(credentials):
    try:
        executor = eval(os.getenv("executor"))
        properties = executor[credentials]
        return properties
    except Exception as e:
        print(f'error en get_executor() in PropertieController.py: {e}')


def get_retailers():
    try:
        retailers = os.getenv('retailers')
        return retailers
    except Exception as e:
        print(f'error en get_retailers() in PropertieController.py: {e}')


def get_countries():
    try:
        countries = os.getenv('countries')
        return countries
    except Exception as e:
        print(f'error en get_countries() in PropertieController.py: {e}')
