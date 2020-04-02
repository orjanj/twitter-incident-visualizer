#!/usr/bin/python
import twitter
import json
import sys
import re

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
#        example_data = "[Status(ID=1245681033124683782, ScreenName=politinordland, Created=Thu Apr 02 11:54:36 +0000 2020, Text='Førerkortet til mistenkte er midlertidig tatt i beslag. https://t.co/BCEykXoMS3'), Status(ID=1245680172155711490, ScreenName=politinordland, Created=Thu Apr 02 11:51:11 +0000 2020, Text='#Sortland FV820 v/Sandstrand: @Utrykningspol har gjennomført laserkontroll på stedet. 4 ff. Høyeste hastighet var 75 km/t i 60 sone.'), Status(ID=1245675059643142146, ScreenName=politinordland, Created=Thu Apr 02 11:30:52 +0000 2020, Text='#Bodø: Mann i midten av 20 årene mistenkt for ruspåvirket kjøring. Stanset av @Utrykningspol . Fremstilles for bevissikring.'), Status(ID=1245639331223486476, ScreenName=politinordland, Created=Thu Apr 02 09:08:54 +0000 2020, Text='#Ballstad: patr har stanset mannlig bilfører som ikke har gyldig førerkort. Blir anmeldt.'), Status(ID=1245637948042698754, ScreenName=politinordland, Created=Thu Apr 02 09:03:24 +0000 2020, Text='Rettelse: Hendelsen har ikke skjedd i et fotgjengerfelt, men idet fotgjenger skulle krysse veien. Vi er i kontakt m… https://t.co/mHBZVpKhBb'), Status(ID=1245625369475964932, ScreenName=politinordland, Created=Thu Apr 02 08:13:25 +0000 2020, Text='#Narvik, Fagernes: fotgjenger truffet av sidespeilet til bil idet denne passerte, skal ha skjedd i fotgjengerfelt.… https://t.co/KRi7TQerGZ'), Status(ID=1245566502113345536, ScreenName=politinordland, Created=Thu Apr 02 04:19:30 +0000 2020, Text='#Sortland. kl 0230 stopper patruljen en bil med 4 stk i. Fører har ikke gyldig førerkort og det blir gjort beslag a… https://t.co/Uo0OYMGxCU'), Status(ID=1245448350494752769, ScreenName=politinordland, Created=Wed Apr 01 20:30:00 +0000 2020, Text='Politiet har gjort undersøkelser på stedet. Bilfører avhørt. Førerkort beslaglegges, sak opprettes. https://t.co/MN0HNld47M'), Status(ID=1245438413433704449, ScreenName=politinordland, Created=Wed Apr 01 19:50:31 +0000 2020, Text='#Leknes: Ambulanse og politi har rykket ut til privatadresse etter melding om at en person er påkjørt i en oppkjørs… https://t.co/418nQyia9r'), Status(ID=1245419026848907266, ScreenName=politinordland, Created=Wed Apr 01 18:33:29 +0000 2020, Text='#Sulitjelma: Statens Naturoppsyn og politiet har gjennomført en snøscooterkontroll. 16 kontrollerte, ingen anmeldelser.'), Status(ID=1245397387776077824, ScreenName=politinordland, Created=Wed Apr 01 17:07:30 +0000 2020, Text='Vi mistenker at uhellet skyldes uaktsom kjøring. Førerkort beslaglegges, sak opprettes. https://t.co/oMaPYZFTuz'), Status(ID=1245391960086663168, ScreenName=politinordland, Created=Wed Apr 01 16:45:56 +0000 2020, Text='#Narvik: Trafikkuhell i Kongens gate. Bil kjørt inn i en snøhaug. Ikke personskade. Vi er på stedet og snakker med fører.'), Status(ID=1245380601588387844, ScreenName=politinordland, Created=Wed Apr 01 16:00:48 +0000 2020, Text='#Stokmarknes: Trafikkuhell på FV 82. Kollisjon mellom to personbiler etter at den ene parten har brutt vikeplikten.… https://t.co/VyZhdJl2p8'), Status(ID=1245369687623548930, ScreenName=politinordland, Created=Wed Apr 01 15:17:26 +0000 2020, Text='#Bodø: Bilfører stanset av UP, mistanke om ruspåvirket kjøring. Bevissikring utført, førerkort beslaglagt.'), Status(ID=1245369165696860163, ScreenName=politinordland, Created=Wed Apr 01 15:15:21 +0000 2020, Text='#Grane #E6: Politiet har gjennomført fartskontroll (gjennomsnitt). Medførte to forenklede forelegg, 108 km/t i 80-s… https://t.co/AkZaalG5X5'), Status(ID=1245341162715652096, ScreenName=politinordland, Created=Wed Apr 01 13:24:05 +0000 2020, Text='#Bodø: UP ar gjennomført fartskontroll i Bodøtunnelen. Seks bilførere gitt forenklet forelegg, høyeste hastighet var 107 km/t i 80-sone.'), Status(ID=1245340307539005441, ScreenName=politinordland, Created=Wed Apr 01 13:20:41 +0000 2020, Text='#Bodø: Bilfører stanset av UP i kontroll. Mistanke om ruspåvirket kjøring. Bevissikring utført. Førerkort beslaglagt.'), Status(ID=1245336717105774597, ScreenName=politinordland, Created=Wed Apr 01 13:06:25 +0000 2020, Text='#Sortland: Bilfører stanset for kontroll. Anmeldes for kjøring uten gyldig førerkort.'), Status(ID=1245328619670560768, ScreenName=politinordland, Created=Wed Apr 01 12:34:14 +0000 2020, Text='#Narvik: UP har avholdt laserkontroll i Bjerkvik. 20 førere fikk forenklede forelegg. Høyeste hastighet var på 74 k… https://t.co/SBoXblz4zx'), Status(ID=1245317949340205056, ScreenName=politinordland, Created=Wed Apr 01 11:51:50 +0000 2020, Text='#Øksnes: UP har avholdt laserkontroll på Nergard. 5 førere fikk forenklede forelegg. Høyeste hastighet var på 72 km/t. 60 km/t på stedet.')]"
#        return(example_data)

    def detectLocation(self, tweet_string):
        """ Detect upper case in words and return the words.
        :params tweet_string: tweet text (string)
        :return words: upper case words (list)
        """
        location_list = []
        for word in tweet_string.split():
            if word[0].isupper() and (word.lower() not in self.blacklist):
                location_list.append(word)
            if word.startswith('v/') and word[2].isupper() and (word[2:].lower() not in self.blacklist): # Example string: v/Bodø
                location_list.append(word[2:])

        return(location_list)

    def buildWordBlacklist(self, filename='config/wordlist_20190123_norsk_ordbank_nob_2005.txt'):
        with open(filename, "r") as wordlist_file:
            for line in wordlist_file.readlines():
                self.blacklist.append(line)

    def getProjectFollowers(self, follower_count):
        """ Get our projects followers from Twitter.
        """
        project_friendslist = self.API.GetFriends(count=follower_count)
        return(project_friendslist)
