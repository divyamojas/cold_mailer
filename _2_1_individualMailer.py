import os

from __sendMail import send_mail
from __test_vars import send_mail_args


def individual_mailer():
    os.system("cls")
    print("Hola! Please fillout the form below to send the mail!")

    send_mail(*send_mail_args)
    print()
    input("Click enter to continue..")
