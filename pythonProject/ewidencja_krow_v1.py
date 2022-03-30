import mysql.connector, os, sys
from sys import exit
from tabulate import tabulate
from sqlalchemy import create_engine
import pandas as pd

class Main(object):
    """docstring for Main."""

    def __init__(self, table, column, value, datas, id):
        self.table = table
        self.column = column
        self.value = value
        self.datas = datas
        self.id = id
        self.list = []
        self.head = []

class Mysql(Main):
    """docstring for Mysql."""

    def open(self):
        query = f"SELECT * FROM {self.table}"
        cursor.execute(query)

        for data in cursor:
            self.list.append(data)

        show_query = f"SHOW COLUMNS FROM {self.table}"
        cursor.execute(show_query)

        for head in cursor:
            self.head.append(head[0])

        print(tabulate(self.list, self.head, tablefmt="grid"))

class Data(object):
    """docstring for Data."""

    def __init__(self, table, base):
        self.table = table
        self.base = base


    def change(self):
        query = f"USE {self.base}"
        cursor.execute(query)

    def tables(self):
        query = f"SHOW TABLES"
        cursor.execute(query)
        list = []

        for data in cursor:
            list.append(data)

        print(tabulate(list, headers=[], tablefmt="grid"))

    def data(self):
        query = "SHOW DATABASES"
        cursor.execute(query)
        list = []

        for data in cursor:
            list.append(data)

        print(tabulate(list, headers=[], tablefmt="grid"))

    def columns(self):
        query = f"SHOW COLUMNS FROM {self.table}"
        cursor.execute(query)
        list = []

        for data in cursor:
            list.append(data)

        print(tabulate(list, tablefmt="grid", showindex="always"))

class Add(Main):
    """docstring for Add."""


    def add(self):
        query = f"INSERT INTO {self.table}({self.column}) VALUES('{self.value}')"
        cursor.execute(query)

class Edit(Main):
    """docstring for Edit."""

    def edit(self):
         query = f"UPDATE {self.table} SET {self.column} = '{self.datas}' WHERE ID={self.id}"
         cursor.execute(query)

class Drop(Main):
    """docstring for Drop."""

    def drop(self):
        query = f"DELETE FROM {self.table} WHERE ID={self.id}"
        cursor.execute(query)

def export():
    print("Którą tabelę chcesz eksportować?")
    table = input("> ")
    frame = pd.read_sql(f"select * from {table}", dbConnection)
    #print(frame)

    try:
        frame.to_excel(f"{table}.xlsx", engine="openpyxl")
        print("Export udał się pomyślnie!")
        os.execl(sys.executable, sys.executable, *sys.argv)

    except:
        print("ups! Coś poszło nie tak.")
        os.execl(sys.executable, sys.executable, *sys.argv)

def login(choice, var):
    if choice == "1":
        try:
            var.open()
        except:
            print("Nieoczekiwany błąd!")
    elif choice == "2":
        var.add()
    elif choice == "3":
        var.edit()
    elif choice == "4":
        var.drop()
    elif choice == "5":
        var.columns()
    elif choice == "6":
        var.data()
    elif choice == "8":
        var.data()
    elif choice == "9":
        var.tables()





    connection.commit()
    connection.close()


print("Podaj IP:")
IP = input("> ")
print("Podaj nazwę użytkownika:")
USER = input("> ")
print("Podaj hasło:")
PASSWORD = input("> ")
print("Podaj nazwę bazy:")
BASE = input("> ")

connection = mysql.connector.connect(user=USER,
                                    password=PASSWORD, host=IP,
                                    database=BASE,
                                    auth_plugin='mysql_native_password')

cursor = connection.cursor()
sqlEngine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{IP}/{BASE}')
dbConnection = sqlEngine.connect()


print('1 - Wyświetl tabelę')
print('2 - Wypełnij tabelę')
print('3 - Edytuj zawartość tabeli')
print('4 - Usuń zawartość tabeli')
print('5 - Wyświetl kolumny')
print('6 - Wyświetl dostępne bazy')
print('7 - Export do Excela')
print('8 - Zmień aktualną bazę')
print('9 Pokaż dostępne tabele')
print('0 - Wyjście')




choice = input("> ")

if choice == '1':
    print("Podaj nazwę tabeli:")
    table = input("> ")
    var = Mysql(table, None, None, None, None)

elif choice == '2':
    print("Podaj nazwę tabeli:")
    table = input("> ")
    print("Podaj kolumnę:")
    column = input("> ")
    print("Podaj zawardość:")
    value = input("> ")
    var = Add(table, column, value, None, None)

elif choice == '3':
    print("Którą tabelę chcesz edytować?")
    table = input("> ")
    print("Wg którego ID chcesz edytować?")
    id = input("> ")
    print("Która kolumna?:")
    column = input("> ")
    print("Podaj zawartość:")
    datas = input("> ")
    var = Edit(table, column, None, datas, id)

elif choice == '4':
    print("Z której tabeli chcesz usunąć zawartość?")
    table = input("> ")
    print("Który wiersz usunąć? (id):")
    id = input(" >")
    var = Drop(table, None, None, None, id)

elif choice =='5':
    print("Dla której tabeli chcesz wyświetlić kolumny?")
    table = input("> ")
    var = Data(table, None)

elif choice == '6':
    var = Data(None, None)

elif choice == '7':
    var = None
    export()

elif choice == '8':
    Data(None, None).data()
    print("Wybierz bazę z dostępnych:")
    base = input("> ")
    var = Data(None, base)

elif choice == '9':
    var = Data(None, None)

elif choice == '0':
    exit(0)
else:
    print("Błąd")


login(choice, var)



connection.close()