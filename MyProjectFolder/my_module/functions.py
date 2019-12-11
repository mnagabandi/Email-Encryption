import random 
import smtplib, ssl #this import is only necessary if actually sending email

def encode(mess, key):
    encoded = ''
    for elem in mess:
        x = ord(elem) + key
        encoded += chr(x)
    return encoded
    
def decode(mess, key):
    decoded = ''
    for char in mess:
        x = ord(char) - key
        decoded += chr(x)
    return decoded

def choose(decision, enc_key):
    if decision == '1':
        message = input("Enter a message to encode: ")
        finished = encode(message, enc_key)
    elif decision == '2':
        message = input("Enter a message to decode: ")
        user_key = input("Please enter a key you wish to use: ")
        finished = decode(message, user_key)
    else:
        print('Decision: ' + decision)
        decision = input("Please enter 1 to encode or 2 to decode")
        choice(decision)
    return finished

def randomizer():
    return random.randint(1, 99)
 
def sending_email(mess, key):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "sender_email@gmail.com"  # Enter your address
    receiver_email = "reciever_email@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = mess + "\n\nKey: " + str(key)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
def sending_fake_email(mess, key):
    sender_email = input("Please list the email address you wish to send your message to: ")
    while (not checking_email(sender_email)):
            sender_email = input("Please enter a valid sender email: ")
    print("Message to: " + sender_email + "\n\n" + mess)
    print("\n\nKey: " + str(key)