#        example_data = '[User(ID=839082941036789760, ScreenName=politietost), User(ID=437997027, ScreenName=PolitiTrondelag), User(ID=1251538416, ScreenName=PolitiMRpd), User(ID=3389005078, ScreenName=110Finnmark), User(ID=382593384, ScreenName=Utrykningspol), User(ID=560997111, ScreenName=110Agder), User(ID=480253925, ScreenName=Oslo110sentral), User(ID=2507231689, ScreenName=110Bodo), User(ID=1047599642, ScreenName=politifinnmark), User(ID=1479532554, ScreenName=politiagder), User(ID=381502681, ScreenName=oslopolitiops), User(ID=1374416472, ScreenName=polititroms), User(ID=2251977161, ScreenName=politinordland)]'
#        return(example_data)

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
#        print(user_info.created_at)
#        example_data = '{"created_at": "Mon Dec 30 12:44:42 +0000 2013","description": "Operasjonssentralen i Nordland informerer om hendelser i distriktet. Vi svarer ikke p\u00e5 twitter, bruk heller v\u00e5r tlf 02800/75589000. Ved N\u00f8d ring 112","favourites_count": 20,"followers_count": 23587,"following": true,"friends_count": 7,"id": 2251977161,"id_str": "2251977161","listed_count": 173,"location": "Bod\u00f8","name": "Politiet i Nordland","profile_background_color": "C0DEED","profile_background_image_url":"http://abs.twimg.com/images/themes/theme1/bg.png","profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png","profile_image_url": "http://pbs.twimg.com/profile_images/417638849137741824/aHsYdiix_normal.jpeg","profile_image_url_https": "https://pbs.twimg.com/profile_images/417638849137741824/aHsYdiix_normal.jpeg","profile_link_color": "0084B4","profile_sidebar_border_color": "FFFFFF","profile_sidebar_fill_color": "DDEEF6","profile_text_color": "333333","profile_use_background_image": true,"screen_name": "politinordland","status": {"created_at":"Thu Apr 02 11:54:36 +0000 2020","favorite_count": 1,"hashtags": [],"id": 1245681033124683782,"id_str": "1245681033124683782","lang": "no","quoted_status_id": 1245675059643142146,"quoted_status_id_str": "1245675059643142146","retweet_count": 1,"source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>","text": "F\u00f8rerkortet til mistenkte er midlertidig tatt i beslag. https://t.co/BCEykXoMS3","urls": [{"expanded_url": "https://twitter.com/politinordland/status/1245675059643142146","url": "https://t.co/BCEykXoMS3"}],"user_mentions": []},"statuses_count": 21769,"url": "https://t.co/xyJnJUHaqs"}'
#        return(example_data)

    def insertAccountToDB(self, account_object=None):
        """ Insertion of account(s) to PostgreSQL DB.
        :params account_object: twitter.models.User (class/object)
        :return: message success/unsuccess
        """
        # Check if the given input string is longer than 0
        if len(account_object) > 0:

            # Build the Twitter profile URL for the account
            account_twitter_url = 'https://twitter.com/' + account_object.screen_name

            # Insert all the values to the database
            query = "INSERT INTO account(account_name, account_url, account_text, account_reg_date, account_webpage, account_pic_url, account_location, account_screen_name) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (account_object.name, account_twitter_url, account_object.description, account_object.created_at, account_object.url, account_object.profile_image_url_https, account_object.location, account_object.screen_name)
            self.db.execute(query, values)
        else:
            print("Error: Seems like the input is empty.. Touchè.")

    def insertTweetsToDB(self, tweet_objects=None):
        """ Insertion of tweets to PostgreSQL DB.
        :params: tweet_objects (json)
        :return: xxx
        """
        # Find account_id for given screen_name
        hash_tag = ''
        latlng = ''
        for obj in tweet_objects:
            for htag in obj.hashtags:
                hash_tag = htag.text

            if len(hash_tag) > 0:
                location_name = hash_tag
                latlng = self.gmaps.lookUpLocation(location_name)

            print(latlng)
            print("\n")
            print(hash_tag)

            print(self.detectUppercase(obj.text))
            print(obj.text)
