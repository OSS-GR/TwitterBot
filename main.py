import gspread
from twitter import *
from authentication import *

gc = gspread.service_account('credentials.json')

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))


# Open a sheet from a spreadsheet in one go
wks = gc.open("My News").sheet1

#Upcoming Tweet
nextTweet = wks.acell('A2').value

#Post Tweet
t.statuses.update(status = nextTweet)


#Delete Tweet after posting
wks.delete_rows(2)
