class Customer():
    c_id = 0
    cust_list = []

    def __init__(self, c_name, c_address, c_mobile):
        self.c_name = c_name
        self.c_address = c_address
        self.c_mobile = c_mobile
        self.id = Customer.c_id
        Customer.c_id += 1

    def customerInfo(self):
        print("Customer Id :", self.id)
        print("Customer Name :", self.c_name)
        print("Customer Address :", self.c_address)
        print("Customer Mobile :", self.c_mobile)

    @classmethod
    def add_customer(cls):
        c_name = input("Please Enter Your Sweet Name: ")
        c_address = input("Please Enter Your Current Address: ")
        try:
            c_mobile = int(input("Please Enter Your Mobile: "))
        except ValueError as e:
            print('Invalid mobile number')
            customer_obj = cls(c_name, c_address, c_mobile)
            cls.cust_list.append(customer_obj)
            print("-" * 50)
            print("WELCOME", customer_obj.c_name.upper())
            print("Thank You For your Registration")
            print("-" * 50)


class Bill:
    total_products = []
    total_sales = 0
    id = 0

    def __init__(self, name, price, brand, category, quantity):
        self.name = name
        self.price = price
        self.brand = brand
        self.category = category
        self.prod_quantity = quantity
        self.id = Bill.id
        Bill.id += 1

    def view_product(self):
        print("-" * 50)
        print("\t\tID       |", self.id)
        print("\t\tName     |", self.name)
        print("\t\tPrice    |", self.price)
        print("\t\tBrand    |", self.brand)
        print("\t\tCategory |", self.category)
        print("\t\tQuantity |", self.prod_quantity)
        print("-" * 50)

    @classmethod
    def add_product(cls):
        print("Add Product".center(30, '-'))
        name = input('Please Enter Product Name: ')
        try:
            price = int(input('Please Enter Price of Product: '))
        except:
            print("Invalid Input ! Please enter price our product ")
            brand = input("Please Enter Product Brand: ")
            category = input("Please Enter Product Category: ")
        try:
            quantity = int(input("Please Enter Quantity: "))
        except:
            print("Invalid Input! Please enter a valid number")
            obj = cls(name, price, brand, category, quantity)
            cls.total_products.append(obj)
            print("-" * 30)
            print("Product added successfully!")
            print("-" * 30)

    @classmethod
    def view_all_products(cls):
        print("-" * 50)
        print("View All Products".center(50, '-'))
        if cls.total_products:
            for product in cls.total_products:
                product.view_product()
                print("-" * 50)
        else:
            print("No products available.")

    @classmethod
    def invoice(cls, purchased_products, cust_obj, quantity_list):
        print("=" * 30)
        print("Invoice".center(30, '-'))
        print("=" * 30)
        total_amount = 0
        for i in range(len(purchased_products)):
            product = purchased_products[i]
            prod_id, quantity = quantity_list[i]
            for obj in cls.total_products:
                if prod_id == obj.id:
                    print("Product |", product.name)
                    print("Price   |", product.price)
                    print("Quantity|", quantity)
                    product.prod_quantity -= quantity
                    total_amount += product.price * quantity
                    print("-" * 30)
                    break
        cls.total_sales += total_amount
        print("Total Amount :", total_amount, "\nThank You Visit Again")
        print("-" * 30)


    @classmethod
    def main(cls):
        while True:
            print("=" * 50)
            print("Welcome To The Billing System".center(50, '-').upper())
            print("=" * 50)
            print("1.Add Product")
            print("2.View All Products")
            print("3.Generate Invoice")
            print("4.Add Customer")
            print("5.Total Sales")
            print("6.Exit")

            try:
                ch = int(input("Please Enter a Choice: "))
            except:
                print("Please Enter only digit number ")
            if ch == 1:
                cls.add_product()
            elif ch == 2:
                cls.view_all_products()
            elif ch == 3:
                purchased_prod_ids = input("Enter Product ID : ")
                purchased_prod_quantity = input("Enter Quantity: ")
                purchased_products = []
                quantity_list = [(int(prod_id), int(quantity)) for prod_id, quantity in zip(purchased_prod_ids, purchased_prod_quantity)]

                for prod_id, quantity in quantity_list:
                    for obj in cls.total_products:
                        if prod_id == obj.id:
                            purchased_products.append(obj)
                            

                mobile = int(input("Enter Customer Mobile No: "))
                cust_exists = False

                for obj in Customer.cust_list:
                    if mobile == obj.c_mobile:
                        cust_exists = True
                        cust_obj = obj

                if cust_exists:
                    cls.invoice(purchased_products, cust_obj, quantity_list)
                else:
                    c_name = input("Please Enter Your Sweet Name: ")
                    c_address = input("Please Enter Your Current Address: ")

                    try:
                        c_mobile = int(input("Please Enter Your Mobile: "))
                    except:
                        print()
                    customer_obj = Customer(c_name, c_address, c_mobile)
                    Customer.cust_list.append(customer_obj)
                    cls.invoice(purchased_products, customer_obj, quantity_list)
            elif ch == 4:
                Customer.add_customer()
            elif ch == 5:
                print("-" * 40)
                print("Total Sales :", cls.total_sales)
                print("-" * 40)
            elif ch == 6:
                print("Thank U For Visit Our Python Billing System\nDesign & Devloped By | Aditya Kamble")
                break
            else:
                print("Invalid Choice")

if __name__ == "__main__":
    obj = Bill("", 0, "", "", 0)
    obj.main()