#            print(obj.user)

            # Insert all the values to the database
#            query = "INSERT INTO tweet"
#            query = "INSERT INTO account(account_name, account_url, account_text, account_reg_date, account_webpage, account_pic_url, account_location, account_screen_name) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
#            values = (account_object.name, account_twitter_url, account_object.description, account_object.created_at, account_object.url, account_object.profile_image_url_https, account_object.location, account_object.screen_name)
#            self.db.execute(query, values)





#followers = tiv.getProjectFollowers(3)
##print([u.screen_name for u in followers])
#for u in followers:
#    account_data = tiv.getAccountInfo(u.screen_name)
#    tiv.insertAccountToDB(account_data)
            # TODO: Add UNIQUE (constraint?) for geo_name, geo_lat and geo_long in one index?
#            geo_query = "INSERT INTO geo(geo_name, geo_lat, geo_long) VALUES(%s, %s, %s)"
#            geo_values = (location_name, tweet_lat, tweet_long)
#            db.execute(geo_query, geo_values)
#            # TODO: Find `geo_id`from DB and use it in next query
#            geo_id = ''


#for u in tweets:
#    print(u.user_mentions)
#    print(u.created_at)
#    print(u.favorite_count)
#    print(u.hashtags)
#    print(u.id)
#    print(u.id_str)
#    print(u.lang)
#    print(u.retweet_count)
#    print(u.source)
#    print(u.text)
#    print(u.truncated)
#    print(u.urls)
#    print(u.user)

