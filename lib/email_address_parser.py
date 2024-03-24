# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, emailString):
        self.emailString = emailString

    def parse(self):

        pattern1 = r',?\s|,'
        regex1 = re.compile(pattern1)
        emailList = regex1.split(self.emailString)
        emailList = [email.strip() for email in emailList if self.is_valid_email(email.strip())]
        emailList.sort()

        return emailList

    def is_valid_email(self,email):
        email_pattern = r'[a-zA-z0-9]+[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-._]'
        return re.match(email_pattern, email)