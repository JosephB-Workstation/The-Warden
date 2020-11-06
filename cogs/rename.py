import discord
import asyncio
from discord.ext import commands

class Rename(commands.Cog):
    def __init__(self, client):
        self.client = client


    def nameChecker(self, ctx, channel, lowername, uppername):
        oldname = " "
        if channel != None:
            oldname = channel.name
        else:
            oldname = ctx.channel.name

        nameGood = True
        if isinstance(channel, discord.TextChannel):
            if oldname == lowername:
                nameGood = False
        else:
            if oldname == uppername:
                nameGood = False;
        return nameGood


    async def renamechannel(self, ctx, lowername, id:int, uppername):
        channel = None
        if int(id) == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(int(id))

        if(channel == None):
            await ctx.send("Channel not found.")
            return

        permission = channel.permissions_for(ctx.author)
        permission2 = channel.permissions_for(ctx.guild.me)

        if permission.manage_channels != True:
            await ctx.send('Error: You do not have the required permission: *Manage channels* for this command!')
        elif permission2.manage_channels != True:
            await ctx.send('Error: I not have the required permission: *Manage channels* for this command!')
        elif channel != None:
            if isinstance(channel, discord.TextChannel):
                if Rename.nameChecker(self, ctx, channel, lowername, uppername):
                    await ctx.send(f'The channel **{channel.name}** was renamed to **{lowername}**!')
                    await channel.edit(name=lowername)

                else:
                    await ctx.send(f'Sorry, but **{lowername}** is already the channel\'s name!')
            else:
                if Rename.nameChecker(self, ctx, channel, lowername, uppername):
                    await ctx.send(f'The channel **{channel.name}** was renamed to **{uppername}**!')
                    await channel.edit(name=uppername)
                else:
                    await ctx.send(f'Sorry, but **{uppername}** is already the channel\'s name!')

    @commands.command()
    async def cname(self, ctx, name, targetid: int=1):  #limited to 2 per channel per 10 minutes
        lowername = str(name)
        id = str(targetid)
        lowername = lowername.replace(' ', '-')
        lowername = lowername.lower()
        await asyncio.wait_for(Rename.renamechannel(self, ctx, lowername, id, name), 3)

    @cname.error
    async def cname_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: Each channel has 2 uses of name or description changes per 10 minutes. Apologies for the inconvienence!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Error: Name for channel not given!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('Error: Invalid channel ID')


def setup(client):
    client.add_cog(Rename(client))
