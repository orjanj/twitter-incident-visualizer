#!/usr/bin/python
import twitter
from Config import Config # TODO: Make it prettier
from DB import DB # TODO: Make it prettier

class TIVTwitter:
    """ Base class for connecting and fetching data from Twitter API. """

    def __init__(self):
        """ Instance constructor
        :return: none
        """
        config = Config()
        config_param = config.getConfigParameter('twitter')
        self.API = twitter.Api(consumer_key = config_param['consumer_key'],
                      consumer_secret = config_param['consumer_secret'],
                      access_token_key = config_param['access_token_key'],
                      access_token_secret = config_param['access_token_secret'])

    def validateConnection(self):
        """
        Connection validation to Twitter API.
        :return: credential information (json)
        """
        print(self.API.VerifyCredentials())

    def getTweet(self, query_string):
        """ Get Tweet information from Twitter.
        :return: xxx
        :return: xxx
        :return: xxx
        :return: xxx
        :return: xxx
        :return: xxx
        """
        # TODO: Use `python-twitter` for this

    def getTweets(self, query_string):
        """ Get Tweet information from Twitter.
        :return: xxx
        :return: xxx
        :return: xxx
        :return: xxx
        :return: xxx
        :return: xxx
        """
        # TODO: Use `python-twitter` for this

    def getAccountInfo(self, tweet_data):
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

    def insertTweetToDB(self, account_name, hash_tag, tweet_content):
        """ Insertion of tweet(s) to PostgreSQL DB.
        :params: tweet_data (json)
        :return: xxx
        """
        db = DB()
        statement = ''
        db.insertQuery()




# PoC:
#tiv = TIVTwitter()
#tiv.validateConnection()