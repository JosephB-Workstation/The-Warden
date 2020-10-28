import discord
import asyncio
import os
import time
from discord.ext import commands


client = commands.Bot(command_prefix='w.')
client.remove_command('help')

@client.event
async def on_ready():  # when the bot is fully prepared to run.
    print('Warden Online...')
    discord.Intents.default()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="w.help for help!"))

def readtoken():
    print('Attempting to read token.txt from the local directory, if it doesn\'t exist, the bot will crash. Please only put your bot token in that file, and nothing else.')
    time.sleep(2)
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'token.txt')
    keygrab = open(filename)
    key = keygrab.read()
    keygrab.close()
    return key

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Error: Command Not found! w.help for a list of commands!')


file = os.path.dirname(os.path.abspath(__file__))
location = os.path.join(file, './cogs')
for filename in os.listdir(location):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(str(readtoken()))
