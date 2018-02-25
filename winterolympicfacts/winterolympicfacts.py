from discord.ext import commands
from discord import Embed
from .utils import checks
from .utils.dataIO import dataIO
import os
import random
import time
timer=True
facts = ['Pyeongchang is the smallest city to host the winter games since 1994.', 'The Stadium cost $109 million to build!', 'The winter olympics started in 1924!', 'The four indoor Winter Sports are: Ice Hockey, Speed Skating, Figure Skating and Curling.', 'The oldest Olympic medalist was Anders Haugen who was 83 when he recieved his bronze medal for the ski jump.']

while timer=True:
  time.sleep(10)
  self.bot.say(facts[random.randint(0,len(facts)-1)])
  
@self.command(pass_context=True)  
async def marco(ctx):
  await self.say("POLO!")

@self.command(pass_context=True)
async def userinfo(ctx, user: Message):
  embed=discord.Embed(title="User"+user.name)
  
  
  
