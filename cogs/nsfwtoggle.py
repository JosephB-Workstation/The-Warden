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

        if isinstance(channel, discord.TextChannel):
            toggle = channel.nsfw
            if (toggle):
                await channel.edit(nsfw=False)
                await ctx.send(f"**{channel.name}** is no longer marked as NSFW!")
            else:
                await channel.edit(nsfw=True)
                await ctx.send(f"**{channel.name}** is now marked as NSFW!")
        else:
            await ctx.send("Error: Sorry, but this command only works on text channels!")


def setup(client):
    client.add_cog(NSFW(client))
