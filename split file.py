file = input('Type your e-mail address: ')
words = file.split()
email = words[3]
company = email.split('@')
print('the company of your e-mail address is:', company[1])
