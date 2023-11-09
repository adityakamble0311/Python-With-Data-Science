class Customer:
    cust_id = 1
    customer_list = []

    def __init__(self,name,address,mobile):
        self.cust_id = Customer.cust_id + 1
        self.cust_name = name
        self.cust_address = address
        self.cust_mobile = mobile
        Customer.cust_id+=1

    def customerInfo(self):
        print("Customer Id:",self.cust_id)
        print("Customer Name:",self.cust_name)
        print("Address:",self.cust_address)
        print("Mobile:",self.cust_mobile)

class Product:

    prod_id = 0
    products_list = []
    total_sales = 0
    def __init__(self,prod_name,prod_category,prod_price,prod_brand,prod_quantity):
        self.prod_id = Product.prod_id + 1
        self.prod_name = prod_name
        self.prod_category = prod_category
        self.prod_price = prod_price
        self.prod_brand = prod_brand
        self.prod_quantity = prod_quantity
        Product.prod_id+=1

    def productInfo(self):
        print()
        print("Product Id:",self.prod_id)
        print("Product Name:",self.prod_name)
        print("Product Brand:",self.prod_brand)
        print("Product Price:",self.prod_price)
        print("Product Category:",self.prod_category)
        print("Product Quantity:",self.prod_quantity)


def bill(purchased_products,cust_obj,quantity_list):
    cust_obj.customerInfo()
    print("Products Lists".center(30,'-'))
    total = 0
    for obj,quantity in zip(purchased_products,quantity_list):
        print("{}\t{}\t{}\t{}\t{}\t{}".format(obj.prod_id,obj.prod_name,obj.prod_brand,obj.prod_price,obj.prod_category,quantity))
        obj.prod_quantity-=quantity
        total+=obj.prod_price*quantity
    print("Total:",total)
    Product.total_sales+=total




def main():
     
    while True:
        print()
        print("1.Add Products")
        print("2.View Products")
        print("3.Billing")
        print("4.Add Customer")
        print("5.Total Sales")
        ch = int(input("Enter Choice: "))

        if ch == 1:
            prod_name = input("Product Name: ")
            prod_brand = input("Brand: ")
            prod_price = float(input("Price: "))
            prod_category = input("Product Category: ")
            prod_quantity = int(input("Product Quantity: "))
            prod_exists = False
            for obj in Product.products_list:
                if obj.prod_name == prod_name and obj.prod_brand == prod_brand and obj.prod_price == prod_price and obj.prod_category == prod_category:
                    prod_exists = True
                    prod_obj = obj
                
            if prod_exists == True:
                prod_obj.prod_quantity+=prod_quantity
            else:    
                obj = Product(prod_name,prod_category,prod_price,prod_brand,prod_quantity)
                Product.products_list.append(obj)

        elif ch == 2:
            for obj in Product.products_list:
                obj.productInfo()

        elif ch == 3:
            purchased_prod_ids = [int(x) for x in input("Enter Product Id <Space> followed by Quantity: ").split()]
            purchased_products = []
            quantity_list = []
            for i in range(1,len(purchased_prod_ids),2):
                quantity_list.append(purchased_prod_ids[i])
            for prod_id in purchased_prod_ids :
                for obj in Product.products_list:
                    if prod_id == obj.prod_id:
                        purchased_products.append(obj)
            mobile = int(input("Enter Customer Mobile No: "))
            cust_exists = False
            for obj in Customer.customer_list:
                if mobile == obj.cust_mobile:
                    cust_exists = True
                    cust_obj = obj
            
            if cust_exists == True:
                bill(purchased_products,cust_obj,quantity_list)
            else:
                cust_name = input("Enter Customer Name: ") 
                cust_address = input("Enter Customer Addresss: ")
                cust_mobile = int(input("Customer Mobile No: ")) 
                customer_obj = Customer(cust_name,cust_address,cust_mobile)
                Customer.customer_list.append(customer_obj)
                bill(purchased_products,customer_obj,quantity_list)

        elif ch == 4:
            cust_name = input("Enter Customer Name: ") 
            cust_address = input("Enter Customer Addresss: ")
            cust_mobile = int(input("Customer Mobile No: ")) 
            customer_obj = Customer(cust_name,cust_address,cust_mobile)
            Customer.customer_list.append(customer_obj)
            print(customer_obj.cust_name,"Welcome")
            print("Customer Id:",customer_obj.cust_id)

        elif ch == 5:
            print("Total Sales:",Product.total_sales)
            
        else:
            print("Wrong Input")

main()


