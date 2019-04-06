import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "blackat: ")

client.remove_command('help')
client.remove_command('ban')

@client.event
async def on_ready():

    #print(client.user.name)
    #print(client.user.id)
    await client.change_presence(game = discord.Game(name = "You" , type = 3))
    
@client.event
async def on_message(message):
    
    author = message.author
    await client.process_commands(message)
    #print("-------")
    #print(author, ":\n", content, "\n")
    
@client.event
async def on_message_delete(message):
    
    author = message.author
    content = message.content
    await client.say("{} has just deleted \"{}\".\n:regional_indicator_f: ".format(author, content))
    
@client.command()
async def say(*stuff):
    
    resp = " "
    for w in stuff:
        resp += w
        resp += " "
    await client.say(resp)

@client.command()
async def embed():
    
    resp = discord.Embed(
        title = "default title",
        description = "descriptive description",
        colour = 0xffffff
        )

    resp.set_footer(text = "Can you smell it?")
    resp.set_image(url = "https://cdn.discordapp.com/avatars/491626514434228226/8281303d76ff1586b492443f74d3a6ea.png?size=256")
    resp.set_thumbnail(url = "https://cdn.discordapp.com/avatars/491626514434228226/8281303d76ff1586b492443f74d3a6ea.png?size=256")
    resp.set_author(name = "Blackat", icon_url = "https://cdn.discordapp.com/avatars/491626514434228226/8281303d76ff1586b492443f74d3a6ea.png?size=256")
    """
    resp.add_field(name = , value = , inline = False)
    resp.add_field(name = , value = , inline = False)
    resp.add_field(name = , value = , inline = False)
    """
                       
    await client.say(embed = resp)

@client.command()
async def help():

    resp = discord.Embed(
        title = "Help mom what is this bot for",
        description = "this bot is not for cleaning up your bot anyways",
        colour = 0xffffff
        )

    resp.add_field(name = ":cold_sweat: Pics" , value = """```i dont have any ideas aaaaaaaaa```""")
    resp.add_field(name = ":cold_sweat: Cat's working progress", value = """```progress ,
sneak_peak ,
wip,
status```""", inline = False)
    resp.set_footer(text = "Ya im done here")

    await client.say(embed = resp)

@client.command()
async def ban():
    
    greet = ["hi", "hello" , "uh" , "um" , "aaag"]
    me = ["i" , "I"]
    be = ["\'m", " am"]
    reason = [" not for banning and stuff", " not here to ban people", " just a fun bot", " not a mod so i cant do anything about that" , " outta here"]
    punc =["." , "..." , "!" , "!!!!!!!111!"]
    
    await client.say(random.choice(greet) + ", " + random.choice(me) + random.choice(be) + random.choice(reason) + random.choice(punc))
    
client.run(token)
