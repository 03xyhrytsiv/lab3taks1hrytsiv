import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

acct = input('Enter Twitter Account:')
count = input('Enter number of friends needed:')
whereInput = input('Enter place to output info(console/file):')


def settings(acct, count):
    """
    Receives two parameters: account and number of friends
    This function contains all needed verifications and connection to get to
    twitter account and returns all the data about the users
    Also it ignores SSL certificate errors
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': count})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    return data


def chosenInformation():
    """
    Has a data with friends from the function "settings" and returns only
    selected information about the user in json format
    You could have it printed out either in console or in "newFile.json" file
    """
    finalDict = {}
    myList = []
    friends = json.loads(settings(acct, count))

    with open('newFile.json', 'w', encoding='utf-8') as file:

        for element in friends["users"]:
            keys = ['id', 'screen_name', 'location', 'created_at', 'friends_count', 'lang', 'time_zone']
            dict1 = {}
            for key in keys:
                dict1[key] = element[key]
            myList.append(dict1)

        finalDict["users"] = myList

        if whereInput == 'file':
            json.dump(finalDict, file, indent=4)
            return "Now enter the newFile.json"
        elif whereInput == 'console':
            return json.dumps(finalDict, indent=4)


print(chosenInformation())
