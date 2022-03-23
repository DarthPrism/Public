import mysql.connector, os, sys
from sys import exit
from tabulate import tabulate
import panda

try:

    connection = mysql.connector.connect(user='root', password='CigaroM12', host='127.0.0.1',
    database='ewidencja_krow', auth_plugin='mysql_native_password')
    cursor = connection.cursor()
except:

    print("Podaj hasło:")
    haslo = input("> ")
    connection = mysql.connector.connect(user='root', password=haslo, host='127.0.0.1',
    database='ewidencja_krow', auth_plugin='mysql_native_password')
    cursor = connection.cursor()

word_list = {
    '0' : 'id',
    '1' : 'numer_kolczyka',
    '2' : 'data_urodzenia',
    '3' : 'data_zakupu',
    '4' : 'cena_zakupu',
    '5' : 'waga_1',
    '6' : 'waga_2',
    '7' : 'waga_3',
    '8' : 'waga_4',
    '9' : 'data_sprzedazy',
    '10' : 'cena_sprzedazy',
    '11' : 'wartosc_sprzedazy'
}

def delete():
    print("Który wiersz usunąć? (id):")
    id = input(" >")
    sql = "DELETE FROM krowy WHERE id=" + str(id)
    cursor.execute(sql)
    connection.commit()
    connection.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

def add():

        print("Numer kolczyka (ostatnie 4 cyfry):")
        numer_kolczyka_inp = input("> ")
        print("Podaj datę urodzenia (RRRR-MM-DD):")
        data_urodzenia_inp = input("> ")
        print("Podaj datę zakupu (RRRR-MM-DD):")
        data_zakupu_inp = input("> ")
        print("Podaj cene zakupu:")
        cena_zakupu_inp = input("> ")

        insertQuery = "INSERT INTO krowy(numer_kolczyka, data_urodzenia, data_zakupu, cena_zakupu) VALUES(%(numer_kolczyka)s, %(data_urodzenia)s, %(data_zakupu)s, %(cena_zakupu)s)"
        insertData = {
            'numer_kolczyka' : numer_kolczyka_inp,
            'data_urodzenia' : data_urodzenia_inp,
            'data_urodzenia' : data_urodzenia_inp,
            'data_zakupu' : data_zakupu_inp,
            'cena_zakupu' : cena_zakupu_inp
        }
        cursor.execute(insertQuery, insertData)
        connection.commit()
        connection.close()
        os.execl(sys.executable, sys.executable, *sys.argv)

def edit():

    print("Którą kolumnę chcesz edytować?")
    print("""
        0 - id
        1 - numer_kolczyka
        2 - data_urodzenia
        3 - data_zakupu
        4 - cena_zakupu
        5 - waga_1
        6 - waga_2
        7 - waga_3
        8 - waga_4
        9 - data_sprzedazy
        10 - cena_sprzedazy
        11 - wartosc_sprzedazy
        """)
    choice = input("> ")
    print('Wg którego nr Id chcesz edytować?')
    id_inp = input("> ")
    print("Dane dla kolumny: ")
    choice_1 = input("> ")

    insertEdit = ("UPDATE krowy SET "+word_list[choice]+" = "+choice_1+" WHERE id = %(id_inp)s")

    insertData = {
        'list' : word_list[choice],
        'choice_1' : choice_1,
        'id_inp' : id_inp
        }

    cursor.execute(insertEdit, insertData)
    connection.commit()
    connection.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

def select():

    query = """SELECT * FROM krowy"""
    cursor.execute(query)


    list = {
        'id' : [],
        'numer_kolczyka' : [],
        'data_urodzenia' : [],
        'data_zakupu' : [],
        'cena_zakupu' : [],
        'waga_1' : [],
        'waga_2' : [],
        'waga_3' : [],
        'waga_4' : [],
        'data_sprzedazy' : [],
        'cena_sprzedazy' : [],
        'wartosc_sprzedazy' : []
    }

    for (id, numer_kolczyka, data_urodzenia, data_zakupu, cena_zakupu, waga_1, waga_2, waga_3, waga_4, data_sprzedazy, cena_sprzedazy, wartosc_sprzedazy) in cursor:
        list["id"].append(id)
        list["numer_kolczyka"].append(numer_kolczyka)
        list["data_urodzenia"].append(data_urodzenia)
        list["data_zakupu"].append(data_zakupu)
        list["cena_zakupu"].append(cena_zakupu)
        list["waga_1"].append(waga_1)
        list["waga_2"].append(waga_2)
        list["waga_3"].append(waga_3)
        list["waga_4"].append(waga_4)
        list["data_sprzedazy"].append(data_sprzedazy)
        list["cena_sprzedazy"].append(cena_sprzedazy)
        list["wartosc_sprzedazy"].append(wartosc_sprzedazy)


    print(tabulate(list, headers='keys', tablefmt='fancy_grid'))
    os.execl(sys.executable, sys.executable, *sys.argv) # restart programu


print('1 - Wyświetl tabelę')
print('2 - Wypełnij tabelę')
print('3 - Edytuj zawartość tabeli')
print('4 - Usuń zawartość tabeli')
print('5 - Wyjście')

wybor_1 = input("> ")

if wybor_1 == "1":

    select()

elif wybor_1 == "2":

    add()

elif wybor_1 == "4":

    delete()

elif wybor_1 == "3":

    edit()

elif wybor_1 == '5':

    exit(0)
else:
    print("Wybierz ponownie!")
    os.execl(sys.executable, sys.executable, *sys.argv)

connection.commit()
connection.close()
