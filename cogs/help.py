import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, filter: str=" "):
        msg = None
        if filter == " ":
            msg = discord.Embed(title="Warden Commands", description="**Run w.help <CommandName> for more information**", color=0x4e5d94)
            msg.add_field(name="w.cname", value="<\"Name in quotes\"> <Optional channel ID>", inline=False)
            msg.add_field(name="w.ctopic", value="<\"Topic in quotes\"> <Optional channel ID>", inline=False)
            msg.add_field(name="w.cslow", value="<Time in seconds> <Optional channel ID>", inline=False)
            msg.add_field(name="w.nsfw", value="<Optional channel ID>", inline=False)
            msg.add_field(name="w.bitrate", value="<Bitrate between 8-96 in kbps> <Mandatory channel ID>", inline=False)
            msg.add_field(name="w.userlimit", value="<User count between 0-99> <Mandatory channel ID>", inline=False)
            msg.add_field(name="w.lock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="w.unlock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="w.delinv", value="<No Arguments>", inline=False)
        elif (filter == "w.cname" or filter == "cname"):
            msg = discord.Embed(title="Help - cname command", color=0x4e5d94)
            msg.add_field(name="w.cname", value="<\"Name in quotes\"> <Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Renames a channel, this combined with ctopic have a 2 use limit per channel per 10 minutes.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel", inline=False)
            msg.add_field(name="Name:", value="Name is the desired name of the channel.", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to change. If that is not set, it will change the name of the current channel.", inline=False)
        elif (filter == "w.ctopic" or filter == "ctopic"):
            msg = discord.Embed(title="Help - ctopic command", color=0x4e5d94)
            msg.add_field(name="w.ctopic", value="<\"Topic in quotes\"> <Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Changes text channel topic, this combined with cname has a 2 use limit per channel per 10 minutes.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel", inline=False)
            msg.add_field(name="Topic:", value="Topic is the desired topic of the text channel", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to change. If that is not set, it will change the topic of the current channel.", inline=False)
        elif (filter == "w.cslow" or filter == "cslow"):
            msg = discord.Embed(title="Help - cslow command", color=0x4e5d94)
            msg.add_field(name="w.cslow", value="<Time in seconds> <Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Changes text channel slow mode timer.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel", inline=False)
            msg.add_field(name="Time:", value="The time in seconds you would like slow mode to be applied for.", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to change. If that is not set, it will change the slow mode of the current channel.", inline=False)
        elif (filter == "w.nsfw" or filter == "nsfw"):
            msg = discord.Embed(title="Help - nsfw command", color=0x4e5d94)
            msg.add_field(name="w.nsfw", value="<Optional channel ID>", inline=False)
            msg.add_field(name="Description: ", value="Toggles NSFW mode on text channels", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to change. If that is not set, it will change the slow mode of the current channel.", inline=False)
        elif (filter == "w.bitrate" or filter == "bitrate"):
            msg = discord.Embed(title="Help - bitrate command", color=0x4e5d94)
            msg.add_field(name="w.bitrate", value="<Bitrate between 8-96 in kbps> <Mandatory channel ID>", inline=False)
            msg.add_field(name="Description: ", value="Changes a voice channel's bitrate, effecting audio quality and bandwith usage.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel", inline=False)
            msg.add_field(name="Bitrate: ", value="A value between 8 and 96 that represents the bitrate you would like your voice channel to have in kbps.", inline=False)
            msg.add_field(name="Channel ID: ", value="Identifies the voice channel you'd like the bot to edit. The command will fail without it.")
        elif (filter == "w.userlimit" or filter == "userlimit"):
            msg = discord.Embed(title="Help - userlimit command", color=0x4e5d94)
            msg.add_field(name="w.userlimit", value="<User count between 0-99> <Mandatory channel ID>", inline=False)
            msg.add_field(name="Description: ", value="Changes the user limit of a voice channel", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel", inline=False)
            msg.add_field(name="User Limit: ", value="A value between 0 and 99 that represents the maximum amount of people you want in a voice channel, 0 being unlimited.", inline=False)
            msg.add_field(name="Channel ID: ", value="Identifies the voice channel you'd like the bot to edit. The command will fail without it.")
        elif (filter == "w.lock" or filter == "lock"):
            msg = discord.Embed(title="Help - lock command", color=0x4e5d94)
            msg.add_field(name="w.lock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Locks a given channel, preventing everyone without a bypass from sending messages or speaking.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel and Manage Permissions", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to change. If that is not set, it will change the slow mode of the current channel.", inline=False)
        elif (filter == "w.unlock" or filter == "unlock"):
            msg = discord.Embed(title="Help - unlock command", color=0x4e5d94)
            msg.add_field(name="w.unlock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Unlocks a given channel, allowing everyone without an explicit block to send messages or speak.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel and Manage Permissions", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to change. If that is not set, it will change the slow mode of the current channel.", inline=False)
        elif (filter == "w.delinv" or filter == "delinv"):
            msg = discord.Embed(title="Help - delinv command", color=0x4e5d94)
            msg.add_field(name="w.delinv", value="<No Arguments>", inline=False)
            msg.add_field(name="Description", value="Bulk deletes invites from your server.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Server", inline=False)
        else:
            msg = discord.Embed(title="Help - ERROR", description="No entries matching your help query were found!", color=0x8a0707)
        await ctx.send(embed=msg)

def setup(client):
    client.add_cog(Help(client))
