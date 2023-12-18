def view_screen(groceries):

    # view screen

    print("\nYour added products")

    n = 1
    
    for key in groceries:
        for item in groceries[key]:
            print(n,item,sep=".")
            n += 1
    print()