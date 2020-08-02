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

# Sending Mail from a Gmail Account
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')

# adding cc and bcc to messages
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')

# If you need to remember which Gmail address the token.json file 
# is configured for, you can examine ezgmail.EMAIL_ADDRESS. 

ezgmail.init()
ezgmail.EMAIL_ADDRESS

# reading mail from gmail account
unreadThreads = ezgmail.unread() # List of GmailThread objects.
ezgmail.summary(unreadThreads)

len(unreadThreads)

str(unreadThreads[0])
len(unreadThreads[0].messages)

str(unreadThreads[0].messages[0])

unreadThreads[0].messages[0].subject
unreadThreads[0].messages[0].body
unreadThreads[0].messages[0].timestamp
unreadThreads[0].messages[0].sender
unreadThreads[0].messages[0].recipient

# Provider, and SMTP server domain name
# Gmail*     smtp.gmail.com
# Outlook.com/Hotmail.com*    smtp-mail.outlook.com
# Yahoo Mail*   smtp.mail.yahoo.com
# AT&T   smpt.mail.att.net (port 465)
# Comcast  smtp.comcast.net
# Verizon  smtp.verizon.net (port 465)