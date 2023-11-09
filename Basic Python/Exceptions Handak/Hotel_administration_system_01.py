class Customer:
    cust_id = 0
    all_accounts = []

    def __init__(self, name, address, mobile_no, email, adharcard_no):
        self.name = name
        self.address = address
        self.mobile_no = mobile_no
        self.email = email
        self.adharcard_no = adharcard_no
        self.cust_id = Customer.cust_id
        Customer.cust_id += 1

    def view_customer(self):
        print("Id:", self.cust_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Mobile No.:", self.mobile_no)
        print("Email Id:", self.email)
        print("Aadhar Card Number:", self.adharcard_no, "\n")
        

class RoomDetails:
    rooms = []
    def __init__(self, room_number, room_type, rate_per_day):
        self.room_number = room_number
        self.room_type = room_type
        self.rate_per_day = rate_per_day
        self.is_booked = False

    def view_rooms(self):
        print("Room Number:", self.room_number)
        print("Room Type:", self.room_type)
        print("Rate per Day:", self.rate_per_day)
        print("Status: Booked" if self.is_booked else "Status: Available", "\n")


class BookingDetail:
    bookings = []
    def __init__(self, customer, room, check_in_date, check_out_date):
        self.customer = customer
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def view_booking(self):
        print("Customer Name:", self.customer.name)
        print("Room Number:", self.room.room_number)
        print("Please Enter Check-in Date :", self.check_in_date)
        print("Please Enter Check-out Date : ", self.check_out_date, "\n")


def main():
    while True:
        print("=" * 30)
        print("Hotel Baba Palace Shirdi".center(30, ' '))
        print("Admin Login".center(30, ' '))
        print("-" * 30)
        user = {"Aditya": "1234"}
        username = input("Please Enter Your Username : ")
        password = input("Please Enter Your Password : ")

        if username in user and user[username] == password:
            print("-" * 30, "\n", username.upper(), "Welcome To The Hotel Baba Palace Shirdi".upper(), "\n", "-" * 30)
            while True:
                print("1. Add Customer")
                print("2. View Customer")
                print("3. Add Room")
                print("4. View Room")
                print("5. Add Booking")
                print("6. View Bookings")
                print("7. Generate Invoice")
                print("8. Logout")
                ch = int(input("Please Enter your Choice : "))

                if ch == 1:
                    name = input("Please enter your name: ")
                    address = input("Please enter your address: ")
                    mobile_no = int(input('Please enter your mobile number: '))
                    email = input('Please enter your email id: ')
                    adharcard_no = int(input('Please enter your aadhar card number: '))
                    customer = Customer(name, address, mobile_no, email, adharcard_no)
                    Customer.all_accounts.append(customer)
                elif ch == 2:
                    for customer in Customer.all_accounts:
                        customer.view_customer()
                elif ch == 3:
                    room_number = input("Please enter room number: ")
                    room_type = input("Please enter room type: ")
                    rate_per_day = float(input("Please enter rate per day: "))
                    room = RoomDetails(room_number, room_type, rate_per_day)
                    RoomDetails.rooms.append(room)
                elif ch == 4:
                    for room in RoomDetails.rooms:
                        room.view_rooms()
                elif ch == 5:
      
                    check_in_date = input("Please enter check-in date: ")
                    check_out_date = input("Please enter check-out date: ")
                    booking = BookingDetail(customer, room, check_in_date, check_out_date)
                    BookingDetail.bookings.append(booking)
                elif ch == 6:
                    for booking in BookingDetail.bookings:
                        booking.view_booking()
                elif ch == 7:
                    pass
                elif ch == 8:
                    print("-" * 60, "\nThank U For Visit Our Python Hotel Administration System\nDesign & Devloped By | Aditya Kamble\n",
                          "-" * 60)
                    break
        else:
            print("Invalid Username or Password, Please Try Again")
            continue


if __name__ == "__main__":
    main()
