max_lenght = 3

while True:
    bread= input("input name\n maximum of 3 characters")
    if len(bread) > max_lenght:
        print("variable to long \n try again please")
    else:
        print(bread.replace(f"you may proceed bitch"))
        break

