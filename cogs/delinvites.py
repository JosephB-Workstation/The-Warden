import discord
import asyncio
from discord.ext import commands

class Del_inv(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_guild=True)
    async def delinv (self, ctx):
        list = await ctx.guild.invites()
        count = 0
        for invite in list:
            await invite.delete()
            count = count + 1
        await ctx.send(f'**{count}** invites were removed from the server')

    @delinv.error
    async def delinv_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I not have the required permission: *Manage Server* for this command!')

def setup(client):
    client.add_cog(Del_inv(client))
