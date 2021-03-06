import discord
import asyncio
from discord.ext import commands

class Userlimit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userlimit(self, ctx, limit: int=0, targetid: int=1):
        channel = None
        if targetid == 1:
            await ctx.send("Error: Voice channel ID not found!")
            return
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
        elif isinstance(channel, discord.VoiceChannel):
            if limit > -1 or limit < 100:
                await channel.edit(user_limit=limit)
                await ctx.send(f'**{channel.name}\'s** user limit has been set to {limit}')
            else:
                await ctx.send("Error: User rate invalid! Please enter in a user limit between 0 and 99 users!")
        else:
            await ctx.send("Error: Sorry, but this command only works on voice channels!")


def setup(client):
    client.add_cog(Userlimit(client))
