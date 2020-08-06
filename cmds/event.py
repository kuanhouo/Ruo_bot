import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_memeber_join(self, memeber):
        channel = self.bot.get_channel(int(jdata['gigi_channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_memeber_remove(self, memeber):
        channel = self.bot.get_channel(int(jdata['gigi_channel']))
        await channel.send(f'{member} leave!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'apple':
            await msg.channel.send('hi')


def setup(bot):
    bot.add_cog(Event(bot))
