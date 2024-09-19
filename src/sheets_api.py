"""
CS1 24fa - Assignment 4
Functionality from Google Sheets API to get and update values in a spreadsheet.
Also creates list of dictionaries representing the pendula in the Newton's cradle.
"""

from .constants import *

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = "./config.json"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def get_values(spreadsheet_id, range_names):
    """
    Returns the values of a spreadsheet in a given range.
    
    Args:
      spreadsheet_id (str): the specific id of the spreadsheet (from url)
      range_names (lst[str]): list of strings that have the ranges
      
    Returns:
		  (dict): with the values of the rows, sorted by columns
	  
    Raises:
      HttpError: if there is an error in getting the information
    """
    try:
      service = build('sheets', 'v4', credentials=creds)

      result = service.spreadsheets().values().batchGet(
          spreadsheetId=spreadsheet_id, 
          ranges=range_names
      ).execute()
      return result
    except HttpError as error:
      print(f"An error occurred: {error}")
      return error
  

def update_values(spreadsheet_id, range_name, values):
    """
    Updates the values in the specified spreadsheet in a given range. 

    Args:
      spreadsheet_id (str): the specific id of the spreadsheet (from url)
      range_names (lst): list of strings that have the ranges
      values (lst): list of values that will be added to the range in sheet
        
    Returns:
		  (dict): with the new values of the rows, sorted by columns
	  
    Raises:
      HttpError: if there is an error in getting the information
    """
    try:
      service = build('sheets', 'v4', credentials=creds)
      result = service.spreadsheets().values().batchUpdate(
          spreadsheetId = spreadsheet_id,
          body = {
              "valueInputOption": 'USER_ENTERED',
              "data": [{
                'range': range_name,
                'values': values,
              }]
          }
        ).execute()
      return result
    except HttpError as error:
      print(f"An error occurred: {error}")
      return error

def get_pendulum_info(range, spreadsheet_id):
    """
    Returns a list with all the information from the Google Sheet stored in
    dictionaries for each pendulum. 

    Args:
		  ranges (lst) - list of strings representing ranges per attribute
      spreadsheet_id (str) - unique spreadsheet id of google sheet
    
    Returns:
		  (list[dict]) - list of dictionaries with attributes for each pendulum
              e.g.: [{'masses':1, 'restitution_coeffs':0.1, 'colors':'green', 
                    'textures':'wood'},..., 
                    {'masses':2, 'restitution_coeffs':0.5, 
                    'colors':'blue', 'textures':'earth'}]
    """
    pend_info = []
    
    data = get_values(spreadsheet_id, range)['valueRanges'][0]['values']
    headers = data[0]
    rows = data[1:]

    for row in rows:
       pend_dict = {}
       for j, col_header in enumerate(headers):
          pend_dict[col_header] = row[j]
       pend_info.append(pend_dict)
    
    return pend_info
       


if __name__ == "__main__":
  # testing
    pend_list = get_pendulum_info(RANGE, SPREADSHEET_ID)
    print(pend_list)

    # # You can also update the values in your Google Sheet with code like this!
    # mass_range = "A2:A5"
    # update_values(SPREADSHEET_ID, mass_range, [['1.5'], ['2'], ['1'], ['1.5']])
    # pend_list_new = get_pendulum_info(RANGE, SPREADSHEET)
    # print(pend_list_new)
       
