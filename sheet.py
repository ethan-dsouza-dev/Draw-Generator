from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'service-account.json'

# The scopes required for the Google Sheets and Drive API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# The ID of the spreadsheet
SPREADSHEET_ID = '1VUTgYe8TupPQHzzLaJjoZkhZEpXgyG8-yvgEx65cJpE'

def get_names():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Build the service object
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Form Responses 1!A2:D").execute()
    values = result.get('values')
    
    if not values:
        print('No data found.')
        return []
    else:
        df = pd.DataFrame(values, columns=['TimeStamp', 'Name', 'Confirmation', 'Your Handicap'])
        # print(df)
        #Removing first row from Df as it is just a column name
        df = df[:: -1]
        names = df['Name'].tolist()
        # print(names)
        return names
