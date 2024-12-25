# Email Sender Script

This repository contains a Python script designed to automate sending emails with personalized attachments. It was developed to help streamline communication, such as sending progress reports to students' parents.

## Features

- Send emails in bulk using a CSV file containing recipient information.
- Attach personalized PDF files to each email.
- Automatically logs issues like missing files or failed email deliveries.
- CC additional recipients on every email.

---

## Prerequisites

### 1. Python Installation
Make sure Python 3.7 or higher is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### 2. Required Libraries
Install the following Python libraries using pip:

```bash
pip install -r requirements.txt
```

**Required libraries:**
- smtplib (built-in)
- email (built-in)
- csv (built-in)
- os (built-in)
- dotenv (to manage environment variables)

### 3. Email Configuration
The script uses environment variables to store sensitive information like your email address and password. Create a `.env` file in the root of your project with the following content:

```
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

> **Note:** Replace `your_email@example.com` and `your_app_password` with your actual credentials. Use [App Passwords](https://support.google.com/accounts/answer/185833) if using Gmail.

---

## File Structure

```
email_sender_script/
├── emails.csv          # Contains recipient names and emails
├── certificates/       # Directory for PDF attachments
├── .env                # Environment variables
├── app.py           # Main Python script
├── README.md           # Documentation
└── requirements.txt    # List of Python dependencies
```

---

## Usage

### Step 1: Prepare the Email List
Create a `emails.csv` file with the following structure:

| name         | email              |
|--------------|--------------------|
| Filan Fisteku   | filan@example.com   |
| Filan Fisteku  | fistkeu@example.com    |

### Step 2: Add Attachments
Place all personalized PDF attachments in the `certificates/` folder. Name them using the format:

```
Raport template Ora sfiduese - [Student Name] - Web Fundamentals.pdf
```

Example:
```
Raport template Ora sfiduese - Filan Fisteku - Web Fundamentals.pdf
```

### Step 3: Run the Script
Execute the script using the following command:

```bash
python app.py
```

The script will:
1. Read the `emails.csv` file to get recipient details.
2. Search for the corresponding PDF in the `certificates/` folder.
3. Send an email to each recipient with the PDF as an attachment.

---

## Error Handling

- **Missing Attachments:**
  If the script cannot find a PDF file for a recipient, it will skip sending the email and log the issue.

- **Failed Deliveries:**
  If an email fails to send, the error message will be displayed in the console.

---

## Contributing
Contributions are welcome! If you have suggestions or want to improve the script, feel free to submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
