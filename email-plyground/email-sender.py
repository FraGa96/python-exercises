import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Me'
email['to'] = 'destinymail'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('Learning Python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('originmail', 'password')
    smtp.send_message(email)