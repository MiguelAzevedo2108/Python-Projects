import smtplib
import getpass
import imaplib
import email

#send emails with Python
def send_email():

    smtp_object = smtplib.SMTP('smtp.gmail.com',587)

    #estabelish the connection
    smtp_object.ehlo()
    smtp_object.starttls()

    email = getpass.getpass('Email: ')
    password = getpass.getpass('Password: ')

    smtp_object.login(email,password)

    from_address = email
    to_address = email

    subject = input('Enter the subject line:')
    message = input('Enter the body message: ')

    msg = "Subject: " + subject + '\n'+message
    smtp_object.sendmail(from_address,to_address,msg)

    smtp_object.quit()

#receive emails with Python
def receive_message():
    m = imaplib.IMAP4_SSL('imap.gmail.com')
    email = getpass.getpass("email:")
    pw = getpass.getpass('Password:')

    m.login(email,pw)

    m.select('inbox')
    typ,data = m.search(None, 'SUBJECT "NEW TEST PYTHON"')

    id = data[0]

    result, id = m.fetch(id,'(RFC822)')

    #email_Data

    raw_email = data[0][1]

    raw_email_string = raw_email.decode('utf-8')

    message = email.message_from_string(raw_email_string)

    for part in message.walk():
        if part.get_content_type():
            body= part.get_payload(decode=True)
            print(body)


if __name__ == '__main__':
    print('Code begin')
    #print(send_email())
    print(receive_message())
    print("Code finish")
