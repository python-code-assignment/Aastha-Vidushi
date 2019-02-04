'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
import re
username= raw_input("Enter user name here: ")
password=[]
password=raw_input("Enter a sequence of comma separated passwords here: ").split(",")

x = True
for each in password:
    while x:
        if (len(each)<6 or len(each)>12):
            break
        elif not re.search("[a-z]", each):
            break
        elif not re.search("[0-9]", each):
            break
        elif not re.search("[A-Z]", each):
            break
        elif not re.search("[$#@]", each):
            break
        elif re.search("\s", each):
            break
        else:
            print(each)
        x=False
        break

