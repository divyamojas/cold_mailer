import json
import openpyxl


from __readExcel import unsent_mail_reciepients
from __sendMail import send_mail


def excel_Mailer():
    # for testing
    excel_filename = "Purnima_Shrivastava.xlsx"
    applications = json.loads(unsent_mail_reciepients(excel_filename))

    workbook = openpyxl.load_workbook(excel_filename)

    worksheet = workbook["Sheet1"]

    sender_mail = applications["sender_mail"]
    user_full_name = applications["user_full_name"]
    contact_number = applications["contact_number"]
    email_address = applications["email_address"]
    college_name = applications["college_name"]

    count = 0
    for i in range(0, len(applications["all_applications"])):

        mail_sent = send_mail(
            sender_mail,
            user_full_name,
            contact_number,
            email_address,
            college_name,
            *((applications["all_applications"][i])[1:]),
        )
        worksheet[f"I{(applications["all_applications"][i])[0] + 1}"].value = mail_sent
        workbook.save(excel_filename)

        if mail_sent:
            count += 1

    if count > 0:
        print(f'Congrats! {count} mails sent successfully just now.')
    else:
        print("Sorry no mails were sent :(")
        print("Please check the excel sheet which mails weren't sent.")
    print()
    input("Click enter to proceed..")
