import discord
from discord import embeds
from discord.ext import commands
from os import name
from discord.ext.commands import cog
import aiohttp
import requests

class random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.data = None
        self.embed = None


    @commands.command(name = "cat")
    async def random_cat(self, ctx):
        r = requests.get("http://aws.random.cat/meow") 
        data = r.json()
        embed = discord.Embed(title="Meow")
        embed.set_image(url=data["file"])
        embed.set_footer(text="http://random.cat/meow")
        await ctx.send(embed=embed)


    @commands.command(name = "dog")
    async def random_dog(self, ctx):
        r = requests.get("https://random.dog/woof.json") 
        data = r.json()
        embed = discord.Embed(title="Woof")
        embed.set_image(url=data["url"])
        embed.set_footer(text="http://random.dog/")
        await ctx.send(embed=embed)
