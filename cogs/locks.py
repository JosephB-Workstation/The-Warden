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

        if(channel == None):
            await ctx.send("Channel not found.")
            return

        permission = channel.permissions_for(ctx.author)
        permission2 = channel.permissions_for(ctx.guild.me)

        if permission.manage_channels != True:
            await ctx.send('Error: You do not have the required permission: *Manage channels* for this command!')
        elif permission2.manage_channels != True:
            await ctx.send('Error: I not have the required permission: *Manage channels* for this command!')
        elif permission.manage_permissions != True:
            await ctx.send('Error: You do not have the required permission: *Manage permissions* for this command!')
        elif permission2.manage_permissions != True:
            await ctx.send('Error: I not have the required permission: *Manage permissions* for this command!')
        elif isinstance(channel, discord.TextChannel):
            await ctx.send(f'**{channel.name}** has been locked!')
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        elif isinstance(channel, discord.VoiceChannel):
            await ctx.send(f'**{channel.name}** has been locked!')
            await channel.set_permissions(ctx.guild.default_role, speak=False)
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

        if(channel == None):
            await ctx.send("Channel not found.")
            return

        permission = channel.permissions_for(ctx.author)
        permission2 = channel.permissions_for(ctx.guild.me)
        if permission.manage_channels != True:
            await ctx.send('Error: You do not have the required permission: *Manage channels* for this command!')
        elif permission2.manage_channels != True:
            await ctx.send('Error: I not have the required permission: *Manage channels* for this command!')
        elif permission.manage_permissions != True:
            await ctx.send('Error: You do not have the required permission: *Manage permissions* for this command!')
        elif permission2.manage_permissions != True:
            await ctx.send('Error: I not have the required permission: *Manage permissions* for this command!')
        elif isinstance(channel, discord.TextChannel):
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f'**{channel.name}** has been unlocked!')
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(ctx.guild.default_role, speak=True)
            await ctx.send(f'**{channel.name}** has been unlocked!')
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
