import pywhatkit


def send_email(*args, **kwargs):
    try:
        my_email = input("Enter your email address: ")
        my_password = input("Enter your password: ")
        mail_to = input("Enter the email address you want to send to: ")
        subject = input("Enter the subject of the email: ")
        content = input("Enter the content of the email: ")
        print("Sending email...")
        pywhatkit.send_mail(email_sender=my_email,
                            password=my_password,
                            subject=subject,
                            message=content,
                            email_receiver=mail_to)
        print("Email sent!")
        return 'Email sent!'
    except Exception as e:
        print(e)
        return 'Email not sent!, Check Error. or Check secure apps is enabled'


if __name__ == "__main__":
    send_email(None)
