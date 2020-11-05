import discord
import asyncio
from discord.ext import commands
class Webhooks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def webhooks(self, ctx, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)

        if (channel == None):
            await ctx.send("Channel not found.")
            return

        permission = channel.permissions_for(ctx.author)
        permission2 = channel.permissions_for(ctx.guild.me)

        if permission.manage_channels != True:
            await ctx.send('Error: You do not have the required permission: *Manage channels* for this command!')
        elif permission2.manage_channels != True:
            await ctx.send('Error: I not have the required permission: *Manage channels* for this command!')
        elif permission.manage_webhooks != True:
            await ctx.send('Error: You do not have the required permission: *Manage webhooks* for this command!')
        elif permission2.manage_webhooks != True:
            await ctx.send('Error: I not have the required permission: *Manage webhooks* for this command!')
        elif isinstance(channel, discord.TextChannel):
            await ctx.send(f"List of webhooks in {channel.name}:")
            hooks = await channel.webhooks()
            if len(hooks) == 0:
                await ctx.send("No webhooks!")
            else:
                for webhook in hooks:
                    await ctx.send(f"Name: {webhook.name} ID: {webhook.id}")
        else:
            await ctx.send("Sorry, this command only works for text channels!")


    @commands.command()
    async def delwebhook(self, ctx, webhookid: int=1, targetid: int=1):
        channel = None
        if targetid == 1:
            channel = ctx.channel
        else:
            await self.client.wait_until_ready()
            channel = self.client.get_channel(targetid)

        if (channel == None):
            await ctx.send("Channel not found.")
            return

        permission = channel.permissions_for(ctx.author)
        permission2 = channel.permissions_for(ctx.guild.me)

        if permission.manage_channels != True:
            await ctx.send('Error: You do not have the required permission: *Manage channels* for this command!')
        elif permission2.manage_channels != True:
            await ctx.send('Error: I not have the required permission: *Manage channels* for this command!')
        elif permission.manage_webhooks != True:
            await ctx.send('Error: You do not have the required permission: *Manage webhooks* for this command!')
        elif permission2.manage_webhooks != True:
            await ctx.send('Error: I not have the required permission: *Manage webhooks* for this command!')
        elif isinstance(channel, discord.TextChannel):
            hooks = await channel.webhooks()
            if len(hooks) == 0:
                await ctx.send("No webhooks in this channel!")
            else:
                for webhook in hooks:
                    if webhook.id == webhookid:
                        await ctx.send("Webhook found and deleted!")
                        await webhook.delete();
                        return;
                await ctx.send("Webhook not found! Run w.webhooks to get a list of webhooks and their IDs!")
        else:
            await ctx.send("Sorry, this command only works for text channels!")


def setup(client):
    client.add_cog(Webhooks(client))
