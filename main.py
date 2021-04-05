import gspread
from twitter import *
from authentication import Authtwit

gc = gspread.service_account('credentials.json')
at = Authtwit
t = Twitter(auth=OAuth(at.get_access_token, at.get_access_token_secret, at.get_api_key, at.get_api_secret))


# Open a sheet from a spreadsheet in one go
wks = gc.open("My News").sheet1

# Upcoming Tweet
nextTweet = wks.acell('A2').value

# Post Tweet
t.statuses.update(status = nextTweet)


# Delete Tweet after posting
wks.delete_rows(2)
