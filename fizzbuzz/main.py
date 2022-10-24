a = int(input("Unesi broj izmedu 1 i 100: "))

for broj in range(a, 101):
    if broj%3 == 0 and broj%5 == 0:
        print("FizzBuzz")
        continue
    elif broj%3 == 0:
        print("Fizz")
        continue
    elif broj%5 == 0:
        print("Buzz")
        continue
    else:
        print(broj)
        continue
