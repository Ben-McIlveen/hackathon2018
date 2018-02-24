from discord.ext import commands
from discord import Embed
from .utils import checks
from .utils.dataIO import dataIO
import os

class register():
    def __init__(self, bot):
        self.bot=bot
        
        
    async def register(self,user):
        prv_channel = await self.bot.start_private_message(user)
        await self.bot.send_message(prv_channel, "Welcome to {user.server}! Please tell us what company you work for - ".format(user))
        msg = await self.bot.wait_for_message(timeout=120, channel = prv_channel, author = user).lower()
        role.append(await self.get_role(user.server, msg.content))
        
        if role[0] is None:
            role[0] = await self.make_role(user.server, msg.content).lower()
        
        await self.bot.send_message(prv_channel, "What skills do you have? (type `exit` to finish)")
        while role[:-1] is not None:
            msg = await self.bot.wait_for_message(timeout=120, channel = prv_channel, author = user).lower()
            if msg.content != "exit" or msg.content is not None:
                role.append(msg.content)
            else: role.append(None)
        
        for x in role[0:-2]:
            role_to_add = await self.get_role(user.server, x)
            if role_to_add is None:
                await self.make_role(user.server, x)
        
    async def get_role(self,server,role):
        roles = set(ctx.message.server.roles)
        for role in roles:
            if role.id == role_id:
                return role
        return None

def check_folders(): #Creates a folder
    if not os.path.exists("data/hackathon"):
        print("Creating data/hackathon")
        os.makedirs("data/hackathon")

def check_files(): #Creates json files in the folder
    if not dataIO.is_valid_json("data/hackathon/register.json"):
        print("Creating empty settings.json...")    
        dataIO.save_json("data/hackathon/register.json", {})
  
def setup(bot):
    check_folders()
    check_files()
    n = register(bot)
    bot.add_listener(n.register, "on_member_join")
    bot.add_cog(n)
