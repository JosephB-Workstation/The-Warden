import discord
import asyncio
from discord.ext import commands
class GuildEdit(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def rename(self, ctx, newname, guildname):
        await ctx.guild.edit(name=newname)
        await ctx.send(f"Server renamed from **{guildname}** to **{newname}**")

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_guild=True)
    async def servername(self, ctx, name):
        newname = str(name)
        guildname = (ctx.guild.name)
        if newname != guildname:
            await asyncio.wait_for(GuildEdit.rename(self, ctx, newname, guildname), 3)

    @servername.error
    async def servername_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

def setup(client):
    client.add_cog(GuildEdit(client))
