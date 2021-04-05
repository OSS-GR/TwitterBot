import gspread
from twitter import *
from authentication import *

gc = gspread.service_account('credentials.json')

t = Twitter(auth=OAuth(acc_token, acc_token_secret, api_key, api_secret))


# Open a sheet from a spreadsheet in one go
wks = gc.open("My News").sheet1

#Upcoming Tweet 
#Text contained in cell  at "A2"
nextTweet = wks.acell('A2').value

#Post Tweet
t.statuses.update(status = nextTweet)


#Delete Tweet after posting
wks.delete_rows(2)
