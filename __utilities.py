# Helper function to create message
import base64
from email import encoders
import email
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_message(sender, to, subject, message_text, file):
    message = MIMEMultipart()
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    message.attach(MIMEText(message_text, "html"))

    with open(file, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={file}")
        message.attach(part)

    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {"raw": raw}


def create_email_body(
    recruiter_name,
    job_title,
    college_name,
    key_skill_or_quality,
    specific_aspect_of_company,
    company_name,
    user_full_name,
    contact_number,
    email_address,
):
    # Generate email text
    email_text = f"""<html>
        <body>
          <p>Dear {recruiter_name.capitalize()},</p>
          <p>I hope you're doing great!</p>
          <p>I came across the job opening of {job_title} at {company_name.capitalize()} and this role really excites me!</p>
          <p>I am currently in my final year at {college_name}, I'm set to graduate soon and would love to bring my {key_skill_or_quality.lower()} to your awesome team. What excites me most about {company_name.capitalize()} is {specific_aspect_of_company}.</p>
          <p>I'd welcome the opportunity to discuss how my skills and enthusiasm can benefit {company_name.capitalize()}. Please let me know your availability for a quick call or an interview.</p>
          <p>Thank you for your time and consideration.</p>
          <p>Sincerely,</p>
          <p>{user_full_name}<br/>
          {contact_number}<br/>
          {college_name}</p>
        </body>
        </html>
        """

    return email_text
