import smtplib


def send_email(from_, from_password, recipient, content):
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()
    mail.login(from_, from_password)

    mail.sendmail(from_, recipient, content)

    mail.close()
