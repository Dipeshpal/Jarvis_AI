import pywhatkit as kit


def send_whatsapp_message(*arg, **kwargs):
    country_code = input("Enter country code (Default=+91): ") or "+91"
    number = input("Enter whatsapp number: ")
    message = input("Enter message: ")
    print("Sending message...")
    kit.sendwhatmsg_instantly(f"{country_code}{number}", message, wait_time=20)
    print("Message sent successfully!")


if __name__ == "__main__":
    send_whatsapp_message()
