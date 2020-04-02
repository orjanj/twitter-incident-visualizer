#!/usr/bin/python3
import time

class File:
    def __init__(self, config):
        """ Main constructor """
        self.config_param = config.getConfigParameter('tweet_storage')
        ts = time.gmtime()
        timestamp = time.strftime("%Y%m%d%H%M%S", ts)

    def exportToFile(self, tweet_content):
        """ Export raw data from Tweets to a file.
        :param tweet_content: contents of a tweet (string)
        """
        export_file = self.config_param['directory'] + '/' + self.config_param['default_filename'] + timestamp + '.' + self.config_param['default_file_extension']
 
        # Open the file in write
        with open(filename, "w") as updated_file:
            for line in tweet_content:
                updated_file.write("{}\n".format(line))

    def importFromFile(self, filename=None):
        """ Import raw data from a file.
        :param filename: file to use (string)
        :return: raw Tweet data (json)
        """
        # Open the file in read
        with open(filename, "r") as record_file:
            return(record_file.readlines())