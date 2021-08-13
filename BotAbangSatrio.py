import os
import discord
from dotenv import load_dotenv
import pickle
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents().all()

prefix = ">"
bot = commands.Bot(command_prefix=prefix, intents=intents)

saves = {}

class PlayerStats:
    def __init__(self, health, money):
        self.health = health
        self.money = money

@bot.event
async def on_ready():
    for guild in bot.guilds:
        members = '\n>'.join([member.name for member in guild.members])
        print(f"{guild}'s members:\n>{members}")
        status = discord.Game("PROJECT PAPER")
        await bot.change_presence(status=discord.Status.online, activity=status)
        print(saves)

@bot.command()
async def setstats(ctx, *args):
    saves[ctx.author.id] = PlayerStats(args[0], args[1])
    with open("data.txt", "wb") as savefile:
        pickle.dump(saves, savefile)
    await ctx.send(f"Player {ctx.author} berhasil registrasi")

@bot.command()
async def getstats(ctx):
    with open("data.txt", "rb") as savefile:
        saves = pickle.load(savefile)
    if ctx.author.id in saves:
        data = saves[ctx.author.id]
        await ctx.send(f"Player {ctx.author} \n>Health: {data.health}\n>Money: {data.money} ")
    else:
        await ctx.send(f"Player {ctx.author} belum registrasi menggunakan !setstats")

bot.run(TOKEN)

##@bot.command()
##async def test(ctx):
##    await ctx.send(str(ctx.author in ctx.guild.members))
##
##@bot.command()
##async def repeat(ctx, text):
##    await ctx.send(f"{ctx.author.mention} {text}")
##
##@bot.command()
##async def ping(ctx, target, amount):
##    for i in range(int(amount)):
##        await ctx.send(target)

##intents = discord.Intents().all()
##client = discord.Client(prefix = '', intents=intents)


##@bot.command()
##async def setstr(ctx, *, string):
##    saves[ctx.author.id] = string
##
##@bot.command()
##async def getstr(ctx):
##    await ctx.send(saves[ctx.author.id])

##client = discord.Client(prefix = '', intents=intents)

##        status = discord.CustomActivity("lagi di perbaikin BangSat")
##@client.event
##async def on_message(message):
##    if message.author != client.user:
##        if message.content[0] == prefix:
##            parameters = message.content.split()
##            command = parameters[0]
##            if command == "~ping":
##                for i in range(int(parameters[2])):
##                    await message.channel.send(f'@{message.raw_mentions[0]}')

##    guild = discord.utils.get(client.guilds, name=GUILD)
##
##    print(
##        f'{bot.user} is connected to the following guild:\n'
##        f'{guild.name}(id: {guild.id})\n'
##    )
##
##    members = '\n - '.join([member.name for member in guild.members])
##    print(f'Guild Members:\n - {members}')
##@client.event
##async def on_message(message):
##    await bot.process_commands(message)
##@client.event
##async def on_typing(channel, user, when):
##    await channel.send(f"diem asu napa typing")

