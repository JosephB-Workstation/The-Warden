import discord
import asyncio
from discord.ext import commands

class Del_inv(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def delinv (self, ctx):
        list = await ctx.guild.invites()
        count = 0
        for invite in list:
            await invite.delete()
            count = count + 1
        await ctx.send(f'**{count}** invites were removed from the server')

def setup(client):
    client.add_cog(Del_inv(client))
