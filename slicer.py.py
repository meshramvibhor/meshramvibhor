try:
    while(True):
        print("\n*********** Welcome to email Slicer******************")
        userinput = int(input(" press 1 to continue 2 to exit :"))

        if userinput==1:
            # get user email address
            try:

                email = input("What is your email address?: ").strip()
                if email == "@":
                    print("enter valid email address..")


                # slice out user name

                user = email[:email.index("@")]

                # slice domain name

                domain = email[email.index("@") + 1 :]

                # format message

                output = "Your username is {} and your domain name is {}".format(user, domain)

                # display output message 

                print(output)
            except Exception as e:
                print("enter valid email address..")

        if userinput == 2:
            break
except Exception as e:
    print("enter either 1 or 2")