import time
import smtplib
TO = 'matthewzourelias@gmail.com'
GMAIL_USER = 'matthewzourelias@gmail.com'
GMAIL_PASS = 'mrcz031808161988'
SUBJECT = 'Intrusion!!'
TEXT = 'Your PIR sensor detected movement'
def send_email():
	print("Sending Email")
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(GMAIL_USER, GMAIL_PASS)
	header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
	header = header + '\n' + 'Subject:' + SUBJECT + '\n'
	print header
	msg = header + '\n' + TEXT + ' \n\n'
	smtpserver.sendmail(GMAIL_USER, TO, msg)
	smtpserver.close()
	
count = 0
while (count < 2 ):
	print 'The count is:', count
	send_email()
	count = count + 1
print "Good bye!"