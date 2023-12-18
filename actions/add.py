from prettytable import PrettyTable

def add_items(groceries,categories):

    file = open("groceries_list.txt", "w+")
    rows = []
    pretty_table = PrettyTable()

    print("\nIn which of the below categories you want to add?")

    pretty_table.field_names = ["S.NO", "Categories"]
    for idx, category in enumerate(categories):
        rows.append([idx+1,category])
        
    pretty_table.add_rows(rows)

    pretty_table.add_row([str(idx+2),"add_category"])

    print(pretty_table)

    add_op = int(input("Choose an option:"))
    if add_op == (idx+2):
        new_cat = input("Enter the name of the category:")
        categories.append(new_cat)
    else:
        print(
            "What "
            + categories[add_op - 1].replace("_", " ").removesuffix("s")
            + " you want to add?\n"
        )
        item = list(map(str,input("Enter your items:").split()))
        if categories[add_op - 1] in groceries:
            temp = groceries[categories[add_op - 1]]
            temp.extend(item)
            groceries[categories[add_op - 1]] = temp
            del temp
        else:
            groceries[categories[add_op - 1]] = item

    print(str(groceries))

    file.write(str(groceries))
    file.close()

