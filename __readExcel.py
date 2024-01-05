import json
import openpyxl


def unsent_mail_reciepients(excel_filename=""):
    if excel_filename == "":
        input("Please enter the file name: ")

    workbook = openpyxl.load_workbook(excel_filename)

    worksheet = workbook["Sheet1"]

    sender_mail = worksheet["K2"].value
    user_full_name = worksheet["L2"].value
    contact_number = worksheet["M2"].value
    email_address = worksheet["N2"].value
    college_name = worksheet["O2"].value

    all_applications = []
    for row in worksheet.iter_rows(min_row=2, max_col=9):
        cells = [cell.value for cell in row[:8]]

        if row[8].value:
            continue

        all_applications.append(cells)


    return json.dumps(
        {
            "sender_mail": sender_mail,
            "user_full_name": user_full_name,
            "contact_number": contact_number,
            "email_address": email_address,
            "college_name": college_name,
            "all_applications": all_applications,
        }
    )


# unsent_mail_reciepients("Purnima_Shrivastava.xlsx")
