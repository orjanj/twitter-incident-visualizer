#!/usr/bin/python3
from modules.Config import Config # TODO: Make it prettier
from modules.DB import DB # TODO: Make it prettier
from modules.Twitter import TIVTwitter # TODO: Make it prettier
from modules.File import File
from modules.Gmaps import Gmaps

# Start of application
if __name__ == '__main__':
    config = Config()
    db = DB(config)
    gmaps = Gmaps(config)
    twitter = TIVTwitter(config, db, gmaps)

    # TODO: Dump to JSON FILE
    #    {json lat long tweet text account name }
    # export til json fil + les til jquery og legg til i google string
