import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, filter: str=" "):
        msg = None
        filter = filter.lower();
        if filter == " ":
            msg = discord.Embed(title="Warden Command Directory", description="**Run w.help <EntryName> for more information**", color=0x4e5d94)
            msg.add_field(name="channelmanagement", value="Category includes commands that helps modify and manage channels", inline=False)
            msg.add_field(name="servermanagement", value="Category that includes commands that helps manage your discord server", inline=False)
            msg.add_field(name="moderation", value="Category that includes commands that helps moderate the users in your server", inline=False)
            msg.add_field(name="Not sure how to get channel ID's for commands?", value="Run w.help ID for assistance!", inline=False)
        elif (filter == "channelmanagement" or filter == "channel_management" or filter == "channel management"):
            msg = discord.Embed(title="Help - Channel Management Category", color=0x4e5d94)
            msg.add_field(name="Carrots (< and >) seperate command arguments", value="You shouldn't include them in commands!", inline=False)
            msg.add_field(name="w.cname - change name", value="<\"Name in quotes\"> <Optional channel ID>", inline=False)
            msg.add_field(name="w.ctopic - change topic", value="<\"Topic in quotes\"> <Optional channel ID>", inline=False)
            msg.add_field(name="w.cslow - change slowmode", value="<Time in seconds> <Optional channel ID>", inline=False)
            msg.add_field(name="w.nsfw", value="<Optional channel ID>", inline=False)
            msg.add_field(name="w.bitrate", value="<Bitrate between 8-96 in kbps> <Mandatory channel ID>", inline=False)
            msg.add_field(name="w.userlimit", value="<User count between 0-99> <Mandatory channel ID>", inline=False)
            msg.add_field(name="w.webhooks", value="<Optional Channel ID>", inline=False)
            msg.add_field(name="w.hookurls - webhook urls", value="<Optional Channel ID>", inline=False)
            msg.add_field(name="w.addhook - add webhook", value="<\"Optional name in quotes\"> <Optional Channel ID>", inline=False)
            msg.add_field(name="w.delhook - delete webhook", value="<Webhook ID> <Optional Channel ID>", inline=False)
            msg.add_field(name="w.purgehooks - purge webhooks", value="<Optional Channel ID>", inline=False)
        elif (filter == "servermanagement" or filter == "server_management" or filter == "server management"):
            msg = discord.Embed(title="Help - Server Management Category", color=0x4e5d94)
            msg.add_field(name="Carrots (< and >) seperate command arguments", value="You shouldn't include them in commands!", inline=False)
            msg.add_field(name="w.delinv - delete invites", value="<No Arguments>", inline=False)
            msg.add_field(name="w.cverify - change verification", value="<VerificationLevel>", inline=False)
            msg.add_field(name="w.cfilter - change content filter", value="<FilterLevel>", inline=False)
            msg.add_field(name="w.csname - change server name", value="<\"New Server Name in quotes\">", inline=False)
            msg.add_field(name="w.cregion - change server region", value="<New Voice Region>", inline=False)
            msg.add_field(name="w.cafkch - change afk channel", value="<Voice channel ID>", inline=False)
            msg.add_field(name="w.cafktime - change afk timer", value="<Time Code>", inline=False)
        elif (filter == "moderation"):
            msg = discord.Embed(title="Help - Moderation Category", color=0x4e5d94)
            msg.add_field(name="Carrots (< and >) seperate command arguments", value="You shouldn't include them in commands!", inline=False)
            msg.add_field(name="w.clear", value="<Amount of messages to clear, default 500> <Optional channel ID>", inline=False)
            msg.add_field(name="w.changenick", value="<Member> <New Nickname>", inline=False)
            msg.add_field(name="w.lock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="w.unlock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="w.lockdown", value="<Optional channel ID>", inline=False)
            msg.add_field(name="w.unlockdown", value="<Optional channel ID>", inline=False)
        elif (filter == "w.changenick" or filter == "changenick" or filter == "change nick" or filter == "nickname"):
            msg = discord.Embed(title="Help - changenick command", color=0x4e5d94)
            msg.add_field(name="w.changenick", value="<Member> <New Nickname>", inline=False)
            msg.add_field(name="Description: ", value="Allows you to change nicknames of users.", inline=False)
            msg.add_field(name="Member: ", value="@ the user in question", inline=False)
            msg.add_field(name="New Nickname:", value="The new nickname the user should have", inline=False);
        elif (filter == "ID" or filter == "id" or filter == "i d" or filter == "i_d"):
            msg = discord.Embed(title="Help - How to get ID's on Desktop or Mobile ", color=0x4e5d94)
            msg.add_field(name="1) Enable developer mode", value="Go into your discord user settings, and under the appearance tab at the bottom, enable developer mode.", inline=False)
            msg.add_field(name="2) Right click a channel and click on \"Copy ID\" at the bottom", value="Webhook ID's are found with w.webhooks", inline=False)
            msg.add_field(name="Task complete", value="You can paste the channel ID where needed now.", inline=False)
        elif (filter == "w.cafktime" or filter == "cafktime" or filter =="inactive timer"):
            msg = discord.Embed(title="Help - cafktime command", color=0x4e5d94)
            msg.add_field(name="w.cafktime", value="<Time Code>", inline=False)
            msg.add_field(name="Description: ", value="Changes the afk/inactive timer of the server", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Server", inline=False)
            msg.add_field(name="Voice channel ID: ", value="The valid time code to change the afk timer to. Valid entries include: 1min, 5min, 15min, 30min, and 1hour", inline=False)
        elif (filter == "w.cafkch" or filter == "cafkch" or filter == "inactive channel"):
            msg = discord.Embed(title="Help - cafkch command", color=0x4e5d94)
            msg.add_field(name="w.cafkch", value="<Server voice channel ID>", inline=False)
            msg.add_field(name="Description: ", value="Changes the afk/inactive channel of the server", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Server", inline=False)
            msg.add_field(name="Voice channel ID: ", value="The ID of the channel you would like to be the new afk channel.", inline=False)
        elif (filter == "w.csname" or filter =="csname"):
            msg = discord.Embed(title="Help - csname command", color=0x4e5d94)
            msg.add_field(name="w.csname", value="<New Server Name>", inline=False)
            msg.add_field(name="Description:", value="Changes the name of the server", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Server", inline=False)
            msg.add_field(name="Name:", value="The new name for the server.", inline=False)
        elif (filter == "w.cregion" or filter =="cregion"):
            msg = discord.Embed(title="Help - cregion command", color=0x4e5d94)
            msg.add_field(name="w.cregion", value="<New Server Region>", inline=False)
            msg.add_field(name="Description:", value="Changes the voice region of the server", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Server", inline=False)
            msg.add_field(name="Region:", value="The voice region for the server.", inline=False)
            msg.add_field(name="Valid Regions:", value="us_west, us_south, us_east, us_central, sydney, south_korea, southafrica, singapore, russia, london, japan, india, hongkong, frankfurt, europe, eu_west, eu_central, dubai, brazil, amsterdam", inline=False)
        elif (filter == "w.webhooks" or filter == "webhooks"):
            msg = discord.Embed(title="Help - webhooks command", color=0x4e5d94)
            msg.add_field(name="w.webhooks", value="<Optional Channel ID>", inline=False)
            msg.add_field(name="Description:", value="Lists all webhooks present in a given channel", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channels and Manage Webhooks", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to see. If that is not set, it will read the webhooks of the current channel.", inline=False)
        elif (filter == "w.hookurls" or filter == "hookurls"):
            msg = discord.Embed(title="Help - hookurls command", color=0x4e5d94)
            msg.add_field(name="w.hookurls", value="<Optional Channel ID>", inline=False)
            msg.add_field(name="Description:", value="Lists all webhooks present in a given channel, with their urls", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channels and Manage Webhooks", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to see. If that is not set, it will read the webhooks of the current channel.", inline=False)
        elif (filter == "w.delhook" or filter == "delhook"):
            msg = discord.Embed(title="Help - delhook command", color=0x4e5d94)
            msg.add_field(name="w.delhook", value="<Webhook ID> <Optional Channel ID>", inline=False)
            msg.add_field(name="Description:", value="Deletes a webhook from a given channel.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channels and Manage Webhooks", inline=False)
            msg.add_field(name="Webhook ID:", value="The ID of the webhook to delete, found with w.webhooks", inline=False)
            msg.add_field(name="Optional Channel ID:", value="Channel ID is the channel id of the channel you want to delete a webhook from. If that is not set, it will delete a webhook from the current channel.", inline=False)
        elif (filter == "w.delhook" or filter == "delhook"):
            msg = discord.Embed(title="Help - addhook command", color=0x4e5d94)
            msg.add_field(name="w.addhook", value="<\"Optional name in quotes\"> <Optional Channel ID>", inline=False)
            msg.add_field(name="Description:", value="Creates a webhook in a given channel.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channels and Manage Webhooks", inline=False)
            msg.add_field(name="Optional name:", value="Name of the new webhook", inline=False)
            msg.add_field(name="Optional Channel ID:", value="Channel ID is the channel id of the channel you want to create a webhook in. If that is not set, it will create a webhook in the current channel.", inline=False)
        elif (filter == "w.purgehooks" or filter == "purgehooks"):
            msg = discord.Embed(title="Help - purgehooks command", color=0x4e5d94)
            msg.add_field(name="w.purgehooks", value="<Optional Channel ID>", inline=False)
            msg.add_field(name="Description:", value="Deletes all webhooks from a given channel", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channels and Manage Webhooks", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to purge webhooks from. If that is not set, it will purge the webhooks of the current channel.", inline=False)
        elif (filter == "w.cverify" or filter == "cverify" or filter == "verification"):
            msg = discord.Embed(title="Help - cverify command", color=0x4e5d94)
            msg.add_field(name="w.cverify", value="<VerificationLevel>", inline=False)
            msg.add_field(name="Description:", value="Changes the necessary verification level of your server.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Server", inline=False)
            msg.add_field(name="Level:", value="The level of verification you want to lock chat messages on the server behind", inline=False)
            msg.add_field(name="Valid values:", value="none, low, medium, high, table_flip, extreme, double_table_flip, very_high, or highest.")
        elif (filter == "w.cfilter" or filter == "cfilter" or filter == "filter"):
            msg = discord.Embed(title="Help - cfilter command", color=0x4e5d94)
            msg.add_field(name="w.cfilter", value="<FilterLevel>", inline=False)
            msg.add_field(name="Description:", value="Deletes a given number of messages from a text channel", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Server", inline=False)
            msg.add_field(name="Level:", value="The level of content filtering you'd like on your server", inline=False)
            msg.add_field(name="Valid values:", value="disabled, no_role, or all_members")
        elif (filter == "w.clear" or filter == "clear"):
            msg = discord.Embed(title="Help - clear command", color=0x4e5d94)
            msg.add_field(name="w.clear", value="<Amount of messages> <Optional Channel ID>", inline=False)
            msg.add_field(name="Description:", value="Deletes a given number of messages from a text channel", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Messages and Read Message History", inline=False)
            msg.add_field(name="Amount:", value="Amount of messages to clear from a channel, defaults at 500", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to delete messages from. If that is not set, it will delete messages from the current channel.", inline=False)
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
        elif (filter == "w.cslow" or filter == "cslow" or filter == "slowmode"):
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
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to change. If that is not set, it will change the nsfw state of the current channel.", inline=False)
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
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to lock. If that is not set, it will lock the current channel.", inline=False)
        elif (filter == "w.unlock" or filter == "unlock"):
            msg = discord.Embed(title="Help - unlock command", color=0x4e5d94)
            msg.add_field(name="w.unlock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Unlocks a given channel, allowing everyone without an explicit block to send messages or speak.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel and Manage Permissions", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to unlock. If that is not set, it will unlock the current channel.", inline=False)
        elif (filter == "w.lockdown" or filter == "lockdown"):
            msg = discord.Embed(title="Help - lock command", color=0x4e5d94)
            msg.add_field(name="w.lockdown", value="<Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Locksdown a given channel, preventing everyone without a bypass from seeing the channel in question", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel and Manage Permissions", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to lockdown. If that is not set, it will lockdown the current channel.", inline=False)
        elif (filter == "w.unlockdown" or filter == "unlockdown"):
            msg = discord.Embed(title="Help - unlockdown command", color=0x4e5d94)
            msg.add_field(name="w.unlock", value="<Optional channel ID>", inline=False)
            msg.add_field(name="Description:", value="Unlocksdown a given channel, allowing everyone without an explicit block to see a channel.", inline=False)
            msg.add_field(name="Permissions Needed: ", value="Manage Channel and Manage Permissions", inline=False)
            msg.add_field(name="Optional ID:", value="Channel ID is the channel id of the channel you want to unlockdown. If that is not set, it will unlockdown the current channel - if the bot can see it.", inline=False)
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
