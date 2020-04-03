#!/usr/bin/python3
import json
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

    result = db.execute("select a.account_screen_name,a.account_pic_url, a.account_url, a.account_name, t.tweet_lat, t.tweet_long, t.tweet_time, t.tweet_content from account a, tweets t where a.account_id = t.account_id")
    json_list = []
    for row in result:
        dct = {}
        dct['screen_name'] = row[0].strip()
        dct['profile_pic'] = row[1].strip()
        dct['twitter_url'] = row[2].strip()
        dct['account_name'] = row[3].strip()
        dct['lat'] = row[4]
        dct['lng'] = row[5]
        dct['time'] = row[6].strip()
        dct['tweet_content'] = row[7].strip()
        json_list.append(dct)

    json_dump = json.dumps(json_list, indent=2)
    with open('examples/web_application.json', "w") as updated_file:
        updated_file.write(json_dump)