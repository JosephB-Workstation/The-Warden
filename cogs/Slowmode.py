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

        if(channel == None):
            await ctx.send("Channel not found.")
            return

        permission = channel.permissions_for(ctx.author)
        permission2 = channel.permissions_for(ctx.guild.me)

        if permission.manage_channels != True:
            await ctx.send('Error: You do not have the required permission: *Manage channels* for this command!')
        elif permission2.manage_channels != True:
            await ctx.send('Error: I not have the required permission: *Manage channels* for this command!')

        elif isinstance(channel, discord.TextChannel):
            await channel.edit(slowmode_delay=seconds)
            await ctx.send(f'{channel.name}\'s slow mode timer was set to **{seconds}** seconds!')
        elif isinstance(channel, discord.VoiceChannel):
            await ctx.send('Error: Sorry, but this command only works for text channels!')



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
