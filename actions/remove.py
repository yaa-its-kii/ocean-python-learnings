def remove_screen(groceries, categories):

    # remove screen
    items = []
    for key in  groceries:
        for item in groceries[key]:
            items.append((key, item))

    if len(items) == 0:
        print("\nThere are no items to remove")
    else:
        print("\nWhat all do you want to remove?")
    for idx, item in enumerate(items):
        print(f"{idx+1}.{item[1]}")
    if len(items) != 0:
        print(idx+2,'.'+'remove all', sep="")
        
    item_no = list(map(int, input().split()))
    for idx, item in enumerate(items):
        if idx+1 in item_no:
            temp = groceries[item[0]]
            temp.remove(item[1])
            groceries[item[0]] = temp
            
    if idx+2 == item_no[0]:
        groceries.clear()