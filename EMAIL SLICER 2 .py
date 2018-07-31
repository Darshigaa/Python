#Get user email address

email = input("What is your email address?: ").strip()

#Slice out user name

user_name = email[:email.index("@")]

#Slice out domain name

domain_name = email[email.index("@") + 1 :]

#Format message

output = "Your username is {}. Your domain is {}".format(user_name,domain_name)

#Display output message

print(output)

