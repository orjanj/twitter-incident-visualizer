#!/usr/bin/python
import twitter
from Config import Config # TODO: Make it prettier
from DB import DB # TODO: Make it prettier
import pprint

class TIVTwitter:
    """ Base class for connecting and fetching data from Twitter API. """

    def __init__(self):
        """ Instance constructor
        :return: none
        """
        config = Config()
        self.config_param = config.getConfigParameter('twitter')
        self.API = twitter.Api(consumer_key = self.config_param['consumer_key'],
                      consumer_secret = self.config_param['consumer_secret'],
                      access_token_key = self.config_param['access_token_key'],
                      access_token_secret = self.config_param['access_token_secret'])

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
#        user_timeline = self.API.GetUserTimeline(screen_name=screen_name, count=tweet_count)
#        return(user_timeline)
        example_data = "[Status(ID=1245681033124683782, ScreenName=politinordland, Created=Thu Apr 02 11:54:36 +0000 2020, Text='Førerkortet til mistenkte er midlertidig tatt i beslag. https://t.co/BCEykXoMS3'), Status(ID=1245680172155711490, ScreenName=politinordland, Created=Thu Apr 02 11:51:11 +0000 2020, Text='#Sortland FV820 v/Sandstrand: @Utrykningspol har gjennomført laserkontroll på stedet. 4 ff. Høyeste hastighet var 75 km/t i 60 sone.'), Status(ID=1245675059643142146, ScreenName=politinordland, Created=Thu Apr 02 11:30:52 +0000 2020, Text='#Bodø: Mann i midten av 20 årene mistenkt for ruspåvirket kjøring. Stanset av @Utrykningspol . Fremstilles for bevissikring.'), Status(ID=1245639331223486476, ScreenName=politinordland, Created=Thu Apr 02 09:08:54 +0000 2020, Text='#Ballstad: patr har stanset mannlig bilfører som ikke har gyldig førerkort. Blir anmeldt.'), Status(ID=1245637948042698754, ScreenName=politinordland, Created=Thu Apr 02 09:03:24 +0000 2020, Text='Rettelse: Hendelsen har ikke skjedd i et fotgjengerfelt, men idet fotgjenger skulle krysse veien. Vi er i kontakt m… https://t.co/mHBZVpKhBb'), Status(ID=1245625369475964932, ScreenName=politinordland, Created=Thu Apr 02 08:13:25 +0000 2020, Text='#Narvik, Fagernes: fotgjenger truffet av sidespeilet til bil idet denne passerte, skal ha skjedd i fotgjengerfelt.… https://t.co/KRi7TQerGZ'), Status(ID=1245566502113345536, ScreenName=politinordland, Created=Thu Apr 02 04:19:30 +0000 2020, Text='#Sortland. kl 0230 stopper patruljen en bil med 4 stk i. Fører har ikke gyldig førerkort og det blir gjort beslag a… https://t.co/Uo0OYMGxCU'), Status(ID=1245448350494752769, ScreenName=politinordland, Created=Wed Apr 01 20:30:00 +0000 2020, Text='Politiet har gjort undersøkelser på stedet. Bilfører avhørt. Førerkort beslaglegges, sak opprettes. https://t.co/MN0HNld47M'), Status(ID=1245438413433704449, ScreenName=politinordland, Created=Wed Apr 01 19:50:31 +0000 2020, Text='#Leknes: Ambulanse og politi har rykket ut til privatadresse etter melding om at en person er påkjørt i en oppkjørs… https://t.co/418nQyia9r'), Status(ID=1245419026848907266, ScreenName=politinordland, Created=Wed Apr 01 18:33:29 +0000 2020, Text='#Sulitjelma: Statens Naturoppsyn og politiet har gjennomført en snøscooterkontroll. 16 kontrollerte, ingen anmeldelser.'), Status(ID=1245397387776077824, ScreenName=politinordland, Created=Wed Apr 01 17:07:30 +0000 2020, Text='Vi mistenker at uhellet skyldes uaktsom kjøring. Førerkort beslaglegges, sak opprettes. https://t.co/oMaPYZFTuz'), Status(ID=1245391960086663168, ScreenName=politinordland, Created=Wed Apr 01 16:45:56 +0000 2020, Text='#Narvik: Trafikkuhell i Kongens gate. Bil kjørt inn i en snøhaug. Ikke personskade. Vi er på stedet og snakker med fører.'), Status(ID=1245380601588387844, ScreenName=politinordland, Created=Wed Apr 01 16:00:48 +0000 2020, Text='#Stokmarknes: Trafikkuhell på FV 82. Kollisjon mellom to personbiler etter at den ene parten har brutt vikeplikten.… https://t.co/VyZhdJl2p8'), Status(ID=1245369687623548930, ScreenName=politinordland, Created=Wed Apr 01 15:17:26 +0000 2020, Text='#Bodø: Bilfører stanset av UP, mistanke om ruspåvirket kjøring. Bevissikring utført, førerkort beslaglagt.'), Status(ID=1245369165696860163, ScreenName=politinordland, Created=Wed Apr 01 15:15:21 +0000 2020, Text='#Grane #E6: Politiet har gjennomført fartskontroll (gjennomsnitt). Medførte to forenklede forelegg, 108 km/t i 80-s… https://t.co/AkZaalG5X5'), Status(ID=1245341162715652096, ScreenName=politinordland, Created=Wed Apr 01 13:24:05 +0000 2020, Text='#Bodø: UP ar gjennomført fartskontroll i Bodøtunnelen. Seks bilførere gitt forenklet forelegg, høyeste hastighet var 107 km/t i 80-sone.'), Status(ID=1245340307539005441, ScreenName=politinordland, Created=Wed Apr 01 13:20:41 +0000 2020, Text='#Bodø: Bilfører stanset av UP i kontroll. Mistanke om ruspåvirket kjøring. Bevissikring utført. Førerkort beslaglagt.'), Status(ID=1245336717105774597, ScreenName=politinordland, Created=Wed Apr 01 13:06:25 +0000 2020, Text='#Sortland: Bilfører stanset for kontroll. Anmeldes for kjøring uten gyldig førerkort.'), Status(ID=1245328619670560768, ScreenName=politinordland, Created=Wed Apr 01 12:34:14 +0000 2020, Text='#Narvik: UP har avholdt laserkontroll i Bjerkvik. 20 førere fikk forenklede forelegg. Høyeste hastighet var på 74 k… https://t.co/SBoXblz4zx'), Status(ID=1245317949340205056, ScreenName=politinordland, Created=Wed Apr 01 11:51:50 +0000 2020, Text='#Øksnes: UP har avholdt laserkontroll på Nergard. 5 førere fikk forenklede forelegg. Høyeste hastighet var på 72 km/t. 60 km/t på stedet.')]"
        return(example_data)

    def getProjectFollowers(self, follower_count):
        """ Get our projects followers from Twitter.
        """
