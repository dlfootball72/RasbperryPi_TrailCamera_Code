import smtplib
import urllib
import datetime
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage 
addr_to = 'youremail@gmail.com'
addr_from = 'Ender'
smtp_server = 'smtp.gmail.com'
smtp_port   = 587
smtp_user   = 'youremail@gmail.com'
smtp_pass   = 'password'
var=1
while var==1 :
	msg = MIMEMultipart()
	msg['To'] = addr_to
	msg['From'] = 'Ender'
# Open the image files, attach them, and then close the images
	image1 = "image1.jpg"
	image2 = "image2.jpg"
	file1 = open(image1, 'rb')
	file2 = open(image2, 'rb')
	attachment1 = MIMEImage(file1.read())
	attachment2 = MIMEImage(file2.read())
	file1.close()
	file2.close()
	attachment1.add_header('Content-Disposition','attachment',filename=image1)
	attachment2.add_header('Content-Disposition','attachment',filename=image2)
	msg.attach(attachment1)
	msg.attach(attachment2)   
# Send the message via an SMTP server
	s = smtplib.SMTP(smtp_server,smtp_port)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(smtp_user,smtp_pass)
	s.sendmail(addr_from, addr_to.split(","), msg.as_string())
	s.quit()
	
	var = 0