#    tweet_text = u.text
#    # Detect words starting with upper case
#    for word in tweet_text.split():
#        if re.match(r"[A-Z]+", word):
#            print(word)
#
##    print("Hashtag:", u.hashtags)
#    for htag in u.hashtags:
#        hash_tag = htag.text
##        print(htag.text)
#    print("-------------------------------")




#        db_query = db.execute("SELECT account_id FROM account WHERE account_screen_name = '" + screen_name + "'")
#        for result in db_query:
#            account_id = result[0]






#        query = "INSERT INTO tweets(account_id, tweet_time, tweet_content, tweet_place, geo_id, tweet_hashtags) VALUES(%s, %s, %s, %s, %s, %s)"
#        values = (tweet_objects.)

#        example_data = "[Status(ID=1245681033124683782, ScreenName=politinordland, Created=Thu Apr 02 11:54:36 +0000 2020, Text='Førerkortet til mistenkte er midlertidig tatt i beslag. https://t.co/BCEykXoMS3'), Status(ID=1245680172155711490, ScreenName=politinordland, Created=Thu Apr 02 11:51:11 +0000 2020, Text='#Sortland FV820 v/Sandstrand: @Utrykningspol har gjennomført laserkontroll på stedet. 4 ff. Høyeste hastighet var 75 km/t i 60 sone.'), Status(ID=1245675059643142146, ScreenName=politinordland, Created=Thu Apr 02 11:30:52 +0000 2020, Text='#Bodø: Mann i midten av 20 årene mistenkt for ruspåvirket kjøring. Stanset av @Utrykningspol . Fremstilles for bevissikring.'), Status(ID=1245639331223486476, ScreenName=politinordland, Created=Thu Apr 02 09:08:54 +0000 2020, Text='#Ballstad: patr har stanset mannlig bilfører som ikke har gyldig førerkort. Blir anmeldt.'), Status(ID=1245637948042698754, ScreenName=politinordland, Created=Thu Apr 02 09:03:24 +0000 2020, Text='Rettelse: Hendelsen har ikke skjedd i et fotgjengerfelt, men idet fotgjenger skulle krysse veien. Vi er i kontakt m… https://t.co/mHBZVpKhBb'), Status(ID=1245625369475964932, ScreenName=politinordland, Created=Thu Apr 02 08:13:25 +0000 2020, Text='#Narvik, Fagernes: fotgjenger truffet av sidespeilet til bil idet denne passerte, skal ha skjedd i fotgjengerfelt.… https://t.co/KRi7TQerGZ'), Status(ID=1245566502113345536, ScreenName=politinordland, Created=Thu Apr 02 04:19:30 +0000 2020, Text='#Sortland. kl 0230 stopper patruljen en bil med 4 stk i. Fører har ikke gyldig førerkort og det blir gjort beslag a… https://t.co/Uo0OYMGxCU'), Status(ID=1245448350494752769, ScreenName=politinordland, Created=Wed Apr 01 20:30:00 +0000 2020, Text='Politiet har gjort undersøkelser på stedet. Bilfører avhørt. Førerkort beslaglegges, sak opprettes. https://t.co/MN0HNld47M'), Status(ID=1245438413433704449, ScreenName=politinordland, Created=Wed Apr 01 19:50:31 +0000 2020, Text='#Leknes: Ambulanse og politi har rykket ut til privatadresse etter melding om at en person er påkjørt i en oppkjørs… https://t.co/418nQyia9r'), Status(ID=1245419026848907266, ScreenName=politinordland, Created=Wed Apr 01 18:33:29 +0000 2020, Text='#Sulitjelma: Statens Naturoppsyn og politiet har gjennomført en snøscooterkontroll. 16 kontrollerte, ingen anmeldelser.'), Status(ID=1245397387776077824, ScreenName=politinordland, Created=Wed Apr 01 17:07:30 +0000 2020, Text='Vi mistenker at uhellet skyldes uaktsom kjøring. Førerkort beslaglegges, sak opprettes. https://t.co/oMaPYZFTuz'), Status(ID=1245391960086663168, ScreenName=politinordland, Created=Wed Apr 01 16:45:56 +0000 2020, Text='#Narvik: Trafikkuhell i Kongens gate. Bil kjørt inn i en snøhaug. Ikke personskade. Vi er på stedet og snakker med fører.'), Status(ID=1245380601588387844, ScreenName=politinordland, Created=Wed Apr 01 16:00:48 +0000 2020, Text='#Stokmarknes: Trafikkuhell på FV 82. Kollisjon mellom to personbiler etter at den ene parten har brutt vikeplikten.… https://t.co/VyZhdJl2p8'), Status(ID=1245369687623548930, ScreenName=politinordland, Created=Wed Apr 01 15:17:26 +0000 2020, Text='#Bodø: Bilfører stanset av UP, mistanke om ruspåvirket kjøring. Bevissikring utført, førerkort beslaglagt.'), Status(ID=1245369165696860163, ScreenName=politinordland, Created=Wed Apr 01 15:15:21 +0000 2020, Text='#Grane #E6: Politiet har gjennomført fartskontroll (gjennomsnitt). Medførte to forenklede forelegg, 108 km/t i 80-s… https://t.co/AkZaalG5X5'), Status(ID=1245341162715652096, ScreenName=politinordland, Created=Wed Apr 01 13:24:05 +0000 2020, Text='#Bodø: UP ar gjennomført fartskontroll i Bodøtunnelen. Seks bilførere gitt forenklet forelegg, høyeste hastighet var 107 km/t i 80-sone.'), Status(ID=1245340307539005441, ScreenName=politinordland, Created=Wed Apr 01 13:20:41 +0000 2020, Text='#Bodø: Bilfører stanset av UP i kontroll. Mistanke om ruspåvirket kjøring. Bevissikring utført. Førerkort beslaglagt.'), Status(ID=1245336717105774597, ScreenName=politinordland, Created=Wed Apr 01 13:06:25 +0000 2020, Text='#Sortland: Bilfører stanset for kontroll. Anmeldes for kjøring uten gyldig førerkort.'), Status(ID=1245328619670560768, ScreenName=politinordland, Created=Wed Apr 01 12:34:14 +0000 2020, Text='#Narvik: UP har avholdt laserkontroll i Bjerkvik. 20 førere fikk forenklede forelegg. Høyeste hastighet var på 74 k… https://t.co/SBoXblz4zx'), Status(ID=1245317949340205056, ScreenName=politinordland, Created=Wed Apr 01 11:51:50 +0000 2020, Text='#Øksnes: UP har avholdt laserkontroll på Nergard. 5 førere fikk forenklede forelegg. Høyeste hastighet var på 72 km/t. 60 km/t på stedet.')]"

