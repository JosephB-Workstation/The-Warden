import discord
import asyncio
from discord.ext import commands

class Redescribe(commands.Cog):
    def __init__(self, client):
        self.client = client

    def descriptionChecker(self, ctx, channel, description):
        olddesc = " "
        if isinstance(channel, discord.TextChannel):
            olddesc = channel.topic
        elif channel == None:
            olddesc = ctx.channel.topic
        if olddesc == " ":
            return True
        elif olddesc == description:
            return False
        else:
            return True

    async def describechannel(self, ctx, description, id: int):
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
        elif Redescribe.descriptionChecker(self, ctx, channel, description) != True:
            await ctx.send("New description matches old description!")
        elif channel != None:
            if isinstance(channel, discord.TextChannel):
                await channel.edit(topic=description)
                await ctx.send(f'**{channel.name}** has had it\'s topic changed!')
            else:
                await ctx.send("Voice channels do not have topics to edit!")


    @commands.command()
    async def ctopic(self, ctx, description, targetid: int=1):  #limited to 2 per channel per 10 minutes
        newdesc = str(description)
        id = str(targetid)
        await asyncio.wait_for(Redescribe.describechannel(self, ctx, newdesc, id), 1)

    @ctopic.error
    async def ctopic_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Error: Each channel has 2 uses of name or description changes per 10 minutes. Apologies for the inconvienence!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Error: Topic for channel not given!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('Error: Invalid channel ID')


def setup(client):
    client.add_cog(Redescribe(client))
