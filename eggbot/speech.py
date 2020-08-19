import os, requests, json


def getAuth(wanted): # using this instead of dotenv due to the fact it was Not Having a Good Time
    file = open('auth').readlines()
    for line in file:
        if line.startswith(wanted):
            print(line)
            line = str([line][0])
            line = line.replace('TOKEN ', '')
            return line


TOKEN = getAuth('TOKEN')
print(TOKEN)


defaultChannelID = '637690113631059979'

channelID = input('Channel ID >>')



if channelID == 'a':
    channelID = defaultChannelID
    print('Using default channel.')

message = input('Message >>')

baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(TOKEN),
             "User-Agent":"eggBotSpeech (http://edgproducts.tk, v1.0)",
            "Content-Type":"application/json", }


while True:
    POSTedJSON =  json.dumps ( {"content":message} )
    r = requests.post(baseURL, headers = headers, data = POSTedJSON)
    message = input('Enter new message. Reply "command" to preform a command. >>')
    if message == 'command'
    if message == 'changechannel':
        channelID = input('New Channel ID >>')
        message = input('New Message >>')
        if channelID == 'a':
            channelID = defaultChannelID
            print('Using default channel.')
    baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
    headers = { "Authorization":"Bot {}".format(TOKEN),
             "User-Agent":"myBotThing (http://some.url, v0.1)",
            "Content-Type":"application/json", }
    