#getTweets        # TODO: Add unicode to wtf8 conversion
        # 


#for u in followers:
#    account_data = tiv.getAccountInfo(u.screen_name)


#lol = tiv.getProjectFollowers(3)
#for i in lol:
#    print(i["screen_name"])
#    acc_string = tiv.getAccountInfo('politinordland')
#    acc_string = tiv.getAccountInfo(i)
#    tiv.insertAccountToDB(acc_string)

#acc_string = {"created_at": "Mon Dec 30 12:44:42 +0000 2013","description": "Operasjonssentralen i Nordland informerer om hendelser i distriktet. Vi svarer ikke p\u00e5 twitter, bruk heller v\u00e5r tlf 02800/75589000. Ved N\u00f8d ring 112","favourites_count": 20,"followers_count": 23587,"following": True,"friends_count": 7,"id": 2251977161,"id_str": "2251977161","listed_count": 173,"location": "Bod\u00f8","name": "Politiet i Nordland","profile_background_color": "C0DEED","profile_background_image_url":"http://abs.twimg.com/images/themes/theme1/bg.png","profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png","profile_image_url": "http://pbs.twimg.com/profile_images/417638849137741824/aHsYdiix_normal.jpeg","profile_image_url_https": "https://pbs.twimg.com/profile_images/417638849137741824/aHsYdiix_normal.jpeg","profile_link_color": "0084B4","profile_sidebar_border_color": "FFFFFF","profile_sidebar_fill_color": "DDEEF6","profile_text_color": "333333","profile_use_background_image": True,"screen_name": "politinordland","status": {"created_at":"Thu Apr 02 11:54:36 +0000 2020","favorite_count": 1,"hashtags": [],"id": 1245681033124683782,"id_str": "1245681033124683782","lang": "no","quoted_status_id": 1245675059643142146,"quoted_status_id_str": "1245675059643142146","retweet_count": 1,"source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>","text": "F\u00f8rerkortet til mistenkte er midlertidig tatt i beslag. https://t.co/BCEykXoMS3","urls": [{"expanded_url": "https://twitter.com/politinordland/status/1245675059643142146","url": "https://t.co/BCEykXoMS3"}],"user_mentions": []},"statuses_count": 21769,"url": "https://t.co/xyJnJUHaqs"}

