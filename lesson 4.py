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

        userinput = input("Add another item (menu: 1), remove an item (menu: 2), or done (menu: 3)? ").lower()

        if userinput == "2":
            userinput2 = input("1. remove item 2. pop item")

            if userinput2 == "1":
                userinput3 = input("What do you want to remove? ")
                if userinput3 in shopping_list:
                    shopping_list.remove(userinput3)
                    print("Shopping list after removing '{}':".format(userinput3))
                    print("________________________")
                    print("\n".join(shopping_list))
                else:
                    print("'{}' not found in shopping list.".format(userinput3))

        break
    else:
        print("Please enter 'yes' or 'no'.")

print("Thank you, sir.")