# You can find full details on EZGmail at https://github.com/asweigart/ezgmail/. 
# EZGmail is not produced by or affiliated with Google; find the official 
# Gmail API documentation at https://developers.google.com/gmail/api/v1/reference/.

# Before you write code, you must first sign up for a Gmail email account 
# at https://gmail.com/. Then, go to https://developers.google.com/gmail/api/quickstart/python/, 
# click the Enable the Gmail API button on that page, and fill out the form that appears.

# download the credentials.json file
# The folder containing the credentials file must be the current working directory

import ezgmail, os
os.chdir(r'C:\path\to\credentials_json_file')
ezgmail.init()

Sending Mail from a Gmail Account
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')