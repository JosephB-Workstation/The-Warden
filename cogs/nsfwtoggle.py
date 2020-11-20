import discord
import asyncio
from discord.ext import commands

class NSFW(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def nsfw(self, ctx, targetid: int=1):
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
            toggle = channel.nsfw
            if (toggle):
                await channel.edit(nsfw=False)
                await ctx.send(f"**{channel.name}** is no longer marked as NSFW!")
            else:
                await channel.edit(nsfw=True)
                await ctx.send(f"**{channel.name}** is now marked as NSFW!")
        else:
            await ctx.send("Error: Sorry, this command only works on text channels!")


def setup(client):
    client.add_cog(NSFW(client))
