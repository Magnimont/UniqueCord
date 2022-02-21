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
# from views.Menu import delethree,dele1,dele2,Paginator,Menu,nitr,histo


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
reminder=[]


class msg(commands.Cog) :
  def __init__(self,b) :
    self.b=b

 



  @commands.Cog.listener()
  async def on_message(self,message):
    cursor=pre.find({})
    gf=0
    for p in cursor :
      if p["Gid"] == str(message.guild.id) :
        gf=1
        pref= str(p["prefix"])
    if gf==0 :
        pref = "u."
    if message.content == f"{pref}remind" :
      embed=discord.Embed(title=f'Setting Up Reminder' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f"```{pref}remind <number>(without-space)s/m/h/d <task> \ns=seconds  m=minutes  h=hours  d=days```\n```Example : {pref}remind 10s work```"
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}cancel" :
      embed=discord.Embed(title=f'Cancelling Reminder' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```step 1  : {pref}show\n            view embed\nstep 2  : {pref}cancel <number>\n            number = position of the Reminder in embed```\n```Example : {pref}cancel 1\n            which cancels the first Reminder in embed```'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}reminddaily" :
      embed=discord.Embed(title=f'Setting Up Daily Reminder' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f"```{pref}reminddaily <number>(without-space)s/m/h/d <task> \ns=seconds  m=minutes  h=hours  d=days```\n```Example : {pref}reminddaily 10s work```"
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}canceldaily" :
      embed=discord.Embed(title=f'Cancelling Daily Reminder' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```step 1  : {pref}showdaily\n            view embed\nstep 2  : {pref}canceldaily <number>\n            number = position of the Reminder in embed```\n```Example : {pref}canceldaily 1\n            which cancels the first Reminder in embed```'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content ==f"{pref}reminduser" :
      embed=discord.Embed(title=f'Setting Up User Reminder' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f"```{pref}reminduser <@user> <number>(without-space)s/m/h/d <task> \ns=seconds  m=minutes  h=hours  d=days```\n``` Example : {pref}reminduser @viper 10s work```"
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}canceluser" :
      embed=discord.Embed(title=f'Cancelling User Reminder' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```step 1  : {pref}showuser\n            view embed\nstep 2  : {pref}canceluser <number>\n            number = position of the Reminder in embed```\n```Example : {pref}canceluser 1\n            which cancels the first Reminder in embed```'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}feedback" :
      embed=discord.Embed(title=f'Sending Feedback' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```{pref}feedback <issue>```'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}customcancel" :
      embed=discord.Embed(title=f'Cancelling Custom Command' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```step 1  : {pref}customshow\n            view embed\nstep 2  : {pref}customcancel <number>\n            number = position of the Custom Command in embed```\n```Example : {pref}customcancel 1\n            which cancels the first Custom Command in embed```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}custom" :
      embed=discord.Embed(title=f'Create a Custom Command' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.set_image(url="https://cdn.discordapp.com/attachments/918469963122081856/920222368931127377/unknown.png")
      embed.description=f'```{pref}custom <NameOfCommand> <Title> <Content>```\n```Example : {pref}custom st STORY Once upon a time, there was a . .```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}dict" :
      embed=discord.Embed(title=f'Find all about a word' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```{pref}dict <word>```\n```Example : {pref}dict viper```'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}changeprefix" :
      embed=discord.Embed(title=f'Change in Prefix of UC Bot for whole Server' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```{pref}changeprefix <prefix>```\n```Example : {pref}changeprefix #```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}ashow" :
      embed=discord.Embed(title=f'View Basic Reminders of other users' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```{pref}ashow <@user>```\n```Example : {pref}ashow @viper```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}ashowuser" :
      embed=discord.Embed(title=f'View User Reminders of other users' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```{pref}ashowuser <@user>```\n```Example : {pref}ashowuser @viper```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}ashowdaily" :
      embed=discord.Embed(title=f'View Daily Reminders of other users' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```{pref}ashowdaily <@user>```\n```Example : {pref}ashowdaily @viper```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}acancel" :
      embed=discord.Embed(title=f'Cancelling Basic Reminder of other users' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```step 1  : {pref}ashow <@user>\n            view embed\nstep 2  : {pref}acancel <@user> <number>\n            number = position of the Reminder in embed```\n```Example : {pref}acancel @viper 1\n            which cancels the first Reminder in embed```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}acanceluser" :
      embed=discord.Embed(title=f'Cancelling User Reminder of other users' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```step 1  : {pref}ashowuser <@user>\n            view embed\nstep 2  : {pref}acanceluser <@user> <number>\n            number = position of the Reminder in embed```\n```Example : {pref}acanceluser @viper 1\n            which cancels the first Reminder in embed```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    if message.content == f"{pref}acanceldaily" :
      embed=discord.Embed(title=f'Cancelling Daily Reminder of other users' ,color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```step 1  : {pref}ashowdaily <@user>\n            view embed\nstep 2  : {pref}acanceldaily <@user> <number>\n            number = position of the Reminder in embed```\n```Example : {pref}acanceldaily @viper 1\n            which cancels the first Reminder in embed```\n**Note** : This command can only be used by Admins.'
      embed.timestamp = datetime.datetime.utcnow()
      s=str(message.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=message.author.avatar.url)
      await message.reply(embed=embed,mention_author=False)
    h=3600
    q=0
    if message.content.startswith(f'{pref}feedback'):
        results=collections.find({"timelim":f'{message.author}'})
        for result in results:
            if(result["flag"]==1):
              results=collections.find({"time2":f'{message.author}'})
              for result in results:
                if(result["flag"]==0):
                  results=collections.find({"time3":f'{message.author}'})
                  for result in results:
                    if(result["flag"]==1):
                      await message.reply('U have reached the limit, try again within next hour.')
                      return
        results=collections.find({"timelim":f'{message.author}'})
        for result in results:
          if(result["flag"]==1):
            results=collections.find({"time2":f'{message.author}'})
            for result in results:
              if(result["flag"]==0):
                results=collections.find({"time3":f'{message.author}'})
                for result in results:
                  if(result["flag"]==0):
                    q=1
                    break
        if(q==0):
          collections.insert_one({"timelim":f"{message.author}","flag":0, "tar" : h + floor(time.time())})
          collections.insert_one({"time2":f"{message.author}","flag":0, "tar" : h + floor(time.time())})
          collections.insert_one({"time3":f"{message.author}","flag":0, "tar" : h + floor(time.time())})
          return
        await message.reply('U have reached the limit, try again within next hour.')
        collections.update_many(
          {"time3":f'{message.author}'},
              {
                    "$set":{
                            "flag":1 
                          }
              }
        )


    if(message.content=='<@!872480069430431794>'):
        embed=discord.Embed(title=f'Hey' ,color=Colour.dark_red())
        embed.set_thumbnail(url=self.b.user.avatar.url)
        embed.description=f"My **Prefix** is **{pref}** for your **Server :  {message.author.guild.name}**\n```Type {pref}help if you need any Help```"
        await message.reply(embed=embed,mention_author=False)
    result = cus.find({})
    for res in result :
      if(message.content==f'{pref}{res["cmdname"]}' and str(message.author.guild.id)==res["Gid"]) :
        embed=discord.Embed(title=f'{res["cmdtitle"]}',color=Colour.dark_red())
        embed.description=f'{res["cmdcnt"]}'
        embed.set_thumbnail(url=self.b.user.avatar.url)
        s=str(res["author"])
        k=s[:(len(s)-5)]
        embed.set_footer(text=f'\u200bCustom Command Made by {k}',icon_url=res["url"])
        await message.reply(embed=embed,mention_author=False)





def setup(b) :
  b.add_cog(msg(b))
  

