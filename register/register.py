from discord.ext import commands
import discord
from .utils import checks
from .utils.dataIO import dataIO
import os

try:
    import pymongo
    from pymongo import MongoClient
    client =  MongoClient()
    db = client["challange-channels"]
except:
    raise RuntimeError("Could not load Database - Check the GIT docs for more info.")

class register():
    def __init__(self, bot):
        self.bot=bot  
        
    async def register(self,user, server=None):
        if server == None:
            server = user.server

        Details = {}
        roles = ["Filler"]
        Details["USER_ID"]=user.id

        Registed_role = await self.get_role(server, "registed")
        if Registed_role is None:
            Registed_role = await self.make_role(server, "registed")

        prv_channel = await self.bot.start_private_message(user)
        await self.bot.send_message(prv_channel, "Welcome to {0}! Please tell us what company you work for - ".format(server))
        msg = await self.bot.wait_for_message(timeout=120, channel = prv_channel, author = user)

        if msg is not None:
            Details["COMPANY"] = msg.content.lower()
            role = await self.get_role(server, msg.content.lower())
            if role is None:
                role = await self.make_role(server, msg.content)
            await self.bot.add_roles(user, role)

        else:
            Details["COMPANY"] = None
        
        await self.bot.send_message(prv_channel, "What skills/job role do you have? (type `exit` to finish)")
        while roles[-1] is not None:
            msg = await self.bot.wait_for_message(timeout=60, channel = prv_channel, author = user)
            if msg is None:
                roles.append(None)

            elif msg.content.lower() != "exit": roles.append(msg.content.lower())

            else: roles.append(None)

        if len(roles)<3:
            Details["ROLES"] = roles[:-2]
        
        if len(roles) < 3 or Details["COMPANY"]==None:
            await self.bot.send_message(prv_channel, "You have not been registered! Ask a mod to be registed")

        #Add max number of roles
        #Maybe add somekind of "verify role"
        #Maybe check agaisnt a list of "bad roles" (or just leave it to the mods XD)

        db.users.insert_one(Details)
        await self.bot.send_message(prv_channel, "You have now been registered!")
        await self.bot.add_roles(user, Registed_role)
    
    async def get_role(self,server,role_name):
        roles = set(server.roles)
        for role in roles:
            if role.name == role_name:
                return role
        return None

    async def make_role(self,server,role_name):
        return await self.bot.create_role(server,name=role_name)

    @commands.group(pass_context=True)
    @checks.serverowner_or_permissions(manage_channels=True)
    async def setregister(self,ctx):
        """Changes the settings for this cog, use with no sub command to get infomation on the cog, and current setings"""

    @setregister.command(pass_context=True)
    @checks.serverowner_or_permissions(manage_roles=True)
    async def reset(self,ctx, user: discord.Member):
        """Resets the members roles & settings"""
        await self.bot.send_message(user, "Your registration has been reset")
        await self.bot.say("Roles reset")
        db.users.update_one({"USER_ID": user.id},{'$set': {}}, upsert=False)
        await self.bot.remove_roles(user, self.get_role(server,"registed"))
        await self.bot.remove_roles(user, self.get_role(server, db.users.find_one({"USER_ID":user.id})["COMPANY"]))

    @setregister.command(pass_context=True)
    @checks.serverowner_or_permissions(manage_roles=True)
    async def forcereg(self, ctx, user:discord.Member):
        """Forces a user to register"""
        await self.register(user,ctx.message.server)
        
    @setregister.command(pass_context=True)
    @checks.serverowner_or_permissions(manage_roles=True)
    async def checkUser(self,ctx,user_id):
        user_info = db.users.find_one({"USER_ID":user_id})
        if user_info is None:
            await self.bot.say("No user with that ID has been registered")
            return
        
        user_obj = await self.bot.get_member(user_id)
        em = discord.Embed(title="{user.name} registration info".format(user=user_obj), colour = 0xff0000)
        em.add_field(name="Company", value=user_info["COMPANY"])
        em.add_field(name="Role(s)", value=", ".join(user_info["ROLES"]))
        em.add_field(name="Joined at:", value=user.joined_at())
        
        await self.bot.send_message(ctx.message.channel, embed=em)
        
    @setregister.command(pass_context=True)
    @checks.serverowner_or_permissions(manage_roles=True)
    async def removeRoles(self,ctx,role_name):
        users = db.users.find_many({"ROLES": {'$in': [role_name]}})
        count = 0
        for user in users:
            count += 1
            user["ROLES"].remove(role_name)
            db.users.update_one({"USER_ID":user["USER_ID"]}, {'$set': {"ROLES": user["ROLES"]}}, upset=False)
            
        await self.bot.say("{count} people have had the {role} removed!".format(count=count, role=role_name))
        
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
