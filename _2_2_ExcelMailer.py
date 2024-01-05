import json


from __readExcel import unsent_mail_reciepients
from __sendMail import send_mail


def excel_Mailer():
    # for testing
    applications = json.loads(unsent_mail_reciepients("Purnima_Shrivastava.xlsx"))

    # for prod
    # applications = json.loads(unsent_mail_reciepients())

    sender_mail = applications["sender_mail"]
    user_full_name = applications["user_full_name"]
    contact_number = applications["contact_number"]
    email_address = applications["email_address"]
    college_name = applications["college_name"]

    for application in applications["applications"]:
        send_mail(
            sender_mail,
            user_full_name,
            contact_number,
            email_address,
            college_name,
            *application
        )


excel_Mailer()