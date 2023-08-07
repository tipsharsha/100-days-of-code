"""sending emails"""
import smtplib


my_email = "maybenewemail@gmail.com"
to_email = "maybedisposable@outlook.com"


connect = smtplib.SMTP("smtp.outlook.com")
connect.starttls()
connect.login(user =to_email,password="t!p$harsha")
connect.sendmail(from_addr=to_email,to_addrs=my_email,msg="hello")
connect.close()

