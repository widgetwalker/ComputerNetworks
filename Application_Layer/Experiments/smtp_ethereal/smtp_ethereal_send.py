import smtplib

# Ethereal SMTP settings
smtp_server = "smtp.ethereal.email"
port = 587

# User input
sender_email = input("Enter your Ethereal email address: ")
password = input("Enter your Ethereal password: ")
receiver_email = input("Enter recipient email address: ")
subject = input("Enter subject: ")
body = input("Enter message body: ")

# Compose the email
message = f"Subject: {subject}\n\n{body}"

# Send the email
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")