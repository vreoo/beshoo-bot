import discord
from discord.ext import commands
from discord import Permissions


class Administration(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def kick(self,ctx, member: discord.Member, *, why=None):
        await member.kick(reason=why)
        await ctx.channel.send(f"**{member} has been kicked from this server by {ctx.author}**")


    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send("Looks like you don't have the perm.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self,ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            await member.add_roles(role)
            await ctx.send(f"{member} was muted.")
        else:
            await member.add_roles(role) 
            await ctx.send(f"{member} was muted.")     

    @mute.error
    async def mute_error(self,ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("You are not an admin") 
        elif isinstance(error, commands.BadArgument):
            await ctx.send("That is not a valid member") 

    

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban (self,ctx, member:discord.User=None, reason =None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
        if reason == None:
            reason = "For being a jerk!"
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member.mention} is banned! :hammer: :hammer: :hammer:")
        await member.send(message)

    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the premissions to do that") 
        elif isinstance(error, commands.BadArgument):
            await ctx.send("That is not a valid member") 

    