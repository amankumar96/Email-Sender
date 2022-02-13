import smtplib
from email.message import EmailMessage
from  string import  Template
from pathlib import  Path

html = Template(Path('index.xhtml').read_text())
email = EmailMessage()
email['from'] = ' Dummy'
email['to'] = 'amank1996@gmail.com'
email['subject'] = 'Hi!!!!! boy '

email.set_content(html.substitute({'name': 'Aman'}), ' html' )

with smtplib.SMTP(host= 'smtp.gmail.com', port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('messegedummy123@gmail.com', 'dummy1996')
    smtp.send_message(email)
    print('all done')
