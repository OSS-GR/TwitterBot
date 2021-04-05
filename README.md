# TwitterBot
A Twitter bot that accesses a CSV file stored in Google Drive using the Google Sheets API.
Thi is a simple Twitter bot that simply posts a text tweet on your Twitter account.
The text is found on your CSV file. It is taken from a cell in the CSV file, posted on the Twitter feed of the account whose credential was used and then deletets the tweet.This way you make sure the same tweet is not resent by accident.

## Installation

To use this code you will need to have the following dependencies installed on your system:
* gspread (You can use 
"
python -m pip install gspread 
" )
* twitter (You can use " python -m pip install python-twitter ")