#######
# Get followers and add all to the database
#followers = tiv.getProjectFollowers(3)
##print([u.screen_name for u in followers])
#for u in followers:
#    account_data = tiv.getAccountInfo(u.screen_name)
#    tiv.insertAccountToDB(account_data)

# Get tweets and populate the database
#screen_name = 'politinordland'
#tweet_count = '10'
#tweets = tiv.getTweets(screen_name, tweet_count)
#tiv.insertTweetsToDB(tweets)
###########



#print([u.created_at for u in tweets])
#for u in tweets:
#    print(u.user_mentions)
#    print(u.created_at)
#    print(u.favorite_count)
#    print(u.hashtags)
#    print(u.id)
#    print(u.id_str)
#    print(u.lang)
#    print(u.retweet_count)
#    print(u.source)
#    print(u.text)
#    print(u.truncated)
#    print(u.urls)
#    print(u.user)

#    tweet_text = u.text
#    # Detect words starting with upper case
#    for word in tweet_text.split():
#        if re.match(r"[A-Z]+", word):
#            print(word)
#
##    print("Hashtag:", u.hashtags)
#    for htag in u.hashtags:
#        hash_tag = htag.text
##        print(htag.text)
#    print("-------------------------------")




# TODO: DETECT SUB TWEETS (RETWEETS / LINKED OPPLEGG)


#print([s.text for s in tweets])




#tiv.getTweets(screen_name, tweet_count)

#tiv.validateConnection()
#var = tiv.getTweets('politinordland', 20)
#for blabla in var:
#    print(blabla)
# print([s.text for s in statuses])

# finnmark:alta:kåfjordbrua:stanset:Unggutt