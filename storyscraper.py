import twitter

api = twitter.Api(consumer_key='',
            consumer_secret='',
            access_token_key='',
            access_token_secret='')

class Storyscraper:
    def __init__(self, name):
        self.name = name

    def get_user(self):
        self.users = api.GetUsersSearch(term=self.name)
        self.idn = self.users[0].id

    def get_timeline(self):
        outfile = open("highscore.txt", "w")
        tweets = api.GetUserTimeline(user_id = self.idn, count = 200, include_rts = False)
        for tweet in tweets:
            outfile.write(ascii(tweet.text))
            outfile.write("\n")
            last = tweet.id
        x = 20
        y = 0
        while x > y:
            y += 1
            tweets = api.GetUserTimeline(user_id = self.idn, count = 200, include_rts = False, max_id = last)
            for tweet in tweets[0:]:
                outfile.write(ascii(tweet.text))
                outfile.write("\n")
                last = tweet.id
        outfile.close()



def main():
    h = Storyscraper("six word stories")
    h.get_user()
    h.get_timeline()

main()
    
    
