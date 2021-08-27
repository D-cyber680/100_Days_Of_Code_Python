import smtplib

my_email = " "
password = "mendez"


connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user = my_email,password=password)
print("success")
connection.sendmail(my_email, to_addrs="coop67077@gmail.com", msg = "Hola que tal")
connection.close()
