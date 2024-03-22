shopping_list = []

while True:
    print("Your current shopping list is:")
    print("________________________")
    print("\n".join(shopping_list))

    add_more = input("Will you like to add anything else to your list? (yes/no) ").lower()

    if add_more == "yes":
        new_item = input("Add here: ")
        shopping_list.append(new_item)
    elif add_more == "no":
        print("Your shopping list is:")
        print("________________________")

        print("\n".join(shopping_list))



        userinput = input("add another item menu:1\n remove item menu:2").lower()

        if userinput == "2":
            userinput == input("1. remove item 2. pop item")

             if userinput == "1":
                 userinput4 = input("what do you want to remove")
                 shopping_list.remove(userinput4)
                 print(shopping_list)
        break

print("Thank you, sir.")