import asyncio
import io
from os import getenv, path, makedirs

import aiohttp
import discord
from discord.ext import commands
from urllib import parse

from main import bot


class FunCommands(commands.Cog, name="Fun Commands"):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.random_channel = int(getenv("CHANNEL_RANDOM", 689534362760642676))
        self.mod_log = int(getenv("CHANNEL_MOD_LOG", 689216590297694211))

    @commands.command(aliases=['crabrave', 'crab_rave', 'crab-rave'], hidden=True)
    async def crab(self, ctx, *, text = None):
        if ctx.channel.id == self.random_channel:
            await ctx.message.delete()

            async with ctx.channel.typing():
                print("Downloading...")
                url = f'https://adventurous-damselfly.glitch.me/video/{parse.quote(text)}.mp4?style=classic'
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        if resp.status != 200:
                            return False
                        resp = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(resp, f'{text}.mp4'))
            # await self.bot.get_channel(self.mod_log).send(f"{ctx.author.mention} did crab rave with arguments '{text}'")
        else:
            await ctx.send("Sorry, please do that in #random")

    @commands.command(hidden=True)
    async def owo(self, ctx):
        if ctx.channel.id == self.random_channel:
            await ctx.send(f"owo what's {ctx.author.mention}")

    @commands.command()
    async def updownupdownleftrightleftrightbastart(self, ctx):
        if ctx.channel.id == self.random_channel:
            await ctx.send("wow that's a long cheat code")

    @commands.command()
    async def pledge(self, ctx):
        voice_channel = ctx.message.author.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel
            vc = await channel.connect()
            person = 'Zeke'
            source = discord.FFmpegPCMAudio('./audiofiles/Zeke.mp3')
            player = vc.play(source)
            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()


def setup(bot):
    bot.add_cog(FunCommands(bot))
