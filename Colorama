#Usando colorama sería:

from colorama import Fore, Style

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

interseccion = conjunto1.intersection(conjunto2)

print(Fore.BLUE + "Conjunto 1:", end=" ")
for elemento in conjunto1:
    if elemento in interseccion:
        print(Fore.RED + str(elemento), end=" ")
    else:
        print(elemento, end=" ")
print()

print(Fore.BLUE + "Conjunto 2:", end=" ")
for elemento in conjunto2:
    if elemento in interseccion:
        print(Fore.RED + str(elemento), end=" ")
    else:
        print(Fore.BLUE + str(elemento), end=" ")
print()

print(Fore.BLUE + "Intersección:", end=" ")
for elemento in interseccion:
    print(Fore.RED + str(elemento), end=" ")
print()

print(Style.RESET_ALL)  # Restaurar el estilo original de la consola
