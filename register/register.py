from discord.ext import commands
from discord import Embed
from .utils import checks
from .utils.dataIO import dataIO
import os

class register():
    def __init__(self, bot):
      self.bot=bot

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
    n = register(bot)
    bot.add_listener(n.server_join, "on_server_join")
    bot.add_cog(n)
