
#Calculate the upper and lower case


def str(s):

    upper_case = 0
    lower_case = 0
    for i in s:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        else:
            pass 
          
    print("no of upper case characters:", upper_case)
    print("no of lower case characters:", lower_case)
str(input("Enter the sample string:"))     


