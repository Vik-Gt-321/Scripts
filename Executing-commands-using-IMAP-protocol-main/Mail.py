import imaplib
import email
from matplotlib.pyplot import flag
from sympy import content
import yaml
import os

# pass.yml contains your email id and password (created using two step verfication)
with open("/home/vikram/Documents/Scripts/pass.yml") as f:
	content = f.read()

my_cred = yaml.load(content, Loader= yaml.FullLoader)

user, passw = my_cred["user"], my_cred["password"]

imap_url = "imap.gmail.com"

my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(user, passw)

my_mail.select('Inbox')

key = 'FROM'
value = 'vikkymus@gmail.com'

_, data = my_mail.search(None, key, value)

f = open('/home/vikram/Documents/Scripts/pass.py')
print("Opening previous code file")
lines = f.readlines()

last_comm_with_code = lines[-1]
# print(last_comm_with_code)
index = 0
for i in last_comm_with_code:
    if i == '#':
        break
    else:
        index = index+1

last_code = last_comm_with_code[:index]

# print(data[0])
mail_id_list = data[0].split()
# print(mail_id_list)
msgs = []
# for num in mail_id_list:

typ, data = my_mail.fetch(mail_id_list[-1], '(RFC822)')
mail_code = mail_id_list[-1]
print(mail_code, last_code)

# compare the mail ids of previous mail and current mail to know if it is a new mail.
if str(mail_code) == str(last_code):
    print("No new command from gmail")
    exit(0)

msgs.append(data)

for msg in msgs[::-1]:
    for response_part in msg:
        if type(response_part) is tuple:
            my_msg=email.message_from_bytes((response_part[1]))
            if my_msg['subject'] == 'code':
                print("_________________________________________")
                print ("subj:", my_msg['subject'])
                print ("from:", my_msg['from'])
                print ("body:")
                for part in my_msg.walk():  
                    # print("ctype " , part.get_content_type())
                    if part.get_content_type() == 'text/plain':
                        var = part.get_payload()
                        arr = [mail_code, '#', var]
                        s = ''.join(str(x) for x in arr)
                        with open('/home/vikram/Documents/Scripts/pass.py', 'a') as f:
                            f.write(s)

                        import subprocess
                        print('hello: ',var,var[:-2]) # two characters appended to commands-remove them
                        a = subprocess.run(var[:-2],shell=True)
                        print(a)
                        # exit process
                        os.system("xdotool key --clearmodifiers Ctrl+Shift+Q key --clearmodifiers KP_Enter") 


        