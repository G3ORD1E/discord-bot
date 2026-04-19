import discord
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!',intents = intents)

@bot.event
async def on_ready():
    print('Online')

@bot.command()
async def hello(ctx):
    await ctx.send('hello there')
@bot.command()
async def time(ctx):
    t = datetime.now()
    await ctx.send(t)

bot.run("-Token paste here-")
