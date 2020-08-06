import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    

    @commands.command()
    async def Gachi(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def 千花(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send('⣿⣿⣟⣽⣿⣿⣿⣿⣟⣵⣿⣿⣿⡿⣳⣫⣾⣿⣿⠟⠻⣿⣿⣿⢻⣿⣿⣿⣿⣷⡽⣿ ⣿⣟⣾⡿⣿⣿⢟⣽⣿⣿⣿⣿⣫⡾⣵⣿⣿⣿⠃⠄⠄⠘⢿⣿⣾⣿⣿⣿⢿⣿⣿⡜ ⡿⣼⡟⣾⣿⢫⣿⣿⣿⣿⡿⣳⣿⣱⣿⣿⣿⡋⠄⠄⠄⠄⠄⠛⠛⠋⠁⠄⠄⣿⢸⣿ ⢳⣟⣼⡿⣳⣿⣿⣿⣿⡿⣹⡿⣃⣿⣿⣿⢳⠁⠄⠄⠄⢀⣀⠄⠄⠄⠄⠄⢀⣿⢿⣿ ⡟⣼⣿⣱⣿⡿⣿⣿⣿⢡⣫⣾⢸⢿⣿⡟⣿⣶⡶⢰⣿⣿⣿⢷⠄⠄⠄⠄⢼⣿⣸⣿ ⣽⣿⢣⣿⡟⣽⣿⣿⠃⣲⣿⣿⣸⣷⡻⡇⣿⣿⢇⣿⣿⣿⣏⣎⣸⣦⣠⡞⣾⢧⣿⣿ ⣿⡏⣿⡿⢰⣿⣿⡏⣼⣿⣿⡏⠙⣿⣿⣤⡿⣿⢸⣿⣿⢟⡞⣰⣿⣿⡟⣹⢯⣿⣿⣿ ⡿⢹⣿⠇⣿⣿⣿⣸⣿⣿⣿⣿⣦⡈⠻⣿⣿⣮⣿⣿⣯⣏⣼⣿⠿⠏⣰⡅⢸⣿⣿⣿ ⡀⣼⣿⢰⣿⣿⣇⣿⣿⡿⠛⠛⠛⠛⠄⣘⣿⣿⣿⣿⣿⣿⣶⣿⠿⠛⢾⡇⢸⣿⣿⣿ ⠄⣿⡟⢸⣿⣿⢻⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⠉⣠⣴⣾⣿⡇⣸⣿⣿⡏ ⠄⣿⡇⢸⣿⣿⢸⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠘⢿⣿⠏⠄⣿⣿⣿⣹ ⠄⢻⡇⢸⣿⣿⠸⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣦⣼⠃⠄⢰⣿⣿⢯⣿ ⠄⢸⣿⢸⣿⣿⡄⠙⢿⣿⣿⡿⠁⠄⠄⠄⠄⠉⣿⣿⣿⣿⣿⣿⡏⠄⢀⣾⣿⢯⣿⣿ ⣾⣸⣿⠄⣿⣿⡇⠄⠄⠙⢿⣀⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣿⠟⠄⠄⣼⡿⢫⣻⣿⣿ ⣿⣿⣿⠄⢸⣿⣿⠄⠄⠄⠄⠙⠿⣷⣶⣤⣴⣿⠿⠿⠛⠉⠄⠄⢸⣿⣿⣿⣿⠃⠄⢀⣴')
   
    @commands.command()
    async def takeitboy(self, ctx):
        random_boi = random.choice(jdata['url_boi'])
        await ctx.send(random_boi)

    @commands.command()
    async def dice(self, ctx ,num=int):
        randomdice = random.randint(1,limit=num)  
        await ctx.send(randomdice)
    

def setup(bot):
    bot.add_cog(React(bot))
