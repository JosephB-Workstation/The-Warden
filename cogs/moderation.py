import discord
import asyncio
from discord.ext import commands
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.Member):
        if isinstance(target, discord.Member):
            if(target.top_role < ctx.author.top_role and target.top_role < ctx.guild.me.top_role):
                await ctx.send(f"**{str(target)}** has been kicked!");
                await ctx.guild.kick(target)
            elif (target.top_role < ctx.author.top_role and  (not target.top_role < ctx.guild.me.top_role)):
                await ctx.send("Error: I do not have a high enough role to kick this user")
            elif ((not target.top_role < ctx.author.top_role) and target.top_role < ctx.guild.me.top_role):
                await ctx.send("Error: You do not have a high enough role to kick this user")
            elif ( (not target.top_role < ctx.author.top_role) and  (not target.top_role < ctx.guild.me.top_role)):
                await ctx.send("Error: Neither you or I have a high enough role to kick this user.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, target: discord.Member):
        if isinstance(target, discord.Member):
            if(target.top_role < ctx.author.top_role and target.top_role < ctx.guild.me.top_role):
                await ctx.send(f"**{str(target)}** has been banned!");
                await ctx.guild.ban(target)
            elif (target.top_role < ctx.author.top_role and  (not target.top_role < ctx.guild.me.top_role)):
                await ctx.send("Error: I do not have a high enough role to ban this user")
            elif ((not target.top_role < ctx.author.top_role) and target.top_role < ctx.guild.me.top_role):
                await ctx.send("Error: You do not have a high enough role to ban this user")
            elif ( (not target.top_role < ctx.author.top_role) and  (not target.top_role < ctx.guild.me.top_role)):
                await ctx.send("Error: Neither you or I have a high enough role to ban this user.")

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def changenick(self, ctx, target: discord.Member, name):
        if isinstance(target, discord.Member):
            newname = str(name)
            if(target.top_role < ctx.author.top_role and target.top_role < ctx.guild.me.top_role):
                await ctx.send(f"**{target.display_name}** has had their nickname changed to **{newname}**");
                await target.edit(nick=newname)
            elif (target.top_role < ctx.author.top_role and  (not target.top_role < ctx.guild.me.top_role)):
                await ctx.send("Error: I do not have a high enough role to rename this user")
            elif ((not target.top_role < ctx.author.top_role) and target.top_role < ctx.guild.me.top_role):
                await ctx.send("Error: You do not have a high enough role to rename this user")
            elif ( (not target.top_role < ctx.author.top_role) and  (not target.top_role < ctx.guild.me.top_role)):
                await ctx.send("Error: Neither you or I have a high enough role to rename this user.")

    @ban.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Ban Members* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Ban Members* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Kick Members* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Kick Members* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')

    @changenick.error
    async def changenick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Nicknames* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Manage Nicknames* for this command!')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: You have reached the rate limit for this command. Apologies for the inconvienence. Please try again later.')


def setup(client):
    client.add_cog(Moderation(client))
