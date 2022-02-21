import os
import discord
from discord import channel
from discord.ext import commands, tasks
from discord.message import MessageReference
from webserver import keep_alive
import asyncio
from discord.colour import Colour
import dns
import time
import _thread
import datetime
from math import floor
from discord.colour import Colour
from discord.utils import get
import discord, asyncio
from discord.ext import commands
import statcord 
import requests


from pymongo import MongoClient
cluster=MongoClient("")
                
db=cluster["test"]
collections=db["test"]
db1=cluster["test1"]
collection=db1["test1"]
db2=cluster["test2"]
coll=db2["test2"]
db3=cluster["test3"]
co=db3["test3"]
db4=cluster["DailyReminder"]
dai=db4["DailyReminder"]
db5=cluster["UserRemind"]
use=db5["UserRemind"]
db6=cluster["custom"]
cus=db6["custom"]
db7=cluster["history"]
his=db7["history"]
db8=cluster["delete"]
de=db8["delete"]
ede=db8["edelete"]
db9=cluster["prefix"]
pre=db9["prefix"]
cnt=db3["count"]
c = discord.Client()
a=[]
rem=[]


def get_prefix(b,message) :
  cursor=pre.find({})
  flag=0
  for p in cursor :
     if p["Gid"] == str(message.guild.id) :
       flag=1
       return str(p["prefix"])
  if flag==0 :
      return "u."

b = commands.Bot(command_prefix=get_prefix)



reminder=[]





key = ""
api = statcord.Client(b,key)
api.start_loop()

b.remove_command("help")


@b.event
async def on_guild_join(guil):
 try :
  m=await guild.fetch_member(761167079171686400)
  p=cnt.find({})
  for re in p :
    if(re["gg"]==1) :
      cnt.update_one(
          {"gg":1},
              {
                    "$set":{
                            "count": re["count"]+1 
                          }
              }
        )
      await m.send(f"Joined server, **Count** : {re['count']+1}")
 except :
   print('Error42069')


@b.event
async def on_command(ctx):
    api.command_run(ctx)






@b.event
async def on_ready():
  print('Bot Online!')
  global guild
  guild = b.get_guild(783921718392520715)
  await b.change_presence(activity=discord.Game(name=f'u.help'))
  global startTime
  async def threading():
    if(1):
      total_seconds_wait=5
      fg=0
      while total_seconds_wait:
        cur=collections.find({})
        for q in cur :
          if(floor(time.time())>=q["tar"]):
            collections.delete_one(q)
        cursor=collection.find({})
        for p in cursor :
          if(floor(time.time())>=p["target"]):
            if(1):
              try :
                asyncio.run_coroutine_threadsafe(b.get_channel(p["chann"]).send(p["output"]), c.loop).result()
                collection.delete_one(p)
              except :
                #print(f'{p["author"]}')
                continue
        cursorer=dai.find({})
        for r in cursorer :
          if(floor(time.time())>=r["target"]):
            try :
                s=str(r["author"])
                k=s[:(len(s)-5)]
                dai.update_many(
                    {"target": r["target"]},
                        {
                          "$set":{
                              "target": floor(time.time())+24*60*60
                                  }
                        }
                )
                asyncio.run_coroutine_threadsafe(b.get_channel(int(r["chann"])).send(r["output"]), c.loop).result()
                # asyncio.run_coroutine_threadsafe(b.get_channel(int(r["chann"])).send(f"```{k}, You have recieved a message from Bot Creator\nType `update to see the message.```"), c.loop).result()
            except :
               #print(f'{r["author"]}')
               continue
        cursor=use.find({})
        for p in cursor :
          if(floor(time.time())>=p["target"]):
            if(1):
              try :
                asyncio.run_coroutine_threadsafe(b.get_channel(p["chann"]).send(p["output"]), c.loop).result()
                use.delete_one(p)
              except :
                #print(f'{p["author"]}')
                continue
        if(fg==0):
            now = floor(time.time())
            fg=1
        if(now+1<=floor(time.time())):
            fg=0
            total_seconds_wait-=1
        if(total_seconds_wait==0):
            total_seconds_wait=5
  def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(threading())
    loop.close()
  _thread.start_new_thread(between_callback,())



class cogrel(discord.ui.Select):
          def __init__(self,b,ctx):
              self.b=b
              self.ctx=ctx
              options = [
                  discord.SelectOption(label='ADMIN'),
                  discord.SelectOption(label='CUSTOM'),
                  discord.SelectOption(label='FUN'),
                  discord.SelectOption(label='HELP'),
                  discord.SelectOption(label='INFO'),
                  discord.SelectOption(label='MISC'),
                  discord.SelectOption(label='MSG'),
                  discord.SelectOption(label='REMINDERS')
              ]
              super().__init__(placeholder='Please Select a Cog', min_values=1, max_values=1, options=options)
          async def callback(self, interaction: discord.Interaction):
              self.b.unload_extension(f'cogs.{self.values[0].lower()}')
              self.b.load_extension(f'cogs.{self.values[0].lower()}')
              await interaction.response.send_message(f'Cog : **{self.values[0]}** has been Reloaded Successfully!')
          async def interaction_check(self,interaction) -> bool :
            if interaction.user!=self.ctx.author :
              await interaction.response.send_message("Only Owner can handle the Cogs",ephemeral=True)
              return False
            else :
              return True
          



class Menu(discord.ui.View):
    def __init__(self,b,ctx):
      super().__init__(timeout=None)
      self.b=b
      self.ctx=ctx
      self.add_item(cogrel(b,ctx))

    async def interaction_check(self,interaction) -> bool :
      if interaction.user!=self.ctx.author :
        await interaction.response.send_message("Only Owner can handle the Cogs",ephemeral=True)
        return False
      else :
        return True
  



@b.command()
async def cogs(ctx) :
  if(ctx.author.id==761167079171686400) :
    embed=discord.Embed(title="Reloading Cogs",description="**GoViper. . .\nPlease Select one of the Cogs\nwhich you want to reload**",color=Colour.dark_red())
    await ctx.send(embed=embed,view=Menu(b,ctx))




for filename in os.listdir('./cogs') :
  if filename.endswith('.py'):
    b.load_extension(f'cogs.{filename[:-3]}')
    print(f'Cog : {filename[:-3]} has been loaded!')




keep_alive() 
b.run('ODcyNDgwMDY5NDMwNDMxNzk0.YQqeYg.5PqkgUhVjCikPahAuox1wWAh0K0')
