import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='sender@gmail.com'
	receiver='receiver@gmail.com'
	msg="Hey"
	s.login(sender,'Password')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("Message sent successfully")
	s.quit()	