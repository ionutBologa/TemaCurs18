#1. Scrieti o functie care sa citeasca de la tastatura un numar si incearca sa scada 2 din el.
# In cazul in care utilizatorul nu introduce numar, afiseaza eroare.
import json
from curses.ascii import isdigit


def minusTwo():
    try:
        nr =int(input("nr= "))
        nr-=2
        print(nr)
    except ValueError:
        print("Error : You have to enter a number")

# minusTwo()

#2.Scrieti o functie care citeste de la tastatura 2 numere si caluleaza a/b.
# Verificati ca nu crapa in cazul in care al doilea numar este 0.
def divide():
    try:
        a = int(input('a= '))
        b = int(input('b= '))
        if b==0:
            raise Exception("'b' must be different from '0'")
        div = a / b
        print(div)
    except Exception as e:
        print(f"Error : {e}")

# divide()

#3.Scrieti o functie care citeste un numar n de la tastatura si afiseaza al n-lea element din lista: [2,4,1,4,2].
# Verificati cazul in care indexul nu exista.
def theN():
    list=[2,4,1,4,2]
    print(list)
    try:
        n=int(input('n= '))
        print(f'The "n" element of the list is: {list[n]}')
    except IndexError:
        print("Error: The list don't have the element")

# theN()

#4.Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string.
def aString():
    try:
        string=input("Write your thoughts: ")
        if string.isdigit():
            raise Exception('Please provide a string')
        lenght=len(string)
        print(f'The lenght of your thought is {lenght}')
    except Exception as e :
        print(f"Error : {e}")

# aString()

#5.Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea
dict={"a":1,"b":2,"c":3}
def theReturnOfTheValue():
    try:
        print('Choose a key(a letter) to see the value: ')
        key=input("Select yout key: ")
        print(dict[key])
    except KeyError:
        print("The key doesn't exist")

# theReturnOfTheValue()

#6.Scrieti o functie care primeste numele unui fisier ca parametru si citeste si afiseaza continutul acestuia.
# Tratati cazul in care fisierul nu exista.
def file(textFile):
    try:
        with open(textFile,'r') as file:
            f=file.read()
            print(f'The content of the file: "{f}"')
    except:
        print("The file doesn't exist")

# file('.txt')

#7.Scrieti o functie care primeste ca parametru numele unui fisier json si ridica o exceptie daca fisierul nu este de tip json
def theJsonFile(file):
    name=file.split(".")
    try:
        if name[1]!="json":
            raise Exception("The file is not a '.json' file")
        print('This is a ".json" file')
    except Exception as e:
        print(f'An error has occurred: "{e}"')

# theJsonFile("file.txt")

#8. Modificati problema anterioara pentru a citi fisierul employees.json intr-un obiect de tip json.
# Se va citi un numar de la tastatura. Tratati cazul in care valoarea introdusa de la tastatura nu este numar.
def employees():
    try:
        nr = int(input('Write a number: '))
        with open("employees.json","r")as file:
            f=json.load(file)
    except :
        print('Sorry , you need to provide a number')

# employees()

#9. Modificati problema anterioara pentru a afisa al n-lea element din jsonul citit din fisier.
# Tratati cazul in care elementul N nu exista.
def nElementJson():
    try:
        nr = int(input('Write a number: '))
        with open("employees.json", "r") as file:
            f = json.load(file)
            print(f[nr])
    except:
        print('Sorry , you need to provide a number')

# nElementJson()

#10. Scrieti o functie care citeste fisierul text.txt. De asemenea, functia va citi un numar n de la tastatura.
# De pe fiecare linie afisati al n-lea element. In cazul in care o linie are mai putin elemente de n,
# afisati mesajul: pe linia curenta nu exista N elemente.
def readTheText():
    try:
        with open('file.txt','r') as f:
            file=f.readline()
            n=int(input('n= '))
            for row in file:
                print(file[n])
    except IndexError:
        print("The element doesn't exist")

# readTheText()