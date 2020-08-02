import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
bot= commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("bot is online")

@bot.event
async def on_memeber_join(memeber):
    channel = bot.get_channel(int(jdata['gigi_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_memeber_remove(memeber):
    channel = bot.get_channel(int(jdata['gigi_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loading {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loading {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loading {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])


