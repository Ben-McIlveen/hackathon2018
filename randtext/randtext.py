import discord, logging, os, random, string
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help

class randtext();
  def __init__(self,bot):
    self.bot=bot
    
  async def rand_response(self,message):
    random_number = random.randint(0,101)
    if random_number <=10:
      await self.bot.send_message(message.channel, "".join([random.choice(ascii.printable()) for x in range(random.randint(2,20))])
      
    if message.content.contains("rand") or message.content.contains("strange"):
      await self.bot.send_message(message.channel, "Mate - git go-"+".join([random.choice(ascii.printable()) for x in range(random.randint(2,20))])
      
def setup(bot):
  n=randtext(bot)
  bot.add_listener(n.rand_response, "on_message")
  bot.add_cog(n)
