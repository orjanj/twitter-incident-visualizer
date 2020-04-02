#!/usr/bin/python3
#import datetime
from modules.Config import Config # TODO: Make it prettier
from modules.DB import DB # TODO: Make it prettier
from modules.Twitter import TIVTwitter # TODO: Make it prettier
from modules.File import File
from modules.Gmaps import Gmaps


if __name__ == '__main__':
    config = Config()
    db = DB(config)
    gmaps = Gmaps(config)
    twitter = TIVTwitter(config, db, gmaps)
#    twitter.validateConnection() # ok



    exit()
#    twitter = TIVTwitter()
#    gmaps = Gmaps()








# Start of mining script
#if __name__ == 'main':
#    tweet = TIVTwitter()
#    tweet_content = getTweets()
##   tw = tiv.getTweet('account=politietinordland,account=politietioslo')
##   for x in tw:
##       print('some shiet' + x)
#
#    mine = Mining()
#    mine.exportToFile(tweet_content)
#    mine.importFromFile(tweet_content)

    # TODO: ADD SOME REGEXP - parse tweet    
#s = "#Rana: @Utrykningspol har gjennomført fartskontroll i Korgfjelltunnelen. Resultat: 2 stk. forenklede forelegg, høyeste måling 98 km/t i 80 sonen."
#print(re.split('#([A-Za-z])(:)', s)[1])
#l = re.compile('(#)([A-Za-z0-9]:)').split(s)
#print(l)
# TEST DATA:
# Vestvågøy/Ner-Voll: brann i traktor på gårdsvei. Ingen personskader. Nødetatene er på tur mot stedet
# #Rana: @Utrykningspol har g#en: @Utrykningspol har gjennomført laserkontroll i 60-sona. Resultat: 7 forenkla forelegg er utskrevet, høyeste hastighet målt til 77 km/t.
# Bilen er helt utbrent. Vi har pågrepet en person mistenkt for bilbrukstyveri og ruspåvirket kjøring.
# #Sortland: #Blokken: Mann i begynnelsen av 30 årene hadde kjørt seg fast i en snøskavel. Mistenkes for promillekjøring. Fremstilles legevakt for bevissikring.

#    account_name = ''
#    hash_tag = ''
#    tweet_content = ''
#    tweet.insertTweetToDB(account_name, hash_tag, tweet_content)
    # TODO: Add more data to this function

    # TODO: jQuery @ demo.html to generate list structure for pinpoints on map
    # jQuery script runs GET AJAX request from JS to backend Py that returns tweets from DB (with lat/long)


#class Mining:
#    """ Base class for mining Tweets from Twitter. """
#
#    def __init__(self):
#        """ Instance constructor
#        :return: none
#        """
#        config = Config()
#        config_param = config.getConfigParameter('gmaps')
#        file_param = config.getConfigParameter('file')
#        file = File()
##        self.filename = file.export_file # todo: fix
#
#    def parseContent(self, tweet_content):
#        """ Parse the content of a Tweet. """
#        # TODO: Create objects/lists/etc out of this