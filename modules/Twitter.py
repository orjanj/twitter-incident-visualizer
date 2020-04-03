#!/usr/bin/python
import twitter

class TIVTwitter:
    """ Base class for connecting and fetching data from Twitter API. """

    def __init__(self, config, db, gmaps):
        """ Instance constructor
        :return: none
        """
        self.db = db
        self.gmaps = gmaps
        self.config_param = config.getConfigParameter('twitter')
        self.API = twitter.Api(consumer_key = self.config_param['consumer_key'],
                      consumer_secret = self.config_param['consumer_secret'],
                      access_token_key = self.config_param['access_token_key'],
                      access_token_secret = self.config_param['access_token_secret'])

        # Set up a blacklist (Norwegian word list)
        self.blacklist = []
        self.buildWordBlacklist()

    def validateConnection(self):
        """
        Connection validation to Twitter API.
        :return: credential information (json)
        """
        print(self.API.VerifyCredentials())

    def getTweets(self, screen_name, tweet_count):
        """ Get Tweet information from Twitter.
        :param screen_name: twitter username (string)
        :param tweet_count: count of tweets to fetch (int)
        :return user_timeline: list of tweets (string)
        """
        user_timeline = self.API.GetUserTimeline(screen_name=screen_name, count=tweet_count)
        return(user_timeline)

    def detectLocation(self, tweet_string):
        """ Detect upper case in words and return the words.
        :params tweet_string: tweet text (string)
        :return words: upper case words (list)
        """
        location_list = []
        for word in tweet_string.split():
            if word[0].isupper() and (word.lower() not in self.blacklist): # TODO: BUG
                location_list.append(word)
            if word.startswith('v/') and word[2].isupper() and (word[2:].lower() not in self.blacklist): # Example string: v/Bodø
                location_list.append(word[2:])

        return(location_list)

    def buildWordBlacklist(self, filename='config/wordlist_20190123_norsk_ordbank_nob_2005.txt'):
        """ Build an word list for blacklisting ordinary Norwegian words to better figure out exact location names. """
        with open(filename, "r") as wordlist_file:
            self.blacklist = [line.rstrip('\n') for line in wordlist_file]

    def getProjectFollowers(self, follower_count):
        """ Get our projects followers from Twitter."""
        project_friendslist = self.API.GetFriends(count=follower_count)
        return(project_friendslist)

    def getAccountInfo(self, screen_name):
        """ Get Twitter account information.
        :param: tweet_data (json)
        :return: account_name
        :return: account_url
        :return: account_text
        :return: account_reg_date
        :return: account_webpage
        :return: account_pic_url
        :return: account_verified
        """
        user_info = self.API.GetUser(screen_name=screen_name)
        return(user_info)

    def insertAccountToDB(self, account_object=None):
        """ Insertion of account(s) to PostgreSQL DB.
        :params account_object: twitter.models.User (class/object)
        :return: message success/unsuccess
        """
        # Build the Twitter profile URL for the account
        account_twitter_url = 'https://twitter.com/' + account_object.screen_name

        # Make query ready for insertion
        query = "INSERT INTO account(account_name, account_url, account_text, account_reg_date, account_webpage, account_pic_url, account_location, account_screen_name) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (account_object.name, account_twitter_url, account_object.description, account_object.created_at, account_object.url, account_object.profile_image_url_https, account_object.location, account_object.screen_name)

        # Insert all the values to the database
        rows = self.db.execute(query, values)
        if rows > 0:
            print(rows, "row(s) changed in database.")

    def insertTweetsToDB(self, account_id, tweet_place, lat, lng, tweet_objects=None):
        """ Insertion of tweets to PostgreSQL DB.
        :params: tweet_objects (json)
        :return: message success/unsuccess
        """
        # Make query ready for insertion
        query = "INSERT INTO tweets(account_id, tweet_time, tweet_content, tweet_place, tweet_hashtags, tweet_lat, tweet_long) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values = (account_id, tweet_objects.created_at.strip(), tweet_objects.text.strip(), tweet_place.strip(), tweet_place.strip(), lat, lng)

        # Insert all the values to the database
        rows = self.db.execute(query, values)
        if rows > 0:
            print(rows, "row(s) changed in database.")