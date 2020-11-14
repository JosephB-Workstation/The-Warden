import discord
import asyncio
from discord.ext import commands

class Verification(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_guild=True)
    async def cverify(self, ctx, verificationlevel="none"):
        guild = ctx.guild
        if verificationlevel == "highest":
            await guild.edit(verification_level=discord.VerificationLevel["very_high"])
            await ctx.send("Guild verification level set to **Highest**")
        elif verificationlevel == "none" or verificationlevel == "low" or verificationlevel == "medium" or verificationlevel == "high" or verificationlevel == "table_flip" or verificationlevel == "extreme" or verificationlevel == "double_table_flip" or verificationlevel == "very_high":
            await guild.edit(verification_level=discord.VerificationLevel[verificationlevel])
            await ctx.send(f"Guild verification level set to **{verificationlevel}**!")
        else:
            await ctx.send("Invalid verification level! See \"w.help cverify\" for valid entries!")

    @cverify.error
    async def cverify_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Error: You do not have the required permission: *Manage Server* for this command!')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send('Error: I do not have the required permission: *Manage Server* for this command!')
def setup(client):
    client.add_cog(Verification(client))
