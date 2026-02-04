import random
import time

OTP_VALIDITY_SECONDS = 60

def generate_otp():
    return random.randint(100000, 999999)

def send_otp_simulation(otp):
    # Simulating OTP delivery (email/SMS)
    print(f"\n[SIMULATION] Your OTP is: {otp}")

def verify_otp(sent_otp, user_otp, generated_time):
    if time.time() - generated_time > OTP_VALIDITY_SECONDS:
        return "⛔ OTP Expired"

    if sent_otp == user_otp:
        return "✅ Authentication Successful"
    else:
        return "❌ Invalid OTP"

def main():
    print("Two-Factor Authentication System")
    print("--------------------------------")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Dummy credentials check
    if username != "admin" or password != "password123":
        print("❌ Invalid credentials")
        return

    otp = generate_otp()
    generated_time = time.time()

    send_otp_simulation(otp)

    try:
        user_otp = int(input("\nEnter OTP: "))
    except ValueError:
        print("❌ OTP must be numeric")
        return

    result = verify_otp(otp, user_otp, generated_time)
    print(result)

if __name__ == "__main__":
    main()
