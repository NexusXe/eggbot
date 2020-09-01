# TODO: The indentation in this entire script is FUCKED
def owobot():
  import discord, ctypes, ctypes.util, logging, sys, os
  from owotext import OwO
  opusname = ctypes.util.find_library('opus')

  discord.opus.load_opus(opusname)
  if not discord.opus.is_loaded():
      raise RuntimeError('Opus failed to load')
      logging.warning('Opus failed to load.')

  uwu = OwO()

  global bound_user
  bound_user = ''

  global voiceChannelID

  client = discord.Client()

  def getAuth(wanted): # using this instead of dotenv due to the fact it was Not Having a Good Time
      file = open('eggbot/auth').readlines()
      for line in file:
          if line.startswith(wanted):
              line = str([line][0])
              line = line.replace(wanted + ' ', '')
              line = line.replace('/n', '')
              logging.debug('Token read as ' + str(line))
              print(str(line))
              return str(line)



  TOKEN = getAuth('TOKEN')

  defaultChannelID = '637690113631059979'

  defaultVoiceChannelID = ''

  voiceChannelID = ''


  def getHelp(message):
    logging.debug('Help raised.')
    if message.content == '~help':
        return ("This bot is still under development. Please be patient, but feel free to interact with it "
                "however you want. A full list of commands is coming soon, but here's what is implemented so"
                " far:\n `~help` responds with this message. Type `~help` followed by another command to learn more"
                " about that command.\n `~egg` responds with an egg.\n `~info` lists some"
                " information about this bot.\n `~owo` owo-ifies the text put after it.\n"
                " `~owox` does the same as the previous command, but deletes the original message.\n"
                "Really, there isn't much to this bot yet. But there is more to come!")
    else:
        skinned = message.content.replace('~help ', '')
        skinned = skinned.replace('~', '')
        print(skinned)
        if skinned == 'egg':
            return 'This command simply responds with an egg emoji.'
        elif skinned == 'help':
            return ('This command, with no other syntax, displays a general help message. By adding another command '
                    'after it (without the tilda), you can get more detailed information about that given command. '
                    'Like you just did!')
        elif skinned == 'owo':
            return ('This command, when followed by a string of text, will respond with that text in an owo-ified '
                    'manner.'
                    'Functionality of omitting some words is coming soon. See also: `owox`.')
        elif skinned == 'owox':
            return ('Like `owo`, `owox` responds with an owo-ified version of the input text. However, this command '
                    'deletes the original message, making it seem as if the bot is saying the text.')
        elif skinned == 'info':
            return 'This command displays some general information about the bot.'
        else:
            return 'Syntax error.'



  def owoify(message, add=' '):
    skinned = message.content.replace('~owo' + add, '')
    return uwu.whatsthis(skinned)


  async def on_ready():
    print('Bot is online.')


  # noinspection PyCompatibility
  @client.event
  async def on_message(message):
    global bound_user
    global voiceChannelID
    if message.author == client.user:
        return
    if message.content.startswith('~owo '):
        await message.channel.send(owoify(message))
    elif message.content.startswith('~owox '):
        await message.channel.send(owoify(message, 'x '))
        await message.delete()
    elif message.content.startswith('~help'):
        response = getHelp(message)
        await message.channel.send(response)
    elif message.content == '~egg':
        response = ':egg:'
        await message.channel.send(response)
    elif message.content == '~info':
        response = ("This is a prototype bot created by the user `Nexus#2396`. I really just mess with it from time to time, and I use it for TTS (coming soon!)")
        await message.channel.send(response)
    elif message.content == '~template':
        response = "Template"
        await message.channel.send(response)
    elif message.content == '~bind':
      bound_user = str(message.author.id)
      print('Bound to ' + str(message.author))
      await message.channel.send('Bound to ' + str(message.author) + '\n' + 'You can now use TTS commands.')
    elif message.content == '~unbind':
      print('Bound user output is ' + bound_user)
      if str(message.author.id) == bound_user:
        bound_user = ''
        await message.channel.send('Unbound.')
        print('Unbound.')
      else:
        await message.channel.send("You aren't bound!")
    elif message.content == '~forceunbind' and str(message.author.id) == '328380599935172611':
      bound_user = ''
      await message.channel.send('oopsie woopsie! looks like i did a bit of a fucky wucky and coomed on the TTS bindings! im vewwy sowwy. also blame nexus lmoa')
    elif message.content.startswith('~setvc'):
      voiceChannelID = message.content.replace('~setvc ', '')
      try:
        voiceChannelID = str(int(voiceChannelID))
        print(voiceChannelID)
        await message.channel.send(voiceChannelID)
      except:
        print(voiceChannelID)
        await message.channel.send('Invalid Channel ID!')
    elif message.content == '~join':
      print('The currently seen voice channel is ' + voiceChannelID)
      await message.channel.send('Unfinished command.')
      if bound_user != '':
        print('Bound to ' + bound_user + ', they can use the TTS bot until someone else binds.')
      else:
        bound_user = str(message.author.id)
      print('Current voice channel ID is '+ voiceChannelID)
      await client.join_voice_channel(voiceChannelID)
      await message.channel.send('Joined VC.')
    else:
        print(message.content)
  client.run(TOKEN)
  
if __name__ == '__main__':
  owobot()