import discord
import random
import re
import sys
import asyncio
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

TOKEN = 'token'

client = discord.Client()

@client.event
async def on_member_join(member):
        channel = client.get_channel(510553881764298766)
#        msg = 'hey look, a person'.format(message)
        print('its a new person')
        await channel.send('hey look!')
        await channel.send('its a person! ' + member.mention)

@client.event
async def on_member_remove(member):
        channel = client.get_channel(510553881764298766)
#        msg = 'hey look, a person'.format(message)
        print('its a gone person')
        await channel.send('awww.... ' + member.mention + ' left. adios amigo. unless you were a dick. but you probably werent a dick. had to have that just in case')

@client.event
async def console_input():
    await client.wait_until_ready()
    msg = input('> Message to send: ')
    await client.send_message(discord.Object(id=672990761607757837), msg)
    print('')
    await console_input()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "@splenda" in message.content.lower():
        msg = '{0.author.mention} mentioned you, splenda. <@385933420389335061>'.format(message)
        #logmsg = '${member.user.tag} splendad'
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('anon @splenda'):
        msg = 'you were anonymously @ed splenda. <@385933420389335061>'.format(message)
        print('anonsplenda')
        channel = client.get_channel(510536109990871051)
        await channel.send(msg)

    if message.content.startswith('botcommandthing'):
        msg = "Your mother"
        print(';)')
        #channel = client.get_channel(672990761607757837)
        channel = client.get_channel(679189513750446110)
        await channel.send(msg)

    if "@spnexa" in message.content.lower():
        msg = 'you wish'.format(message)
#        logmsg = '${member.user.tag} spnexad'.format(message)
        print('someone spnexad')
        await message.channel.send(msg)

    if "uwu" in message.content.lower():
        msg = 'OwO'.format(message)
        print('cancer')
        await message.channel.send(msg)

    if "mallcop" in message.content.lower():
        messages = ["A mustache a day keeps the shoplifters at bay", "The correct term is Security Officer", "I'm gonna have to ask you to tone it down. You're scaring off the other shoppers.", "Welcome to the Asshat Mall! Get your shit and get out!", "Enjoy your shopping experience!", "Sir, the area between the escalators is not a slide!", "Ma'am, if you don't leave right now, I will have to call the actual police here to arrest you!", "Our security guards are equipped with the latest in pepper spray technology", "NOT A FUCKING MALLCOP"]
        msg = random.choice(messages)
        print('mallcop')
        await message.channel.send(msg.format(message))

    if message.content.startswith(':('):
        messages = ["https://tenor.com/view/30rock-alec-baldwin-there-there-cheer-up-comfort-gif-4215371", "cheer up. theres no need to be sad. the world is a wonderful place. i mean, it kinda sucks here. but its as wonderful as you make it. so make it wonderful", "https://tenor.com/view/catbug-everything-is-ok-gif-5943760"]
        msg = random.choice(messages)
        print('cheerup')
        await message.channel.send(msg.format(message))

    if message.content.startswith('searchxkcd'):
        query = message.content.lower() + ' site:xkcd.com -site:*.xkcd.com -site:forums.xkcd.com'
        print(query)
        #query = 'xkcd sheeple'
        for j in search(query[10:], tld="com", num=1, stop=1, pause=2): 
           print(j)  
        await message.channel.send(j)

    if message.content.startswith('searchcyanide'):
        query = message.content.lower() + ' site:explosm.net'
        print(query)
        #query = 'xkcd sheeple' 
        for j in search(query[14:], tld="com", num=1, stop=1, pause=2): 
           print(j)  
        await message.channel.send(j)

#    if re.match(r'\bi\'?m', message.content.lower(), re.IGNORECASE):
    if message.content.startswith("I'm"):
        #query = message.content.lower()
        dadjoke = 'hi' + message.content.lower()[3:] + ", I'm dad"
        print(dadjoke)
        await message.channel.send(dadjoke)

    if "have a cookie" in message.content.lower():
        msg = "I LOVE COOKIES".format(message)
        await message.channel.send(msg)

    if message.content.startswith('bitch'):
        msg = 'LASAGNA!!!'.format(message)
        print('you india you lose')
        await message.channel.send(msg)

    if message.content.startswith(':)))'):
        msg = 'Woah, calm yo tits there. no one has that many chins'.format(message)
        await message.channel.send(msg)

    if ':)' == message.content.lower():
        await message.channel.send('woah there, too much happiness up in here. calm yo tits.'.format(message))

    if message.content.startswith('XD'):
        msg = 'lulz'.format(message)
        await message.channel.send(msg)

    if re.match(r'oo+f', message.content.lower()):
        msg = 'no, just no'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('D:'):
        msg = 'shocking'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!deleteme'):
        await message.channel.send('I will delete myself now...', delete_after=3.0)

    if  "<@560446299040645122>" in message.content.lower():
        msg = 'ima bot. beep boop. did you mean @splenda?'.format(message)
        print('boop beep')
        await message.channel.send(msg)

    if  "its quiet" in message.content.lower():
        msg = 'https://tenor.com/view/antisocial-hide-meme-introvert-gif-9201075'.format(message)
        print('quiet')
        await message.channel.send(msg)

    if "polygraph" in message.content.lower():
        await message.channel.send('lie detectors are a lie', file=discord.File('lie-behind-the-lie-detector.pdf'))

    if "getoptifine" in message.content.lower():
        await message.channel.send('here ya go', file=discord.File('optifine.jar'))

    if message.content.startswith('advertise'):
        print('ad')
        await message.channel.send('THIS IS AN ADVERTISEMENT', file=discord.File('boobs.jpg'))

    if message.content.startswith('mobileshrug'):
        print('shrug')
        await message.channel.send('shrugs', file=discord.File('shrug.gif'))

    if message.content.startswith('deletedtvallresponse'):
        print('delete')
#        await message.channel.send('you deleted him', file=discord.File('delete.png'))
#        msg = 'you were anonymously @ed splenda. <@385933420389335061>'.format(message)
        print('anonsplenda')
        channel = client.get_channel(510536109990871051)
        await channel.send('you deleted him', file=discord.File('delete.png'))



    if message.content.startswith('wow'):
        print('wow')
        messages = ["https://tenor.com/view/owen-wilson-wow-snapchat-gif-12686549", "https://tenor.com/view/mindblown-amazed-explosion-space-omg-gif-10279314", "https://tenor.com/view/jaw-drop-shocked-surprised-omg-amazed-gif-4919080"]
        msg = random.choice(messages)
        await message.channel.send(msg)

    if message.content.startswith(':|'):
        print(':|')
        await message.channel.send('cammy wanted a response to this one, so here ya go')

    if 'nooo' in message.content.lower():
        print('nooo')
        await message.channel.send('no', file=discord.File('no.gif'))

    if 'peter' in message.content.lower():
        print('peter')
        await message.channel.send('bestgif', file=discord.File('8bitpeter.mp4'))

    if 'fedora' in message.content.lower():
        print('splendashairsalon.gb')
        await message.channel.send('lets play a game', file=discord.File('splendashairsalon.gb'))

    if 'f' == message.content.lower():
        print('pay respeccs')
        await message.channel.send('a salute to the fallen', file=discord.File('F.gif'))

    if 'bad bot' in message.content.lower():
        print('splendas a dick')
        await message.channel.send("you're not my dad")

@client.event
async def on_ready():
    game = discord.Game("Minecraft, but for Bots")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #console_input()

client.run(TOKEN)
