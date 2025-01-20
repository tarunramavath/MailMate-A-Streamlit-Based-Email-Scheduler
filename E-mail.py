import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import schedule
import time
import os
import streamlit as st
from datetime import datetime
import threading

# Global flag to track if the email has been sent
email_sent_flag = {}

# Function to validate email
def validate_email(email):
    return email.endswith("@gmail.com")

# Function to send email
def send_email(sender_email, app_password, recipient_email, subject, body, file_path=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Handle file attachment if provided
    if file_path:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                file_attachment = MIMEApplication(f.read(), _subtype=os.path.splitext(file_path)[1][1:])
                file_attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
                msg.attach(file_attachment)
        else:
            st.error(f"File not sent - File does not exist: {file_path}")
            return False

    try:
        # Create server object with SSL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        st.success("Email sent successfully!")
        return True
    except Exception as e:
        st.error(f"Failed to send email. Error: {e}")
        return False

# Function to schedule email
def schedule_email(sender_email, app_password, recipient_email, subject, body, send_time, file_path=None):
    # Task to be executed
    def task():
        current_date = datetime.now().strftime('%Y-%m-%d')
        if email_sent_flag.get(current_date) is None:  # Check if email has already been sent today
            email_sent_flag[current_date] = True
            send_email(sender_email, app_password, recipient_email, subject, body, file_path)
        else:
            print(f"Email for {current_date} has already been sent. Skipping.")

    # Schedule the task
    schedule.every().day.at(send_time).do(task)
    st.success(f"Email scheduled to be sent at {send_time} every day!")

    while True:
        schedule.run_pending()
        time.sleep(1)

# Ensure the temp directory exists
if not os.path.exists("temp"):
    os.makedirs("temp")

# Streamlit UI
st.title("Email Scheduler")

# Input fields
sender_email = st.text_input("Sender Email")
if sender_email and not validate_email(sender_email):
    st.warning("Invalid email! Sender email must end with @gmail.com.")

app_password = st.text_input("App Password", type="password")
recipient_email = st.text_input("Recipient Email")
if recipient_email and not validate_email(recipient_email):
    st.warning("Invalid email! Recipient email must end with @gmail.com.")

subject = st.text_input("Email Subject")
body = st.text_area("Email Body")
file_path = st.file_uploader("Attach a File (optional)", type=None)
send_time = st.text_input("Send Time (HH:MM in 24-hour format)")

# Submit button for sending email immediately
if st.button("Send Email Now"):
    if not all([sender_email, app_password, recipient_email, subject, body]):
        st.error("Please fill in all required fields!")
    elif not validate_email(sender_email) or not validate_email(recipient_email):
        st.warning("Please ensure all email addresses end with @gmail.com.")
    else:
        # Save the uploaded file locally if provided
        if file_path:
            saved_file_path = os.path.join("temp", file_path.name)
            with open(saved_file_path, "wb") as f:
                f.write(file_path.getbuffer())
        else:
            saved_file_path = None

        # Send the email
        send_email(sender_email, app_password, recipient_email, subject, body, saved_file_path)

# Submit button for scheduling email
if st.button("Schedule Email"):
    if not all([sender_email, app_password, recipient_email, subject, body, send_time]):
        st.error("Please fill in all required fields!")
    elif not validate_email(sender_email) or not validate_email(recipient_email):
        st.warning("Please ensure all email addresses end with @gmail.com.")
    else:
        # Validate send_time format
        try:
            datetime.strptime(send_time, "%H:%M")
        except ValueError:
            st.error("Invalid time format! Please use HH:MM in 24-hour format.")
        else:
            # Save the uploaded file locally if provided
            if file_path:
                saved_file_path = os.path.join("temp", file_path.name)
                with open(saved_file_path, "wb") as f:
                    f.write(file_path.getbuffer())
            else:
                saved_file_path = None

            # Start scheduling in a separate thread
            threading.Thread(
                target=schedule_email,
                args=(sender_email, app_password, recipient_email, subject, body, send_time, saved_file_path),
                daemon=True,
            ).start()
