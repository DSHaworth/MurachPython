def main():
    full_name = get_full_name()
    password = get_password()
    email = get_email()
    phone_number = get_phone_number()
    first_name = get_first_name(full_name)   
    print("Hi " + first_name + ", thanks for creating an account.\n" +
          "We'll text your confirmation code to this number: " + phone_number)
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password

def get_email():
    while True:
        email = input("Enter email address:   ").strip()
        atSignPresent = email.find("@") > 0
        endsWithDotCom = email.endswith(".com")
        if atSignPresent == False or endsWithDotCom == False:
            print("Please enter a valid email address")
        else:
            return email

def get_phone_number():
    while True:
        phone_number = input("Please enter a 10-digit phone number:   ")
        # phone_number = phone_number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace(".", "")
        for char in " -().":
            phone_number = phone_number.replace(char, "")
        if len(phone_number) != 10 or phone_number.isdigit() == False:
            print("Please enter a 10-digit phone number.")
        else:
            return phone_number[:3] + "." + phone_number[3:6] + "." + phone_number[6:]

if __name__ == "__main__":
    main()
