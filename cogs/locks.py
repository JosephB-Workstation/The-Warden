import discord
import asyncio
from discord.ext import commands

class Locks(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def lock(self, ctx, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)
        if isinstance(channel, discord.TextChannel):
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send(f'{channel.name} has been locked!')
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(ctx.guild.default_role, speak=False)
            await ctx.send(f'{channel.name} has been locked!')
        else:
            await ctx.send('Channel not found!')


    @commands.command()
    async def unlock(self, ctx, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)
        if isinstance(channel, discord.TextChannel):
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f'{channel.name} has been unlocked!')
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(ctx.guild.default_role, speak=True)
            await ctx.send(f'{channel.name} has been unlocked!')
        else:
            await ctx.send('Channel not found!')

    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: Ratelimit has been reached, apologies for the inconvienence, please try again in a few minutes')
        if isinstance(error, commands.BadArgument):
            await ctx.send('Error: Invalid channel ID')

    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: Ratelimit has been reached, apologies for the inconvienence, please try again in a few minutes')
        if isinstance(error, commands.BadArgument):
            await ctx.send('Error: Invalid channel ID')


def setup(client):
    client.add_cog(Locks(client))
