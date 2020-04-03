#!/usr/bin/python3
#import datetime
from modules.Config import Config # TODO: Make it prettier
from modules.DB import DB # TODO: Make it prettier
from modules.Twitter import TIVTwitter # TODO: Make it prettier
from modules.File import File
from modules.Gmaps import Gmaps

# Start of our mining application
if __name__ == '__main__':

    # Create instances
    config = Config()
    db = DB(config)
    gmaps = Gmaps(config)
    tiv = TIVTwitter(config, db, gmaps)

    # Get config parameters for the mining script
    mine_cfg = config.getConfigParameter('twitter-mine')
    gmaps_cfg = config.getConfigParameter('gmaps')

    # Get followers
    if mine_cfg['mine_followers'] == True:

        # Get value for number of followers
        followers = tiv.getProjectFollowers(mine_cfg['mine_number_of_followers'])

        # Go through all the followers
        for user in followers:

            # Get account information for the user
            account_data = tiv.getAccountInfo(user.screen_name)

            # Insert the account data into the database
            tiv.insertAccountToDB(account_data)

    # Get tweets from Twitter
    if mine_cfg['mine_tweets'] == True:

        # Get account screen names
        result = db.execute("SELECT account_screen_name, account_id FROM account ORDER BY account_screen_name DESC")

        # And let's go through all users tweets
        for row in result:

            # Get tweets for each user
            account_screen_name = row[0]
            account_id = row[1]
            users_tweets_data = tiv.getTweets(account_screen_name, mine_cfg['mine_tweet_count'])

            # Go through Tweets for each user
            for u in users_tweets_data:

                # Create a hash tag list
                hash_list = []

                # Check if there is any hashtags
                if len(u.hashtags) > 0:
                    hsh = ''

                    # Create an comma separated hash variable
                    for tag in u.hashtags:
                        if len(hsh) > 0:
                            hsh += ', '
                        hsh += tag.text

                # Check if the hash variable contains data, and get lat/long
                if len(hsh) > 0:
                    google_location = gmaps.lookUpLocation(hsh)
                    if not google_location == None:
                        longitude = google_location['lng']
                        latitude = google_location['lat']

                # Insert record data to database
                tiv.insertTweetsToDB(account_id, hsh, latitude, longitude, u)