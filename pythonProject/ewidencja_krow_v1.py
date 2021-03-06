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
    print("Kt??r?? tabel?? chcesz eksportowa???")
    table = input("> ")
    frame = pd.read_sql(f"select * from {table}", dbConnection)
    #print(frame)

    try:
        frame.to_excel(f"{table}.xlsx", engine="openpyxl")
        print("Export uda?? si?? pomy??lnie!")
        os.execl(sys.executable, sys.executable, *sys.argv)

    except:
        print("ups! Co?? posz??o nie tak.")
        os.execl(sys.executable, sys.executable, *sys.argv)

def login(choice, var):
    if choice == "1":
        try:
            var.open()
        except:
            print("Nieoczekiwany b????d!")
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
print("Podaj nazw?? u??ytkownika:")
USER = input("> ")
print("Podaj has??o:")
PASSWORD = input("> ")
print("Podaj nazw?? bazy:")
BASE = input("> ")

connection = mysql.connector.connect(user=USER,
                                    password=PASSWORD, host=IP,
                                    database=BASE,
                                    auth_plugin='mysql_native_password')

cursor = connection.cursor()
sqlEngine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{IP}/{BASE}')
dbConnection = sqlEngine.connect()


print('1 - Wy??wietl tabel??')
print('2 - Wype??nij tabel??')
print('3 - Edytuj zawarto???? tabeli')
print('4 - Usu?? zawarto???? tabeli')
print('5 - Wy??wietl kolumny')
print('6 - Wy??wietl dost??pne bazy')
print('7 - Export do Excela')
print('8 - Zmie?? aktualn?? baz??')
print('9 Poka?? dost??pne tabele')
print('0 - Wyj??cie')




choice = input("> ")

if choice == '1':
    print("Podaj nazw?? tabeli:")
    table = input("> ")
    var = Mysql(table, None, None, None, None)

elif choice == '2':
    print("Podaj nazw?? tabeli:")
    table = input("> ")
    print("Podaj kolumn??:")
    column = input("> ")
    print("Podaj zawardo????:")
    value = input("> ")
    var = Add(table, column, value, None, None)

elif choice == '3':
    print("Kt??r?? tabel?? chcesz edytowa???")
    table = input("> ")
    print("Wg kt??rego ID chcesz edytowa???")
    id = input("> ")
    print("Kt??ra kolumna?:")
    column = input("> ")
    print("Podaj zawarto????:")
    datas = input("> ")
    var = Edit(table, column, None, datas, id)

elif choice == '4':
    print("Z kt??rej tabeli chcesz usun???? zawarto?????")
    table = input("> ")
    print("Kt??ry wiersz usun????? (id):")
    id = input(" >")
    var = Drop(table, None, None, None, id)

elif choice =='5':
    print("Dla kt??rej tabeli chcesz wy??wietli?? kolumny?")
    table = input("> ")
    var = Data(table, None)

elif choice == '6':
    var = Data(None, None)

elif choice == '7':
    var = None
    export()

elif choice == '8':
    Data(None, None).data()
    print("Wybierz baz?? z dost??pnych:")
    base = input("> ")
    var = Data(None, base)

elif choice == '9':
    var = Data(None, None)

elif choice == '0':
    exit(0)
else:
    print("B????d")


login(choice, var)



connection.close()