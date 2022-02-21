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
cluster=MongoClient("mongodb+srv://GoViper:GoViper#123@unique--cord.hmhy6.mongodb.net/test?retryWrites=true&w=majority")
                
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


class misc(commands.Cog) :
  def __init__(self,b) :
    self.b=b

 


    
  @commands.command()
  async def update(self,ctx):
    
    cursor=pre.find({})
    gf=0
    for p in cursor :
      if p["Gid"] == str(ctx.guild.id) :
        gf=1
        pref= str(p["prefix"])
    if gf==0 :
        pref = "u."
    cn=0
    results=coll.find({})
    for result in results:
        if(result["member"]==f'{ctx.author}'):
          cn=1
          break
    if(cn==0) :
      coll.insert_one({"member" : f'{ctx.author}'})
    await ctx.reply(f'**No Announcement for now.**')











  @commands.command()
  async def feedback(self,ctx,*,arg):
    
    cursor=pre.find({})
    gf=0
    for p in cursor :
      if p["Gid"] == str(ctx.guild.id) :
        gf=1
        pref= str(p["prefix"])
    if gf==0 :
        pref = "u."
    x=0
    results=collections.find({"timelim":f'{ctx.author}'})
    for result in results:
          if(result["flag"]==1):
            x=1
            break
    if(x==0):
      with open("feedback.txt","a") as f:
        f.write(f"{ctx.author} -> {arg}\n")
      embed=discord.Embed(title=f'Feedback Recieved by {ctx.author}',color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.description=f'```{arg}```\n'
      #embed.add_field(name='New commands',value=f'```Type {pref}help to check out new commands```',inline=False)
      await ctx.reply(embed=embed)
      collections.update_many(
        {"timelim":f'{ctx.author}'},
            {
                  "$set":{
                          "flag":1
                        }
            }
      )
    



  @commands.command()
  async def ping(self,ctx) :
    
    embed=discord.Embed(title='My Ping',description=f"**{(self.b.latency)*1000} ms**",color=Colour.dark_red())
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=self.b.user.avatar.url)
    # em.set_thumbnail(url=ctx.author.avatar_url)
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,mention_author=False)

  @commands.command()
  async def uptime(self,ctx) :
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    s= str(uptime)
   
    s=s.replace(',', '`')
    print(s)
    s=s.replace('d', '`d')
    flag=0
    f=0
    fl=0
    k=""
    p=""
    q=""
    for i in range(len(s)) :
      if s[i]!=':' and flag==0 :
        k+=s[i]
        continue
      if s[i]==':' and flag==0 :
        p+=f"{k} : `Hours`"
        k=""
        flag=1
        continue
      if s[i]!=':' and f==0 :
        k+=s[i]
        continue
      if s[i]==':' and f==0 :
        q+=f"{k} : `Minutes`"
        f=1
        k=""
        continue
      if s[i]!=':' and fl==0 :
        k+=s[i]
        continue
      
    p=p.replace('`d', ':`d')     
    embed=discord.Embed(title='My UpTime',description=f"{p} {q} {k} : `Seconds`",color=Colour.dark_red())
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=self.b.user.avatar.url)
    # em.set_thumbnail(url=ctx.author.avatar_url)
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,mention_author=False)



  @commands.command()
  async def invite(self,ctx) :
    
    embed=discord.Embed(title='Invite UniqueCord',url='https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands' ,description="Thank You!\nYou wont regret this UwU",color=Colour.dark_red())
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=self.b.user.avatar.url)
    # em.set_thumbnail(url=ctx.author.avatar_url)
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,mention_author=False)

  @commands.command()
  async def vote(self,ctx) :
    
    embed=discord.Embed(title='Vote UniqueCord',url='https://top.gg/bot//vote' ,description="Thank You for Voting! UwU",color=Colour.dark_red())
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=self.b.user.avatar.url)
    # em.set_thumbnail(url=ctx.author.avatar_url)
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,mention_author=False)



def setup(b):
  b.add_cog(misc(b))