# bot.py
import os, discord, sys
from owotext import OwO

uwu = OwO()


def getAuth(wanted):
    file = open('auth').readlines()
    for line in file:
        if line.startswith(wanted):
            print(line)
            line = str([line][0])
            line = line.replace('TOKEN ', '')
            return line


TOKEN = getAuth('TOKEN')
print(TOKEN)


def getHelp(message):
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


client = discord.Client()


# noinspection PyCompatibility
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('~owo ') and not message.content.startswith('~owox '):  # makes sure that message
        # does not have arguments for other command in it; redundant but fixes some weird issues
        skinned = (message.content.replace('~owo ', ''))
        response = uwu.whatsthis(skinned)
        await message.channel.send(response)
    if message.content.startswith('~owox ') and not message.content.startswith('~owo '):  # same as above
        skinned = message.content.replace('~owox ', '')
        response = uwu.whatsthis(skinned)
        await message.channel.send(response)
        await message.delete()
    if message.content.startswith('~help'):
        response = getHelp(message)
        await message.channel.send(response)
    elif message.content == '~egg':
        response = ':egg:'
        await message.channel.send(response)
    elif message.content == '~dointro':
        if message.author == '328380599935172611':
            response = ("Hello! I'm your local neighborhood :egg:! Feel free to interact with me! :smiley: Currently"
                        " I don't do much, but I'm learing! A list of my commands can be found by typing `~help`")
            await message.channel.send(response)
    elif message.content == '~info':
        response = ("This is a prototype bot created by the user `Nexus#2396`. Its purpose is simply as a means of"
                    " testing. However, in the more long-term, there are plans to turn this into a bot that produces"
                    " AI-generated responses to input messages. That is far from where it is now. Any feature"
                    " requests can be directed to DMs.")
        await message.channel.send(response)
    elif message.content == '~template':
        response = "Template"
        await message.channel.send(response)
    else:
        print('dont care didnt ask')
        print('Ignored message content: ' + message.content)


client.run(TOKEN)
