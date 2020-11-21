import discord
import asyncio
from discord.ext import commands

class ContentFilter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_guild=True)
    async def cfilter(self, ctx, filterLevel="disabled"):
        guild = ctx.guild
        if filterLevel == "0":
            await guild.edit(explicit_content_filter=discord.ContentFilter["disabled"])
            await ctx.send(f"Guild content filter set to **Disabled**!")
        elif filterLevel == "1":
            await guild.edit(explicit_content_filter=discord.ContentFilter["no_role"])
            await ctx.send(f"Guild content filter set to **No Role**!")
        elif filterLevel == "2":
            await guild.edit(explicit_content_filter=discord.ContentFilter["all_members"])
            await ctx.send(f"Guild content filter set to **All Members**!")
        elif filterLevel == "disabled" or filterLevel == "no_role" or filterLevel == "all_members":
            await guild.edit(explicit_content_filter=discord.ContentFilter[filterLevel])
            await ctx.send(f"Guild content filter set to **{filterLevel}**!")
        else:
            await ctx.send("Invalid content filter! See \"w.help cfilter\" for valid entries!")

    @cfilter.error
    async def cfilter_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Manage Server* for this command!')

def setup(client):
    client.add_cog(ContentFilter(client))