#        project_friendslist = self.API.GetFriends(count=follower_count)
#        return(project_friendslist)
        example_data = '[User(ID=839082941036789760, ScreenName=politietost), User(ID=437997027, ScreenName=PolitiTrondelag), User(ID=1251538416, ScreenName=PolitiMRpd), User(ID=3389005078, ScreenName=110Finnmark), User(ID=382593384, ScreenName=Utrykningspol), User(ID=560997111, ScreenName=110Agder), User(ID=480253925, ScreenName=Oslo110sentral), User(ID=2507231689, ScreenName=110Bodo), User(ID=1047599642, ScreenName=politifinnmark), User(ID=1479532554, ScreenName=politiagder), User(ID=381502681, ScreenName=oslopolitiops), User(ID=1374416472, ScreenName=polititroms), User(ID=2251977161, ScreenName=politinordland)]'
        return(example_data)

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
#        user_info = self.API.GetUser(screen_name=screen_name)
#        print(user_info)
        example_data = '{"created_at": "Mon Dec 30 12:44:42 +0000 2013","description": "Operasjonssentralen i Nordland informerer om hendelser i distriktet. Vi svarer ikke p\u00e5 twitter, bruk heller v\u00e5r tlf 02800/75589000. Ved N\u00f8d ring 112","favourites_count": 20,"followers_count": 23587,"following": true,"friends_count": 7,"id": 2251977161,"id_str": "2251977161","listed_count": 173,"location": "Bod\u00f8","name": "Politiet i Nordland","profile_background_color": "C0DEED","profile_background_image_url":"http://abs.twimg.com/images/themes/theme1/bg.png","profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png","profile_image_url": "http://pbs.twimg.com/profile_images/417638849137741824/aHsYdiix_normal.jpeg","profile_image_url_https": "https://pbs.twimg.com/profile_images/417638849137741824/aHsYdiix_normal.jpeg","profile_link_color": "0084B4","profile_sidebar_border_color": "FFFFFF","profile_sidebar_fill_color": "DDEEF6","profile_text_color": "333333","profile_use_background_image": true,"screen_name": "politinordland","status": {"created_at":"Thu Apr 02 11:54:36 +0000 2020","favorite_count": 1,"hashtags": [],"id": 1245681033124683782,"id_str": "1245681033124683782","lang": "no","quoted_status_id": 1245675059643142146,"quoted_status_id_str": "1245675059643142146","retweet_count": 1,"source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>","text": "F\u00f8rerkortet til mistenkte er midlertidig tatt i beslag. https://t.co/BCEykXoMS3","urls": [{"expanded_url": "https://twitter.com/politinordland/status/1245675059643142146","url": "https://t.co/BCEykXoMS3"}],"user_mentions": []},"statuses_count": 21769,"url": "https://t.co/xyJnJUHaqs"}'
        return(example_data)

    def insertTweetToDB(self, account_name, hash_tag, tweet_content):
        """ Insertion of tweet(s) to PostgreSQL DB.
        :params: tweet_data (json)
        :return: xxx
        """
        # TODO: Add unicode to wtf8 conversion
        # https://stackoverflow.com/questions/4182603/how-to-convert-a-string-to-utf-8-in-python
        db = DB()
        statement = ''
        db.insertQuery()





# PoC:
tiv = TIVTwitter()
#tiv.getProjectFollowers()
tiv.getAccountInfo('politinordland')

#tiv.validateConnection()
#var = tiv.getTweets('politinordland', 20)
#for blabla in var:
#    print(blabla)
# print([s.text for s in statuses])




# finnmark:alta:kåfjordbrua:stanset:Unggutt
# REF:
# https://www.alexkras.com/how-to-get-user-feed-with-twitter-api-and-python/
# https://github.com/Ondkloss/norwegian-wordlist
# https://github.com/bear/python-twitter/blob/master/examples/get_all_user_tweets.py

# https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api
# https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api.GetFriends
# https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api.GetUser
# https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api.GetUserTimeline
# https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api.VerifyCredentials
