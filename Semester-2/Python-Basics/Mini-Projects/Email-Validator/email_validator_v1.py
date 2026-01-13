email=input("Enter your Email: ").strip()

condition=False

while condition==False:
    
    pos=email.find('@')
    service=email[pos:]

    if '@' in email and '.' in email and email.count('@')==1 and service.count('.')==1:
        print("Valid Email: ")
        
        condition=True
    else:
        print("Invalid Email,","enter a valid email")
        email=''
        email=input("Enter your Email: ")
        service=email[pos:]
        condition=False