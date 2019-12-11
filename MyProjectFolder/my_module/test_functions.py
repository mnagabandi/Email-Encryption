def checking_message(decision, key, mess):
    if decision == '1':
         test = decode(mess) 
         print(test)
    elif decision == '2':
          test = encode(mess)
          print(test)

def checking_email(email)
    check = 1
    for elem in email:
          if elem == '@':
              check += 1
    if check == 1:
          return True
    else:
          return False
        
def checking_randomizer(key):
    if key < 1 or key > 99:
        return "Invalid randomization."

