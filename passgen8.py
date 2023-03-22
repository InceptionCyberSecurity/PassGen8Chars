#!/usr/bin/python
# allowed characters are in chars.txt. Edit as you see fit
import random
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
print("   ")
print(" This Python script will quickly generate an 8 character password using the included chars.txt. ")
print(" The resulting password will be sent to an email of your choice. Make sure your emails are encrypted.")
print("   ")
print(" Specify your Send/Recieve emails in LINES 38 and 39 BEFORE you begin ! ")
print(" Terminate by hitting Ctrl+C or Ctrl+Z if you haven't done this yet. ")
print(" This script will begin automatically ........ ")
print("   ")
time.sleep(25)
# define password set
def generate_password(character_set):
    password = ''
    character_file = open(character_set, 'r+')
    character_array = character_file.readlines()
    len_character_array = len(character_array)
    for i in range(0, 8):
        raw = random.randint(0, len_character_array-1)
        password = str(password) + str(character_array[raw].rstrip('\n'))
    character_file.close()
    return password
# print genetrated password on screen
file_name = "chars.txt"
print(generate_password(file_name))
# save generated password to file pass8.txt
txtFileWriter = open("pass8.txt", "a") # what does the "a" do ?
txtFileWriter.write("password")
txtFileWriter.close()
# send pass8.txt to user defined email
sender_email = "info@arcacdeusops.com" # CHANGE THIS
receiver_email = "nathan.jones@arcadeusops.com" # CHANGE THIS
message = MIMEMultipart()
message["From"] = sender_email
message['To'] = receiver_email
message['Subject'] = "Your Reset Info"
file = "pass8.txt"
attachment = open(file,'rb')
obj = MIMEBase('application','octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition',"attachment; filename= "+file)
message.attach(obj)
my_message = message.as_string()
email_session = smtplib.SMTP('smtp.gmail.com',587)
email_session.starttls()
email_session.login(sender_email,'password')
email_session.sendmail(sender_email,receiver_email,my_message)
email_session.quit()
print("   ")
print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY TO" reciever_email)
