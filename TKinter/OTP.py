from twilio.rest import Client
import random

# Replace these with your actual Twilio credentials
account_sid = 'ACd703f30e1360a2f06245f1bf7d1ca051'
auth_token = 'ced92775d244265dec785e7ad13db25a'
twilio_phone_number = '8329902128'  # This is the phone number Twilio provides

client = Client(account_sid, auth_token)

# Generate a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Send OTP via SMS using Twilio
def send_otp_via_twilio(user_phone_number, otp):
    message = client.messages.create(
        body=f'Your OTP is: {otp}',
        from_=twilio_phone_number,
        to=user_phone_number
    )
    print(f"OTP sent to {user_phone_number} via Twilio.")

# Verify the entered OTP
def verify_otp(entered_otp, generated_otp):
    return entered_otp == generated_otp

# Example usage
user_phone_number = '8329902128'  # Replace with user's actual phone number
generated_otp = generate_otp()
send_otp_via_twilio(user_phone_number, generated_otp)

entered_otp = input("Enter the OTP sent to your phone: ")
if verify_otp(entered_otp, generated_otp):
    print("OTP verified successfully. User authenticated.")
else:
    print("OTP verification failed. Please try again.")
