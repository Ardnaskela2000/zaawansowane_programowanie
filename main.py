# Zestaw 1

#Zad 2 a
#W parametrze lista 5 imion i każde z nich wyświetlić

names = ["Kamil", "Anna", "Joanna", "Adam", "Tomek"]

def print_names_list(names):
 for name in names:
    print(name)

print_names_list(names)



# Zad 2_b
#5 dowolnych liczb, które pomnożyć przez 2 i potem zwrócić

#wersja_1 - petla for

numbers = [22, 12, 32, 11, 3]

def print_double_numbers(numbers):
 number_list = []
 for number in numbers:
    number_list.append(number * 2)
 print(number_list)

print_double_numbers(numbers)


#wrsja_2 - lista składowa

numbers = [22, 12, 32, 11, 3]

def print_double_numbers_2(numbers):
    number_list_2 = [number * 2 for number in numbers]
    print(number_list_2)

print_double_numbers_2(numbers)


#Zad 2 c
#lista 10 liczb przez range i wyświetli parzyste

for i in range(10):
    if i % 2 ==0:
        print(i)



#zad 2 d
#lista 10 liczb i wyświetla co drugą

for i in range (10):
    if i % 2:
        print(i)


#Zestaw 2

#Zad 1
# argumenty name i surname i zwrócić

name = "Adam"
surname = "Kowalski"

def print_person(name,surname):
    return f'Cześć, {name } {surname}'

talk = print_person(name,surname)
print(talk)


#Zad 2
# zwrócenie mnozenia 2 liczb

def mnozenie(x,y):
    return x * y

wynik = mnozenie(6,3)
print(wynik)


#Zad 3
#sprawdzenie czy parzyste i zwrócenie jako bool true/faulse

def czy_parzyste(i):
    if i % 2 ==0:
       return True
    else:
        return False

wynik = czy_parzyste(2)

if (wynik):
    print("Liczba pzrysta")
else:
    print("Liczba nieparzysta")


#Zad 4
#3 argumenty



def czy_wieksze(number_1, number_2, number_3):
    if number_1 + number_2 > number_3:
        return True
    else:
        return False

sprawdzenie = czy_wieksze(2,3,8)

if (sprawdzenie):
    print("Prawda")
else:
    print("Fałsz")


#Zad 5

def czy_przyjmuje_list(list: list, liczba:int) -> bool:
    if liczba in list:
        return True
    else:
        return False

lista = czy_przyjmuje_list([24,34],24)

if (lista):
    print("Prawda")
else:
    print("Fałsz")


#Zad 6

def skomplikowane(lista_1:list, lista_2:list) -> bool:
    listy = lista_1 + lista_2
    listy = set(listy)

    argum = []
    for elementy in listy:
        argum.append(elementy**3)

    for elementy in argum:
        print(elementy)

    return argum

listy = skomplikowane([2,3], [1,2])

