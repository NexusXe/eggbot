def speech():
  import os, requests, json


  def getAuth(wanted): # using this instead of dotenv due to the fact it was Not Having a Good Time
      file = open('eggbot/auth').readlines()
      for line in file:
          if line.startswith(wanted):
              line = str([line][0])
              line = line.replace(wanted + ' ', '')
              line = line.replace('/n', '')
              return str(line)


  TOKEN = getAuth('TOKEN')
  print(TOKEN)
  channelID = False
  defaultChannelID = '637690113631059979'
  print(defaultChannelID)

  def send_message(channelID):
    while True:
      didCMD = False
      message = input('Type out your message or "command" to send a command. >>')
      if message == 'command':
        didCMD = True
        while True:
          message = input('Enter a command. Type "list" for a list of usable commands. >>')
          if message == 'list':
            print('Current usable commands are: list, changechannel, sendmessage, and exit.')
            continue
          elif message == 'exit':
            return 'exit'
          elif message == 'changechannel':
            channelID = set_channel()
            break
          elif message == 'sendmessage':
            break
          else:
            print('Invalid command!')
            continue
      if didCMD:
        continue
      if not channelID:
        channelID = defaultChannelID
        print('Warning: No channelID set. Using default channel.')
      baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
      headers = { "Authorization":"Bot {}".format(TOKEN),
                  "User-Agent":"eggBotSpeechLauncher (http://edgproducts.tk, v2.0",
                  "Content-Type":"application/json", }
      POSTedJSON =  json.dumps ( {"content":message} )
      r = requests.post(baseURL, headers = headers, data = POSTedJSON)
      print('Sent.')
      break


  def set_channel():
    channelID = input('Enter a new channelID.')
    if channelID == 'a':
      channelID = defaultChannelID
      print('Using default channel.')
      return channelID

  while True:
    a = send_message(channelID)
    if a == 'exit':
      break

if __name__ == "__main__":
  speech()
  