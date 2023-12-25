import smtplib

smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)
smpt_obj.ehlo()

