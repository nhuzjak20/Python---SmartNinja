import random

#pokusaji se vraca ispod nule iako postavim uvjet, to ne znam zašto ali tu primarno sve radi

prvi_broj = input("Od kojeg broja zelis nasumicno(manji broj): ")
drugi_broj = input("Do kojeg broja zelis(najveci): ")

prvi_broj = int(prvi_broj)
drugi_broj = int(drugi_broj)

broj = random.randint(prvi_broj, drugi_broj)
unos = 0
pokusaji = 4

while(unos!=broj or pokusaji >= 1):
    unos = input("Unesi broj: ")
    unos = int(unos)
    pokusaji = int(pokusaji)
    if unos > broj:
        print("Broj je preveliki. Imate " + str(pokusaji) + " pokusaja")
        pokusaji = pokusaji - 1
    elif unos < broj:
        print("Broj je premali. Imate " + str(pokusaji) + " pokusaja" )
        pokusaji = pokusaji - 1
    elif pokusaji == 0:
        print("Iskoristili te pokusaje")
        exit()
    else:
        print("pogodili ste broj")
        exit()
