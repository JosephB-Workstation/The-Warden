import discord
import asyncio
from discord.ext import commands

class Lockdowns(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lockdown(self, ctx, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)


        if(channel == None):
            await ctx.send("Channel Not found!")
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
            await ctx.send(f'**{channel.name}** has been locked down!')
            await channel.set_permissions(ctx.guild.default_role, read_messages=False)
        elif isinstance(channel, discord.VoiceChannel):
            await ctx.send(f'**{channel.name}** has been locked down!')
            await channel.set_permissions(ctx.guild.default_role, view_channel=False)


    @commands.command()
    async def unlockdown(self, ctx, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)


        if(channel == None):
            await ctx.send("Channel Not found!")
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
            await ctx.send(f'**{channel.name}** has been unlocked down!')
            await channel.set_permissions(ctx.guild.default_role, read_messages=True)
        elif isinstance(channel, discord.VoiceChannel):
            await ctx.send(f'**{channel.name}** has been unlocked down!')
            await channel.set_permissions(ctx.guild.default_role, view_channel=True)


def setup(client):
    client.add_cog(Lockdowns(client))
