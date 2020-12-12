import discord
from discord.ext import commands


class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, user:discord.Member):
        muted_role = discord.utils.find(lambda r: r.name.upper() == 'MUTED', ctx.guild.roles)
        if muted_role:
            await user.add_roles(muted_role)
            await ctx.send(f"{user} has been muted!")
        else:
            await ctx.send("Couldn't find a role with 'muted' in the name.")

def setup(client):
    client.add_cog(AdminCommands(client))