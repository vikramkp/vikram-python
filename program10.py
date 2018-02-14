import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("vikramgowda107@gmail.com", "**********")
msg="HI"
server.sendmail("vikramgowda107@gmail.com", "dixitshetty930@gmail.com", msg)
print("success")
server.quit()
