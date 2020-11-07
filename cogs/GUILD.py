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
    async def csname(self, ctx, name):
        newname = str(name)
        guildname = (ctx.guild.name)
        if newname != guildname:
            await asyncio.wait_for(GuildEdit.rename(self, ctx, newname, guildname), 3)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_guild=True)
    async def cregion(self, ctx, regions="us_east"):
        guild = ctx.guild
        region = str(regions)
        if region == "us_west" or region == "us_south" or region == "us_east" or region == "us_central" or region == "sydney" or region == "south_korea" or region == "southafrica" or region == "singapore" or region == "russia" or region == "london" or region == "japan" or region == "india" or region == "hongkong" or region == "frankfurt" or region == "europe" or region == "eu_west" or region == "eu_central" or region == "dubai" or region == "brazil" or region == "amsterdam":
            await guild.edit(region = discord.VoiceRegion[region])
            await ctx.send(f"Voice region changed to **{region}**")
        elif ((region == "vip_ampsterdam" or region == "vip_us_east" or region == "vip_us_west")):
            await ctx.send(f"Unfortunately, we do not support VIP region codes at the moment")
        else:
            await ctx.send("Region not found! run w.help cregion for a list of known regions!")


    @csname.error
    async def csname_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

    @cregion.error
    async def cregion_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

def setup(client):
    client.add_cog(GuildEdit(client))
