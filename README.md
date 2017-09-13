##### add config file

~~~python
# -*- cording: utf-8 -*-

CHANNEL_ACCESS_TOKEN = <line bot channel access token>
TO                   = <line bot end point>
MESSAGE              = <default push message>
CONSUMER_KEY         = <twitter consumer key>
CONSUMER_SECRET      = <twitter cousumer secret>
ACCESS_TOKEN         = <twitter access token>
ACCESS_TOKEN_SECRET  = <twitter access token secret>
~~~

##### upload heroku

~~~bash
$ git push heroku master
$ heroku ps:scale bot=1
$ heroku ps:scale web=1
~~~
