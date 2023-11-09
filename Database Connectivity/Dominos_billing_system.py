#15/08/2023


print("WELCOME TO DOMINO'S BILLING SYSTEM")
while True:
    print("1.Add Menu")
    print("2.Order")
    print("3.Exit")
    ch = int(input("Please enter what to do :"))
    menu=[]

    def display_menu():
        for i in range (len(menu)):
            print(i+1,".",menu[i])

    if ch == 1:
        while True:
            print("\n\tMENU ADDITION MENU:")
            print("1.ADD NEW ITEM")
            print("2.BACK")
            ch = int(input("Enter what to do :"))
            if ch==1:
                name = input('Name of the item:')
                price = float (input ('Price :' ))
                category = input('Which category :')
                menu.append([name,price,category])
                print("Item Added Successfully")
            elif ch == 2:
                print("Exit")
                break
            else:
                print("Invalid choice please try again")
    elif ch == 2:
        u_name = input("Enter your name :")
        u_mobile = input("Enter your mobile no :")
        print(u_name.upper()+" WELCOME")
        display_menu()

        order = {'name':u_name,'Mobile':u_mobile,'Item':[]}

        while True:
            try:
                item_choice = int(input("Enter the item number you want to order (0 to finish): "))
                if item_choice == 0:
                    break
                elif 1 <= item_choice <= len(menu):
                    order['items'].append(menu[item_choice - 1])
                    print(f"{menu[item_choice - 1]['name']} added to your order.")
                else:
                    print("Invalid item number, please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid item number.")

        orders.append(order)
        print("Order placed successfully!")

    elif choice == 3:
        # print("\nORDER HISTORY:")
        # for index, order in enumerate(orders, start=1):
        #     print(f"Order {index} - {order['name']} ({order['mobile']})")
        #     for item in order['items']:
        #         print(f"  {item['name']} - ${item['price']}")
        pass

    elif choice == 4:
        print("Exiting the program")
        break

    else:
        print("Invalid choice, please try again")
        continue
