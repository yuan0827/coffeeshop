import gspread
from oauth2client.service_account import ServiceAccountCredentials


def gsheet(self, stocks):
    scopes = ["https://spreadsheets.google.com/feeds"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "python-google-sheet-573c80bc154b.json", scopes)

    client = gspread.authorize(credentials)

    sheet = client.open_by_key(
        "1wyPeKo0RB9mCUvopLENWLXbggWCi__8og4dOGkDwBXg").sheet1