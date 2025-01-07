from typing import List
from functools import wraps

import pandas as pd

def logger_method(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n-------------- !!!!!!!      Executing  {func.__name__} method       !!!!!!!-------------- \n")

        return func(*args, **kwargs)
    return wrapper


class PandasPrac:

    @logger_method
    def DupsInDataframe(self) -> pd.DataFrame:
        data = {
            'customer_id': [1, 2, 3, 4, 5, 6],
            'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
            'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com',
                      'john@example.com', 'alice@example.com']
        }
        df = pd.DataFrame(data)
        print(df.drop_duplicates(subset='email'))

    @staticmethod
    @logger_method
    def rename_cols():
        data = {
            'id': [1, 2, 3, 4, 5],
            'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
            'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
            'age': [6, 7, 16, 18, 10]
        }
        df = pd.DataFrame(data)
        df = df.rename(columns={'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})
        print(df)

    @staticmethod
    @logger_method
    def dropMissingData():
        data = {
            "student_id": [355, 951, 470, 977, 300],
            "name": [None, None, "Quincy", "Sophia", "Liam"],
            "age": [9, 8, 20, None, 15]
        }
        df = pd.DataFrame(data)
        print("Before")
        print(df)
        df = df.dropna(axis=0, subset=['name'])
        print(df)

    @staticmethod
    @logger_method
    def createBonusColumn():
        data = {
            "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
            "salary": [4548, 28150, 1103, 6593, 74576, 24433]
        }
        employees = pd.DataFrame(data)
        employees['bonus'] = employees['salary']*2
        print(employees)

    @staticmethod
    @logger_method
    def changeDatatype():
        data = {
            "student_id": [1, 2],
            "name": ["Ava", "Kate"],
            "age": [6, 15],
            "grade": [73.0, 87.0]
        }
        df = pd.DataFrame(data)
        df.astype({'grade': 'int32'})
        print(df)

    @staticmethod
    @logger_method
    def fillMissingValues() -> pd.DataFrame:
        data = [
            {"name": "Wristwatch", "quantity": None, "price": 135},
            {"name": "WirelessEarbuds", "quantity": None, "price": 821},
            {"name": "GolfClubs", "quantity": 779, "price": 9319},
            {"name": "Printer", "quantity": 849, "price": 3051},
        ]

        df = pd.DataFrame(data)
        df['quantity'] = df['quantity'].fillna(0).astype('int32')
        print(df)

    @staticmethod
    @logger_method
    def concatenateTables():
        data = [
            {"name": "Wristwatch", "quantity": None, "price": 135},
            {"name": "WirelessEarbuds", "quantity": None, "price": 821},
            {"name": "GolfClubs", "quantity": 779, "price": 9319},
            {"name": "Printer", "quantity": 849, "price": 3051},
        ]

        df1 = pd.DataFrame(data)
        df2 = df1
        pd.concat([df1, df2], ignore_index=True)

    @staticmethod
    @logger_method
    def pivotTable():
        data = {
            'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso',
                     'ElPaso', 'ElPaso', 'ElPaso'],
            'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'],
            'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
        }
        df = pd.DataFrame(data)
        print("Before\n", df)
        df = pd.pivot_table(data=df, index='month', columns='city', values='temperature', aggfunc=sum).reset_index()
        print("After\n", df)
        new = pd.melt(df, id_vars=['month'], value_vars=['ElPaso', 'Jacksonville'], var_name='city', value_name='temperature')
        print("After melt\n", new)

    @staticmethod
    @logger_method
    def findHeavyAnimals():
        data = {
            'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
            'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
            'age': [98, 50, 6, 45, 100, 26],
            'weight': [464, 41, 328, 463, 50, 349]
        }
        animals = pd.DataFrame(data)
        print('Before\n', animals)
        new = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
        print('After \n', new)


prac = PandasPrac()
# prac.DupsInDataframe()
# PandasPrac.rename_cols()
# PandasPrac.dropMissingData()
# PandasPrac.createBonusColumn()
# PandasPrac.fillMissingValues()
PandasPrac.pivotTable()
# PandasPrac.findHeavyAnimals()
