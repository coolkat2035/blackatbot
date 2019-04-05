import discord
from discord.ext import commands

token = "NTU4ODk1MDM5ODMzNDQwMjU3.D3oalQ._voS4vvKei30nRppZL24p6khNCA"

client = commands.Bot(command_prefix = "blackat: ")

@client.event
async def on_ready():
    print("blackat is online yooooooo")
    #print(client.user.name)
    #print(client.user.id)
    await client.change_presence(game = discord.Game(name = "blackat: | include space after the colon!"))
    
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
    channel = message.channel
    await client.send_message(channel,"{} deleted \"{}\".\n:regional_indicator_f: ".format(author, content))
    
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
    resp.add_field(name = field(0), value = field(1), inline = False)
    resp.add_field(name = field(2), value = field(3), inline = False)
    resp.add_field(name = field(4), value = field(5), inline = False)

    """
                       
    await client.say(embed = resp)
                       
client.run(token)
