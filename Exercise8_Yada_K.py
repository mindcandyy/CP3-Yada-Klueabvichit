usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput=="mind" and passwordInput=="1234":
    print("Welcome Mind")
    print("----Shop---")
    print("1.Water 5baht")
    print("2.Milk 10baht")
    userselected = int(input(">>"))
    quantity = int(input("quantity: "))
    if userselected==1:
        result = 5*quantity
    elif userselected==2:
        result = 10*quantity
    print(result)

