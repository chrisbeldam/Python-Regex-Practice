import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

emailAddresses = re.search(r'(?P<email>\w+-?\.?\w+\@\w+\.\w+)', emails) # Gets the first two emails
print(emailAddresses.groupdict())
