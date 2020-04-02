#!/usr/bin/python3
import time
from Config import Config # TODO: Make it prettier

class File:
    def __init__(self):
        """ Main constructor """
        config = Config()
        self.config_param = config.getConfigParameter('tweet_storage')
        ts = time.gmtime()
        timestamp = time.strftime("%Y%m%d%H%M%S", ts)
#        print(timestamp) # TODO: Consider if timestamp should be set when exporting
        self.export_file = self.config_param['directory'] + '/' + self.config_param['default_filename'] + timestamp + '.' + self.config_param['default_file_extension']

#    def exportToFile(self, tweet_content, filename=self.export_file):
    def exportToFile(self, tweet_content, filename=None):
        """ Export raw data from Tweets to a file.
        :return: xxx
        """
        # Open the file in write
#        with open(filename, "w") as updated_file:
#            for line in tweet_content:
#                updated_file.write("{}\n".format(line))

    def importFromFile(self, filename=None):
        """ Import raw data from a file.
        :param filename: file to use (string)
        :return: raw Tweet data (json)
        """
        # Open the file in read
#        with open(filename, "r") as record_file:

            # Go through all lines in the file
#            for line in record_file.readlines():



# PoC:
f = File()
#f.exportToFile('asdasdasd')