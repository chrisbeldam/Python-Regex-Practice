import re

testText = """
    111-223-4466
    123.859-9876
    876-987*3456


    chris:beldam
    john smith
    martyn watson



"""

phoneNumber = re.search(r'(?P<phone>\d{3}-?\.?\d{3}-?\*?\d{4})',testText)
print(phoneNumber.groupdict())
