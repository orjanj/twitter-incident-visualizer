#!/usr/bin/python3
#from twitter import *
import twitter
#consumer_key = 'Err7UwBle9Q6oVHwzfCygGnG2'
#consumer_secret = 'k4acSlMEgg7UCo0FvPKwt14LIuDM8wk4oT4UuivgtmOtqGbN10'
#access_token_key = '1216480282192285696-3FTTZbSr0ZRletE4wkAW6g2nS7XO46'
#access_token_secret = '3VnrbENbyP0ax89nyAHlud8e3Lifhc4CnnULZmsZbWI5o'




api = twitter.Api(consumer_key='Err7UwBle9Q6oVHwzfCygGnG2',
  consumer_secret='k4acSlMEgg7UCo0FvPKwt14LIuDM8wk4oT4UuivgtmOtqGbN10',
    access_token_key='1216480282192285696-3FTTZbSr0ZRletE4wkAW6g2nS7XO46',
    access_token_secret='3VnrbENbyP0ax89nyAHlud8e3Lifhc4CnnULZmsZbWI5o')

#twitter = Twitter(auth=OAuth('Err7UwBle9Q6oVHwzfCygGnG2', 'k4acSlMEgg7UCo0FvPKwt14LIuDM8wk4oT4UuivgtmOtqGbN10', '1216480282192285696-3FTTZbSr0ZRletE4wkAW6g2nS7XO46', '3VnrbENbyP0ax89nyAHlud8e3Lifhc4CnnULZmsZbWI5o'))
print(api.VerifyCredentials())






#import twitter
#consumer_key = 'Err7UwBle9Q6oVHwzfCygGnG2'
#consumer_secret = 'k4acSlMEgg7UCo0FvPKwt14LIuDM8wk4oT4UuivgtmOtqGbN10'
#access_token_key = '1216480282192285696-3FTTZbSr0ZRletE4wkAW6g2nS7XO46'
#access_token_secret = '3VnrbENbyP0ax89nyAHlud8e3Lifhc4CnnULZmsZbWI5o'
#api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)
#print(api.VerifyCredentials())




# https://gist.github.com/yanofsky/5436496
