from Google import create_service
import pandas as pd

CLIENT_SECRET_FILE = 'credentials.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
GOOGLE_SHEET_ID = '1VUTgYe8TupPQHzzLaJjoZkhZEpXgyG8-yvgEx65cJpE'

def run_batchUpdate_request(service, google_sheet_id, request_body_json):
    try:
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=google_sheet_id,
            body=request_body_json
        ).execute()
        return response
    except Exception as e:
        print(e)
        return None

def get_names():
    service = create_service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

    """
    Iterate Worksheets
    """
    gsheets = service.spreadsheets().get(spreadsheetId=GOOGLE_SHEET_ID).execute()
    sheets = gsheets['sheets']

    for sheet in sheets:
        if sheet['properties']['title'] != 'master':
            dataset = service.spreadsheets().values().get(
                spreadsheetId=GOOGLE_SHEET_ID,
                range=sheet['properties']['title'],
                majorDimension='ROWS'
            ).execute()
            df = pd.DataFrame(dataset['values'], columns=['TimeStamp', 'Name', 'Confirmation', 'Your Handicap'])
            #Removing first row from Df as it is just a column name
            df = df[:: -1]
            names = df['Name'].tolist()
    return names
            
            