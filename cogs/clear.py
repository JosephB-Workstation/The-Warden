import discord
import asyncio
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount: int=500, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)

        permission = channel.permissions_for(ctx.author)
        permission2 = channel.permissions_for(ctx.guild.me)

        if permission.manage_messages != True:
            await ctx.send("Error: You do not have reqired permission: *Manage Messages* for this command!")
        elif permission2.manage_messages != True:
            await ctx.send("Error: I do not have reqired permission: *Manage Messages* for this command!")
        elif permission.read_message_history != True:
            await ctx.send('Error: You do not have the required permission: *Read Message History* for this command!')
        elif permission2.read_message_history != True:
            await ctx.send('Error: I not have the required permission: *Read Message History* for this command!')
        elif isinstance(channel, discord.TextChannel):
            if amount > 1000:
                amount = 1000
            if amount < 1:
                amount = 1
            counter = amount + 1
            delamount = 0
            while (counter > 0):
                if counter >= 100:
                    messages = await channel.history(limit=100).flatten()
                    counter -= len(messages)
                    delamount += len(messages)
                    if len(messages) == 0:
                        amount = amount - counter
                        counter = 0
                    await channel.delete_messages(messages)
                else:
                    messages = await channel.history(limit=counter).flatten()
                    delamount += len(messages)
                    if len(messages) == 0:
                        amount = amount - counter
                        counter = 0
                    await channel.delete_messages(messages)
                    counter = 0
            await ctx.send(f'Deleted **{delamount}** messages from **{channel.name}** for **{str(ctx.author)}**!')
        else:
            await ctx.send("Error: Sorry, this command only works in text channels!")


def setup(client):
    client.add_cog(Clear(client))
