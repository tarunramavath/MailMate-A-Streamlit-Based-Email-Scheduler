# MailMate-A-Streamlit-Based-Email-Scheduler

A **Streamlit-based application** for sending and scheduling emails. The application supports file attachments and email validation, providing a simple and user-friendly interface.

---

## 📋 Features

- **Send Emails Instantly**: Quickly send emails with just a few clicks.
- **Schedule Emails**: Set a daily schedule to send emails automatically at a specific time.
- **File Attachments**: Attach files to your emails easily.
- **Email Validation**: Ensures sender and recipient email addresses are valid Gmail accounts.
- **Interactive UI**: Built using Streamlit for an intuitive user experience.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-scheduler.git
   cd email-scheduler
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
streamlit run app.py
🚀 Usage
Open the application in your web browser (usually at http://localhost:8501).
Fill out the required fields:
Sender Email: Enter your Gmail address.
App Password: Provide the app password for your Gmail account.
Recipient Email: Enter the recipient's Gmail address.
Email Subject: Type the subject of your email.
Email Body: Compose the message you want to send.
Attach a File (optional): Upload a file to include in your email.
Send Time (optional): Set a daily schedule in HH:MM format (24-hour clock).
Click:
"Send Email Now": Send the email immediately.
"Schedule Email": Schedule the email to be sent daily at the specified time.
📦 Requirements
Python 3.7 or higher
Gmail Account with App Password: Learn how to create an app password here.
📂 Project Structure
plaintext
Copy
Edit
email-scheduler/
├── temp/                  # Temporary directory for uploaded files
├── app.py                 # Main application code
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
🔒 Security Note
Avoid hardcoding sensitive information like Gmail passwords in the code.
Use environment variables or secure storage solutions to manage credentials.
🤝 Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or new features.
