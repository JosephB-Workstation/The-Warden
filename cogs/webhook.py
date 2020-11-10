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
            msg = None
            hooks = await channel.webhooks()
            if len(hooks) == 0:
                msg = discord.Embed(title=f"Error!", description=f"No webhooks in text channel {channel.name}", color=0x8a0707)
            else:
                msg = discord.Embed(title=f"Webhooks for {channel.name}", description="List of webhooks:", color=0x4e5d94)
                for webhook in hooks:
                    msg.add_field(name=f"Name: {webhook.name}", value=f"*ID: {webhook.id}*", inline=False)
            await ctx.send(embed=msg)
        else:
            await ctx.send("Sorry, this command only works for text channels!")


    @commands.command()
    async def hookurls(self, ctx, targetid: int=1):
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
            msg = None
            if len(hooks) == 0:
                msg = discord.Embed(title=f"Error!", description=f"No webhooks in text channel {channel.name}", color=0x8a0707)
            else:
                msg = discord.Embed(title=f"Webhooks for {channel.name}", description="List of webhooks:", color=0x4e5d94)
                for webhook in hooks:
                    msg.add_field(name=f"Name: {webhook.name}", value=f"*URL: {webhook.url}*", inline=False)
            await ctx.send(embed=msg)
        else:
            await ctx.send("Sorry, this command only works for text channels!")


    @commands.command()
    async def delhook(self, ctx, webhookid: int=1, targetid: int=1):
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
                        await ctx.send(f"Webhook **{webhook.name}** found and deleted!")
                        await webhook.delete();
                        return;
                await ctx.send("Webhook not found! Run w.webhooks to get a list of webhooks and their IDs!")
        else:
            await ctx.send("Sorry, this command only works for text channels!")

    @commands.command()
    async def purgehooks(self, ctx, targetid: int=1):
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
                await ctx.send("No webhooks!")
            else:
                await ctx.send(f"Deleted **{len(hooks)}** webhooks from **{channel.name}**")
                for webhook in hooks:
                    await webhook.delete()
        else:
            await ctx.send("Sorry, this command only works for text channels!")

    @commands.command()
    async def addhook(self, ctx, name="Fresh Webhook", targetid: int=1):
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
            strname = str(name)
            webhook = await channel.create_webhook(name=strname)
            msg = discord.Embed(title=f"Webhook {webhook.name} created!", description=f"ID: {webhook.id}", color=0x4e5d94)
            await ctx.send(embed=msg)



def setup(client):
    client.add_cog(Webhooks(client))
