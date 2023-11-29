groceries = {}
cate = ["diary_products", "meat_products", "snacks", "grains"]


while True:
    print("Menu:\n\n1.Add\n2.Remove\n3.View\n4.Exit")

    op = int(input("Choose an option:"))
    if op == 1:
        # add screen
        print("\nIn which of the below categories you want to add?")
        for i, k in enumerate(cate):
            print(str(i + 1) + "." + k)
        add_op = int(input("Choose an option:"))
        print(
            "What "
            + cate[add_op - 1].replace("_", " ").removesuffix("s")
            + " you want to add?\n"
        )
        item = input("Enter your item:")
        if cate[add_op - 1] in groceries:
            temp = groceries[cate[add_op - 1]]
            temp.append(item)
            groceries[cate[add_op - 1]] = temp
        else:
            groceries[cate[add_op - 1]] = [item]

    if op == 2:
        # remove screen
        print("\nWhat all do you want to remove?")
        m = 1
        for items in  groceries.values():
            for item in items:
                print(f"{m}.{item}")
                m += 1
        
        input()
    if op == 3:
        # view screen
        print(groceries)
    if op == 4:
        break
