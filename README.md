# TwitterBot
A Twitter bot that accesses a CSV file stored in Google Drive using the Google Sheets API.  
This simple Twitter bot posts a tweet on your Twitter account.  
The text is found on a CSV file stored in your Google Drive. The text contained in the tweet is taken from a cell in the CSV file, posted on the Twitter feed of your account and then is deleted from the cell. 

I have used the Google Cloud Function to automate this process in order to have a tweet posted daily on my Twitter feed. If you are intrested in finding out more about that I suggest you search it up theres a lot of information on how to use it.

## Installation

To use this code you will need to have the following dependencies installed on your system:
* gspread (You can use 
"
python -m pip install gspread 
" )
* twitter (You can use " python -m pip install python-twitter ")

## License
- Apache 2.0
