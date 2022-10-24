print("Program sluzi za konverziju kilometara u milje")

upit = "y"

def promjena(kilometri):
    povrat = float(kilometri) / 1.609
    return str(round(povrat, 21))

while(upit == "y"):
    km = input("Unesi kilometre: ")
    print(km + " je " + promjena(km) + " kilometara")
    upit = input("Zelis dalje? y/n: ")



