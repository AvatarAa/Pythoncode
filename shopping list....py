def get_user_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("Please enter 'yes' or 'no'.")

shopping_list = {}

while True:
    print("Your current shopping list is:")
    print("________________________")
    for item, count in shopping_list.items():
        print(f"{item}: {count}")

    add_more = get_user_input("Will you like to add anything else to your list? (yes/no) ")

    if add_more == "yes":
        new_item = input("Add here: ")
        if new_item in shopping_list:
            shopping_list[new_item] += 1
        else:
            shopping_list[new_item] = 1
    elif add_more == "no":
        print("Your shopping list is:")
        print("________________________")

        for item, count in shopping_list.items():
            print(f"{item}: {count}")
        print("THANK YOU")
        break
