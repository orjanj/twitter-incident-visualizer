# twitter-incident-visualizer

This is a school project by <a href="https://github.com/orjanj">Ørjan Jacobsen</a> ([Cyber Security](https://www.noroff.no/en/studies/university-college/cyber-security)), <a href="https://github.com/palarssen">Pål Larssen</a> ([Cyber Security](https://www.noroff.no/en/studies/university-college/cyber-security)) and <a href="https://github.com/dansolb">Dan Solberg</a> ([Digital Forensics](https://www.noroff.no/en/studies/university-college/digital-forensics)).
This project provides a visual event pinpointer in Google Maps, where Tweets would be localized.

The project connects to the Twitter API with a PostgreSQL database and using Google Maps API to visualise location of events.
We have used Python backend with a database, and connecting this to the frontend we've used JavaScript JSON structure.

## Demo of finished product
Graphical demonstration: https://github.com/orjanj/twitter-incident-visualizer/blob/master/examples/Googlemaps.PNG

Video demonstration: https://github.com/orjanj/twitter-incident-visualizer/blob/master/examples/map_preview.mp4?raw=true

## Installing the application
Please read the [installation manual](https://github.com/orjanj/twitter-incident-visualizer/blob/master/INSTALL.md).



## Nice to know
The given database structure in the sql directory is outdated (one table is removed while developing the application).

The attached wordlist found in the config directory is created by [Ondkloss](https://github.com/Ondkloss/norwegian-wordlist) and released under the WTFPL licence.

Given credentials in earlier commits is reset and not in use anymore.

You need to have a Twitter developer account and access to the Google API to use this application.
