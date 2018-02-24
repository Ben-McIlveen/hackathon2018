from discord.ext import commands
from discord import Embed
from .utils import checks
from .utils.dataIO import dataIO
import os

class search():
  def __init__(self.bot):
    self.bot = bot
  @commands.command(pass_context = True)
  async def Search(self, ctx, role_name):
    await self.bot.say("command correct")
    a = ctx.server.roles
    for users in role:
      await self.bot.say(users)
      
def check_folders(): #Creates a folder
    if not os.path.exists("data/"):
        print("Creating data/hackathon")
        os.makedirs("data/hackathon")

def check_files(): #Creates json files in the folder
    if not dataIO.is_valid_json("data/hackathon/settings.json"):
        print("Creating empty settings.json...")    
        dataIO.save_json("data/hackathon/settings.json", {})
  
def setup(bot):
    check_folders()
    check_files()
    n = search(bot)
    bot.add_listener(n.server_join, "on_server_join")
    bot.add_cog(n)
