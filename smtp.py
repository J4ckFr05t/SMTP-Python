import sys
import smtplib
import getpass	                #for hiding password input
from termcolor import colored   #for highlighting

HOST = "smtp.gmail.com" 
PORT = 465

smtp_client = smtplib.SMTP_SSL(HOST,PORT)

TO = input("\nEnter reciever email: ")

FROM = "yourmail@gmail.com"
secret = getpass.getpass(prompt="Password for {}:".format(FROM))

try:
	smtp_client.login(FROM, secret)
except Exception as e:
	print(colored("Unable to Login. Incorrect email/password.",'yellow'))
	sys.exit()

header = "To\t:\t{}\nFrom\t:\t{}\n".format(TO,FROM)

subj = input("\nEnter Subject: ")
body = input("Enter Body: ")
subject = "Subject\t:\t{}".format(subj)
signature = "\n\nJibin George\nCSEA\nRoll No. 63"
message =  header + subject +"\n\n"+body+signature

print(colored("\nTo\t:\t",'green'),end="")
print(colored(TO,'white'))
print(colored("From\t:\t",'green'),end="")
print(colored(FROM,'white'))
print(colored("Subject\t:\t",'green'),end="")
print(colored(subj,'white'))
print(colored("\n"+body+signature,'white'))


while True:
	confirmation = input("\nDo you want to send the mail (y/n): ")
	if (confirmation == "y") or (confirmation == "Y"):
		try:
			smtp_client.sendmail(FROM,TO,message)
			print(colored("Email has been sent.",'yellow'))
			break
		except Exception as e:
			print(colored("Unable to send mail. Check To address",'yellow'))
			break
	elif (confirmation == "n") or (confirmation == "N"):
		print(colored("Cancelled Email from being send.",'green'))
		break
	elif confirmation == "":
		continue
	else:
		continue
