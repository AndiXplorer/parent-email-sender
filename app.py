import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import csv
import re

# Email credentials (use environment variables for sensitive data)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  # Replace with your environment variable
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Replace with your environment variable

# CC recipients
CC_RECIPIENTS = ['example1@example.com', 'example2@example.com']  # Replace with actual CC emails if needed

# Read email list from CSV
def get_email_list(file_path):
    email_list = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            email_list.append(row)  # Each row contains {'name': 'Student Name', 'email': 'parent_email'}
    return email_list

# Sanitize the filename to extract only the student's name from it
def sanitize_filename(student_name):
    # Return the name exactly as the filename is supposed to match the structure
    return f"Raport template Ora sfiduese - {student_name} - Web Fundamentals.pdf"

# Send email function
def send_email(recipient_email, recipient_name, attachment_path):
    try:
        # Set up the MIME message
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = recipient_email
        message['Cc'] = ', '.join(CC_RECIPIENTS)  # Add CC recipients
        message['Subject'] = "Subject Placeholder - Progress Report"

        # Email body (Lorem Ipsum text)
        body = f"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus viverra nulla ut metus varius laoreet. 
Suspendisse potenti. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. 
Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.
"""
        message.attach(MIMEText(body, 'plain'))

        # Sanitize the filename and construct the correct path
        sanitized_filename = sanitize_filename(recipient_name)
        certificate_path = os.path.join(os.path.dirname(attachment_path), sanitized_filename)

        # Log the certificate path for debugging
        print(f"Certificate path: {certificate_path}")
        
        if not os.path.exists(certificate_path):
            print(f"Certificate not found: {certificate_path}")
            return  # Skip sending the email if the file doesn't exist

        # Attach the PDF
        with open(certificate_path, 'rb') as attachment_file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(attachment_file.read())
            encoders.encode_base64(attachment)
            attachment.add_header(
                'Content-Disposition',
                f'attachment; filename="{os.path.basename(certificate_path)}"'
            )
            message.attach(attachment)

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            print(f"Email sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")

# Main execution
if __name__ == '__main__':
    email_list = get_email_list('emails.csv')  # CSV file containing 'name,email'
    certificate_folder = 'certificates/'  # Folder containing certificates

    for entry in email_list:
        student_name = entry['name']
        parent_email = entry['email']
        certificate_path = os.path.join(certificate_folder, f"Raport template Ora sfiduese - {student_name} - Web Fundamentals.pdf")
        send_email(parent_email, student_name, certificate_path)
