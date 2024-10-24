import smtplib

GMAIL_SMTP = 'smtp.gmail.com'
MY_EMAIL = 'smtpyapptest@gmail.com'
PASSWORD = 'xgkqvlapyfnhqowj'
#abcd1234()

connection = smtplib.SMTP(GMAIL_SMTP, 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)
connection.sendmail(from_addr=MY_EMAIL, to_addrs='fernando.aaf@hotmail.com', msg='Hello!')
connection.close()