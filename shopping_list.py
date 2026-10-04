shopping = []

while True:
    choice = input("\nadd / remove / show / done: ").strip().lower()

    if choice == "add":
        item = input("Item to add: ").strip()
        shopping.append(item)
        print(item, "added.")

    elif choice == "remove":
        item = input("Item to remove: ").strip()
        if item in shopping:
            shopping.remove(item)
            print(item, "removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        for item in shopping:
            print(item)

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Please type add, remove, show or done.")