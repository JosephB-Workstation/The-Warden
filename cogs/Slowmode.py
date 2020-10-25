import discord
import asyncio
from discord.ext import commands

class Slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cslow(self, ctx, seconds, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)
        if isinstance(channel, discord.TextChannel):
            await channel.edit(slowmode_delay=seconds)
            await ctx.send(f'{channel.name}\'s slow mode timer was set to {seconds} seconds!')
        elif isinstance(channel, discord.VoiceChannel):
            await ctx.send('Voice channels do not have a slow mode to edit!')
        else:
            await ctx.send('Channel not found!')


    @cslow.error
    async def cslow_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: Invalid time for slowmode! Please enter a time in seconds!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Error: Time in seconds not given!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('Error: Invalid channel ID')

def setup(client):
    client.add_cog(Slowmode(client))
