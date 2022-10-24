mood = input("Unesi raspolozenje")
mood = mood.lower()

if mood == "happy":
    print("Sretni ste")
elif mood == "sad":
    print("Tuzni ste")
elif mood == "nervous":
    print("Nervozn ste")
else:
    print("Ne poznajem ovo raspolozenje")
