import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("creatibot prompts").sheet1

def saveprompt(arg):
    row = [arg]
    index = 1
    wks.insert_row(row, index)

def getprompt():
    randomuserprompt = ""
    counter = 0
    while counter < wks.row_count:
        if randomuserprompt == "" and wks.col_values(1):
            randomuserprompt = random.choice(wks.col_values(1))
            counter +=1
        if not wks.col_values(1):
            return "Your prompts list is empty!"
        else:
            break
    return randomuserprompt