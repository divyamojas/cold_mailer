import json
import openpyxl


def unsent_mail_reciepients(excel_filename=""):
    

    if excel_filename == "":
        input("Please enter the file name: ")

    workbook = openpyxl.load_workbook(excel_filename)

    worksheet = workbook["Sheet1"]  # Replace "Sheet1" with the actual sheet name

    sender_mail = worksheet["L2"].value
    user_full_name = worksheet["L3"].value
    contact_number = worksheet["L4"].value
    email_address = worksheet["L5"].value
    college_name = worksheet["L6"].value

    all_applications = []
    for row in worksheet.iter_rows(min_row=2, max_col=9):
        cells = [cell.value for cell in row[:7]]
        
        if row[7].value:
            continue

        all_applications.append(cells)


    return json.dumps(
        {
            "sender_mail": sender_mail,
            "user_full_name": user_full_name,
            "contact_number": contact_number,
            "email_address": email_address,
            "college_name": college_name,
            "applications": all_applications,
        }
    )

# unsent_mail_reciepients("Purnima_Shrivastava.xlsx")
