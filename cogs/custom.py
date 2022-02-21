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



class customs(commands.Cog) :
  def __init__(self,b) :
    self.b=b


  @commands.command()
  async def custom(self,ctx,name,title,*,cont):
    
    if ctx.message.author.guild_permissions.administrator:
      cursor=cus.find({})
      z=0
      for p in cursor :
        if (p["cmdname"] == name and p["Gid"] == str(ctx.author.guild.id)) :
          await ctx.send("Command already exists, Try another name")
          z=1
      if z==0 :
        cus.insert_one({"author" : f"{ctx.author}","url" : f"{ctx.author.avatar.url}" ,"cmdname" : name, "cmdtitle" : title, "cmdcnt" : cont, "Gid" : f"{ctx.guild.id}"})
        his.insert_one({"author" : f'{ctx.author}', "hist" : f'Set a Custom Command : {name}'})
        await ctx.reply(f"Custom Command named **{name}** has been successfully created!")
    else :
      embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
      embed.description=f"You don't have enough permissions to use this command!"
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.timestamp = datetime.datetime.utcnow()
      s=str(ctx.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)

  @commands.command()
  async def customshow(self,ctx) :
    
    cursor=cus.find({})
    a=[]
    cnt=1
    for p in cursor :
      if(p["Gid"]==str(ctx.author.guild.id)) :
        a.append(f'{cnt}. {p["cmdname"]}')
        cnt+=1
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed=discord.Embed(title=f"Server's Custom Commands",color=Colour.dark_red())
    embed.set_thumbnail(url=self.b.user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    if(len(a)==0):
      embed.description='No Custom Commands Yet'
      await ctx.reply(embed=embed,mention_author=False)
    else:
      separator = "\n"
      embed.description=separator.join(map(str, a))
      await ctx.reply(embed=embed,mention_author=False)
    a.clear()

  @commands.command()
  async def customcancel(self,ctx,c):
    
    if ctx.message.author.guild_permissions.administrator:
      cursor=pre.find({})
      gf=0
      for p in cursor :
        if p["Gid"] == str(ctx.guild.id) :
          gf=1
          pref= str(p["prefix"])
      if gf==0 :
          pref = "u."
      cnt=1
      fa=0
      h=0
      cursor=cus.find({})
      for p in cursor :
        if(p["Gid"]==str(ctx.author.guild.id)):
          rem.append(p["cmdname"])
      if(len(rem)==0):
        await ctx.reply('**No Custom Commands to cancel**',mention_author=False)
      else:
        for i in range(len(rem)):
          if(1):
            if(cnt==int(c)): 
                cus.delete_one({"cmdname" : rem[i]})
                his.insert_one({"author" : f'{ctx.author}', "hist" : f'Cancelled a Custom Command : {rem[i]}'})
                await ctx.send(f"Custom Command **{c}** has been cancelled  **{ctx.author.mention}**")
                h=1
                rem.clear()
                return
            cnt=cnt+1
            fa=1
        if(fa==0):
          await ctx.reply(f'No Custom Commands to Cancel',mention_author=False)
        if(h==0):
          await ctx.reply(f'Number you typed is not within the range\nType {pref}customshow to see the range {ctx.author.mention}',mention_author=False)
      rem.clear()
    else :
      embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f"You don't have enough permissions to use this command!"
      embed.timestamp = datetime.datetime.utcnow()
      s=str(ctx.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      await ctx.reply(embed=embed,mention_author=False)
    









def setup(b):
  b.add_cog(customs(b))