from discord.ext import commands
from discord import Embed
from .utils import checks
from .utils.dataIO import dataIO
import random
rand=random.randint
factrue = True

@self.command(pass_context=True)  
async def marco(ctx):
  await self.say("POLO!")

@self.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
  embed=discord.Embed(title="User {}'s info".format(user.name), description = "Here's what I found!", color=0x1971ff)
  embeded.add_field(name="Name", value= user.name, inline=True)
  embeded.add_field(name="ID", vlaue= user.id, inline=True)
  embeded.add_field(name="Status",value= user.status, inline=True)
  embeded.add_field(name="Highest Role", value=user.role_top, inline=True)
  embeded.add_field(name="Lowest Role",value=user.role_bottom,inline=True)
  embeded.add_field(name="Joined",value=user.joined_at,inline=True)
  embeded.set_thumbnail(url=user.avatar_url)
  await self.say(embeded = embeded)
  
@self.command(pass_context=True)
async def severinfo(ctx)
embeded=discord.Embeded(title="Server {}'s info".format(ctx.message.server.name), description="Here's what I found!", color=0xff8d3d)
embeded.add_field(name="Server Name:", value = ctx.message.server.name, inline=True)
embeded.add_field(name="Server ID:", value = ctx.message.server.id, inline = True)
embeded.add_field(name="Companies:", value = ctx.len(message.server.roles), inline=True)
embeded.add_field(name="Members:", value = ctx.len(message.server.members), inline=True)
embeded.set_thumbnail(url=ctx.server.icon_url)
await self.say(embeded= embeded)

@self.command(pass_context=True)
async def randomworldfacts(ctx):
  world=["In Japan, you can hire a handsome man to watch sappy movies with you and wipe away your tears.", "In China, any TV shows and films featuring time travel are censored.", " Ethiopia follows a calendar that is seven years behind the rest of the world.","In Denmark, citizens have to select baby names from a list of 7,000 government-approved names.", "In Singapore, selling, importing or spitting out chewing gum is illegal.", "In France, you can marry a dead person.", "In Niue, an island nation in the South Pacific, its coins feature Disney and “Star Wars” characters.", "In Russia, authorities proposed to ban all things “emo” because they were declared a threat to national stability.",]
  while factrue == True:
    time.sleep(120)
    await self.say(world[0,len(world)-1])
  

  
  
  
  
