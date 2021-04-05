#Add your information for your own Twitter Account. You will need a Twitter developer account in order to receive the following keys.
class authtwit:

    def __init__(self):
        self.api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
        self.api_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    def get_api_key(self):
        return self.api_key

    def get_api_secret(self):
        return self.api_secret

    def get_access_token(self):
        return self.access_token

    def get_access_token_secret(self):
        return self.access_token_secret
