from discord.ext import commands
from discord import Embed
from .utils import checks
from .utils.dataIO import dataIO
import os, pymongo

class register():
    def __init__(self, bot):
        self.bot=bot  
        
    async def register(self,user):
        prv_channel = await self.bot.start_private_message(user)
        await self.bot.send_message(prv_channel, "Welcome to {user.server}! Please tell us what company you work for - ".format(user=user))
        msg = await self.bot.wait_for_message(timeout=120, channel = prv_channel, author = user)
        msg.content = msg.content.lower()
        role = [] #this is used for the string of role names to add
        if msg.content is not None:
            role.append(msg.content.lower())
        
        if role[0] is None:
            role[0] = await self.make_role(user.server, msg.content)
        
        await self.bot.send_message(prv_channel, "What skills/job role do you have? (type `exit` to finish)")
        while role[-1] is not None:
            msg = await self.bot.wait_for_message(timeout=60, channel = prv_channel, author = user)
            if msg is None:
                role.append(None)
            elif msg.content.lower() != "exit": role.append(msg.content.lower())
            else: role.append(None)

        if len(role) <= 2:
            return

        #Add max number of roles
        #Maybe add somekind of "verify role"
        #Maybe check agaisnt a list of "bad roles" (or just leave it to the mods XD)

        for x in role[0:-1]:
            role_to_add = await self.get_role(user.server, x)
            if role_to_add is None:
                role_to_add = await self.make_role(user.server, x)
            await self.bot.add_roles(user, role_to_add)
        
    async def get_role(self,server,role_name):
        roles = set(server.roles)
        for role in roles:
            if role.name == role_name:
                return role
        return None

    async def make_role(self,server,role_name):
        return await self.bot.create_role(server,name=role_name)

    @commands.command(pass_context=True, no_pm=True)
    async def registerRole(self,ctx,role):
        pass

    #@commands.group()

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
