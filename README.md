# MailMate A Streamlit-Based Email Scheduler

An easy-to-use application that allows users to schedule emails to be sent at specific times. This tool is designed for both personal and professional use, making email management more efficient and timely.

## Features

- Schedule emails to be sent at a future date and time.
- Support for multiple email recipients.
- Integration with popular email services like Gmail, Outlook, etc.
- Save drafts of scheduled emails.
- Notifications for successful email delivery or errors.
- Support for attachments.
- Simple and intuitive user interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/email-scheduler.git
    cd email-scheduler
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:  
   Create a `.env` file in the project root and add the following:
    ```env
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_USER=your-email@example.com
    EMAIL_PASSWORD=your-password
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Open the application.
2. Log in with your email credentials.
3. Compose an email:
   - Enter the recipient(s).
   - Add a subject and body.
   - Attach files if necessary.
4. Set the desired date and time for the email to be sent.
5. Click "Schedule."

The application will send the email at the specified time.

## Configuration

- **Email Service Providers**: Configure the `EMAIL_HOST` and `EMAIL_PORT` in the `.env` file for your preferred email provider.
- **Time Zone**: Update the application's time zone in `settings.py` if needed.

## Requirements

- Python 3.8 or higher
- Flask (for web-based interface)
- smtplib or an equivalent library for sending emails
- A database for storing scheduled emails (SQLite, PostgreSQL, or others)

## Contribution

We welcome contributions!
