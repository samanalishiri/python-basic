import re

email_pattern = re.compile('[\w.\-_]+@\w+\.\w+')
email_fullmatch_pattern = re.compile('[\w.\-_]+@\w+\.\w{2,3}')
with open('emailsample.txt') as file:
    [print(email) for email in email_pattern.findall(file.read()) if email_fullmatch_pattern.fullmatch(email)]
