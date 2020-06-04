# EZSheets third-party module, documented at https://ezsheets.readthedocs.io/
# pip install --user ezsheets. 
# EZSheets will also install the google-api-python-client, 
# google-auth-httplib2, and google-auth-oauthlib modules. 
# These modules allow your program to log in to Google’s servers and make API requests. 

# Before you can use EZSheets, you need to enable the Google Sheets 
# and Google Drive APIs for your Google account. 
# Visit the following web pages and click the Enable API buttons at the top of each:
# https://console.developers.google.com/apis/library/sheets.googleapis.com/
# https://console.developers.google.com/apis/library/drive.googleapis.com/

# The following files should be kept in the same folder as the python script
# A credentials file named credentials-sheets.json
# A token for Google Sheets named token-sheets.pickle
# A token for Google Drive named token-drive.pickle

# Go to the Google Sheets Python Quickstart page at 
# https://developers.google.com/sheets/api/quickstart/python/ 
# and click the blue Enable the Google Sheets API button, 

import ezsheets
ss = ezsheets.Spreadsheet('name')