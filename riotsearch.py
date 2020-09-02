from riotwatcher import LolWatcher
from requests.exceptions import HTTPError
import cfg

key = cfg.key
watcher = LolWatcher(key)
my_region = 'na1'

x = 0


# fetch last match detail and what parID they where minus 1
def finduserId(name, match_detail):
    global x
    x = 0
    for item in match_detail.get('participantIdentities'):
        snam = item.get('player').get('summonerName')
        if name == snam:
            return x
        x += 1


# get the matchdetails of last game for the user
def findUser(name):
    try:
        me = watcher.summoner.by_name(my_region, name)
        my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
        last_match = my_matches['matches'][0]
        match_detail = watcher.match.by_id(my_region, last_match['gameId'])
        return match_detail
    except HTTPError:
        print("Error")
        return "No data"


# gets the stats from the match data and userID
def findStats(userName):
    global x
    match_detail = findUser(userName)
    if match_detail == "No data":
        print("No data for " + userName)
        return "No data"
    else:
        gamekills = []
        gamedeaths = []
        kda = []
        userId = finduserId(userName, match_detail)
        print(userId)
        for item in match_detail.get('participants'):
            datak = item.get('stats').get('kills') + item.get('stats').get('assists')
            datad = item.get('stats').get('deaths')
            if datad == 0:
                datad = 1
            gamekills.append(datak)
            gamedeaths.append(datad)
            kda.append(round(datak / datad, 1))
        print(userName)
        print("    Kills plus assists " + str(gamekills[userId]))
        print("    Deaths " + str(gamedeaths[userId]))

        x = 0
        return kda[userId]


def winCheck(userName):
    wins = []
    match_detail = findUser(userName)
    userId = finduserId(userName, match_detail)
    for item in match_detail.get('participants'):
        wins.append(item.get('stats').get('win'))
    if wins[userId]:
        return True
    else:
        return False

