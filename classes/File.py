#!/usr/bin/python3
from Config import Config # TODO: Make it prettier

class File:
    def __init__(self):
        """ Main constructor """
        config = Config()
        self.config_param = config.getConfigParameter('tweet_storage')
        timestamp = ''
        self.export_file = self.config_param['directory'] + '/' + self.config_param['default_filename'] + timestamp + '.' + self.config_param['default_file_extension']

#    def exportToFile(self, tweet_content, filename=self.export_file):
    def exportToFile(self, tweet_content, filename='tweet-202004010100.json'):
        """ Export raw data from Tweets to a file.
        :return: xxx
        """

    def importFromFile(self, filename='tweet-202004010100.json'):
        """ Import raw data from a file.
        :return: raw Tweet data (json)
        """