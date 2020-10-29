import discord
import asyncio
from discord.ext import commands

class Bitrate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bitrate(self, ctx, rate: int=64, targetid: int=1):
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
            if rate > 7 or rate < 97:
                await channel.edit(bitrate=(rate*1000))
                await ctx.send(f"**{channel.name}'s** bitrate has been set to {rate}kbps")
            else:
                await ctx.send("Error: Bitrate invalid! Please enter in a bitrate between 8 and 96kbps.")
        else:
            await ctx.send("Error: Sorry, but this command only works on voice channels!")

def setup(client):
    client.add_cog(Bitrate(client))
