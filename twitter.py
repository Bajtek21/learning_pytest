
class Twitter():

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) < 160:
            self.tweets.append(message)
        else:
            raise Exception("wiadomość za długa ")