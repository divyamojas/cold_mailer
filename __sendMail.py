from __future__ import print_function

import os


from __createMail import create_mail
from __auth import auth_setup


def send_mail(
    sender_mail="",
    user_full_name="",
    contact_number="",
    email_address="",
    college_name="",
    key_skill_or_quality="",
    specific_aspect_of_company="",
    recruiter_email="",
    recruiter_name="",
    job_title="",
    company_name="",
    filename="",
):
    os.system("cls")

    service = auth_setup()

    # Will be used in Prod
    # message = create_mail()

    # For testing
    message = create_mail(
        sender_mail,
        user_full_name,
        contact_number,
        email_address,
        college_name,
        key_skill_or_quality,
        specific_aspect_of_company,
        recruiter_email,
        recruiter_name,
        job_title,
        company_name,
        filename,
    )

    # Send the email
    try:
        message = service.users().messages().send(userId="me", body=message).execute()
        print("Message Id: %s" % message["id"])
        print("Email sent successfully!")
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
