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

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_guild=True)
    async def cafkch(self, ctx, targetid: int=1):
        guild = ctx.guild
        channelID = str(targetid)
        await self.client.wait_until_ready()
        channel = self.client.get_channel(targetid)
        if isinstance(channel, discord.VoiceChannel):
            await guild.edit(afk_channel=channel)
            await ctx.send(f"Server inactive channel changed to **{channel.name}**!")
        else:
            await ctx.send("Error: Sorry, but this command requires the ID of a voice channel!")

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_guild=True)
    async def cafktime(self, ctx, seconds):
        guild = ctx.guild
        time = None
        code = None
        if seconds == "1min":
            time = int(60)
            code = str("1 Minute")
        elif seconds == "5min":
            time = int(300)
            code = str("5 Minutes")
        elif seconds == "15min":
            time = int(900)
            code = str("15 Minutes")
        elif seconds == "30min":
            time = int(1800)
            code = str("30 Minutes")
        elif seconds == "1hour":
            time = int(3600)
            code = str("1 Hour")

        if time != None:
            await guild.edit(afk_timeout=time)
            await ctx.send(f"Afk channel timeout set to **{code}**")
        else:
            await ctx.send("Invalid time! Please see w.help cafktime for valid time entries!")



    @csname.error
    async def csname_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

    @cregion.error
    async def cregion_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

    @cafkch.error
    async def cafkch_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

    @cafktime.error
    async def cafktime_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

def setup(client):
    client.add_cog(GuildEdit(client))
