from __utilities import create_email_body, create_message


def create_mail(
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
    print(user_full_name)
    if user_full_name == "":
        sender_mail = input("Enter your own email address to send the mails: ")
        user_full_name = input("Enter your full name: ")
        contact_number = input("Enter your contact number: ")
        email_address = input("Enter your email address: ")
        college_name = input("Enter the name of your college: ")
        key_skill_or_quality = input("Enter a key skill or quality you possess: ")
        specific_aspect_of_company = input(
            "Enter a specific aspect of the company you find interesting: "
        )
        recruiter_email = input("Enter the recruiter's email address: ")
        recruiter_name = input("Enter the hiring manager's name: ")
        job_title = input("Enter the job title you are applying for: ")
        company_name = input("Enter the name of the company: ")

    subject = f"{job_title.capitalize()} | Fresh out of college for {company_name.capitalize()}"

    email_body = create_email_body(
        recruiter_name,
        job_title,
        college_name,
        key_skill_or_quality,
        specific_aspect_of_company,
        company_name,
        user_full_name,
        contact_number,
        email_address,
    )

    message = create_message(
        sender_mail, recruiter_email, subject, email_body, filename
    )

    return message


# sender_mail
# user_full_name
# contact_number
# email_address
# college_name
