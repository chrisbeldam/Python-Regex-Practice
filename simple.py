import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

names = re.search(r'(?P<formal>Mr?s?\s?\.?\s\w+)',text_to_search) #returns all the names
print(names.groups())

numbers = re.search(r'(?P<phone>\d{3}-?\.?\*?\d{3}-?\.?\*?\d{4})', text_to_search)
print(numbers.groups())


sentence = 'Start a sentence and then bring it to an end'

m = re.match(r'Start', sentence) # Searches for the word Start in the sentence variable
print(m.group(0))
# m2 = re.search(r'Start\s\w\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+',sentence)
# print(m2.group(0))
