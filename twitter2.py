import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
from locations import map







def get_map(acct):
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    if (len(acct) < 1):
        breakpoint()
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '100'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    map(js)


if __name__ == "__main__":
    pass
