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








class fun(commands.Cog) :
  def __init__(self,b) :
    self.b=b

  


  class delethree(discord.ui.View):
      def __init__(self,b,ctx,a,k):
        super().__init__(timeout=None)
        self.list=b
        self.ctx=ctx
        self.a=a
        self.k=k
          
      @discord.ui.button(label="1", style=discord.ButtonStyle.red)
      async def cnter(self, button: discord.ui.Button, interaction: discord.Interaction):
        s=str(self.ctx.author)
        k=s[:(len(s)-5)]
        if self.a==0 :
         embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
        else :
          embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
        embed.set_thumbnail(url=self.k)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
        embed.description=self.list[0]
        for item in self.children:
              item.disabled = False
        button.disabled=True
        await interaction.response.edit_message(embed=embed,view=self) 


      @discord.ui.button(label="2", style=discord.ButtonStyle.red)
      async def counter1(self, button: discord.ui.Button, interaction: discord.Interaction):
        for item in self.children :
          item.disabled=False
        button.disabled=True
        s=str(self.ctx.author)
        k=s[:(len(s)-5)]
        if self.a==0 :
         embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
        else :
          embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=self.k)
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
        embed.description=self.list[1]
        for item in self.children:
              item.disabled = False
        button.disabled=True
        await interaction.response.edit_message(embed=embed,view=self)


      @discord.ui.button(label="3", style=discord.ButtonStyle.red)
      async def counter2(self, button: discord.ui.Button, interaction: discord.Interaction):
        for item in self.children :
          item.disabled=False
        button.disabled=True
        s=str(self.ctx.author)
        k=s[:(len(s)-5)]
        if self.a==0 :
         embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
        else :
          embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=self.k)
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
        embed.description=self.list[2]
        for item in self.children:
              item.disabled = False
        button.disabled=True
        await interaction.response.edit_message(embed=embed,view=self)

      


  class dele2(discord.ui.View):
      def __init__(self,list,ctx,a,k):
        super().__init__(timeout=None)
        self.list=list
        self.ctx=ctx
        self.a=a
        self.k=k

      @discord.ui.button(label="1", style=discord.ButtonStyle.red)
      async def counter3(self, button: discord.ui.Button, interaction: discord.Interaction):
        for item in self.children :
          item.disabled=False
        button.disabled=True
        s=str(self.ctx.author)
        k=s[:(len(s)-5)]
        if self.a==0 :
         embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
        else :
          embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=self.k)
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
        embed.description=self.list[0]
        for item in self.children:
              item.disabled = False
        button.disabled=True
        await interaction.response.edit_message(embed=embed,view=self) 


      @discord.ui.button(label="2", style=discord.ButtonStyle.red)
      async def counter4(self, button: discord.ui.Button, interaction: discord.Interaction):
        for item in self.children :
          item.disabled=False
        button.disabled=True
        s=str(self.ctx.author)
        k=s[:(len(s)-5)]
        if self.a==0 :
         embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
        else :
          embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=self.k)
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
        embed.description=self.list[1]
        for item in self.children:
              item.disabled = False
        button.disabled=True
        await interaction.response.edit_message(embed=embed,view=self)



  class dele1(discord.ui.View):
      def __init__(self,list,ctx,a,k):
        super().__init__(timeout=None)
        self.list=list
        self.ctx=ctx
        self.a=a
        self.k=k

      @discord.ui.button(label="1", style=discord.ButtonStyle.red)
      async def counter5(self, button: discord.ui.Button, interaction: discord.Interaction):
        for item in self.children :
          item.disabled=False
        button.disabled=True
        s=str(self.ctx.author)
        k=s[:(len(s)-5)]
        if self.a==0 :
         embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
        else :
          embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=self.k)
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
        embed.description=self.list[0]
        for item in self.children:
              item.disabled = False
        button.disabled=True
        await interaction.response.edit_message(embed=embed,view=self) 



    
  class nitr(discord.ui.View):
      def __init__(self,ctx):
        super().__init__(timeout=None)
        self.ctx=ctx

      @discord.ui.button(label="Claim", style=discord.ButtonStyle.red)
      async def counter5(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(embed=None,content="https://imgur.com/NQinKJB",view=self) 
      
      async def interaction_check(self,interaction) -> bool :
        if interaction.user!=self.ctx.author :
          await interaction.response.send_message("You can't claim other's Nitro!",ephemeral=True)
          return False
        else :
          return True






  @commands.command()
  async def secret(self,ctx) :
    
    embed=discord.Embed(title='Secret Fun Fact about me!',color=Colour.dark_red())
    embed.description='I am the **Mother** of [**this Bot**](https://top.gg/bot/873590828986171423)\nLets not talk about who **Father** is'
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=self.b.user.avatar.url)
    # em.set_thumbnail(url=ctx.author.avatar_url)
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,mention_author=False)




        
  @commands.Cog.listener()
  async def on_message_delete(self,message):
    if not message.author.bot:
      de.insert_one({"author" :f'{message.author}', "Gid" : f'{message.author.guild.id}', "msg" : f'{message.content}', "flag" : 0, "chann" : f'{message.channel}',"target" : int(time.time()) })



  @commands.command()
  async def snipe(self,ctx) :
    
    cursor=de.find({})
    cur=de.find({})
    a=[]
    self.b.d=[]
    c=[]
    for p in cursor :
      if p["Gid"]==str(ctx.author.guild.id) and p["flag"]==0:
        c.append(p["msg"])
    for q in cur :
      if(q["Gid"]==str(ctx.author.guild.id) and q["flag"]==0) :
        a.append(f'Message Owner : **{q["author"]}**\nChannel : **{q["chann"]}**\nMessage Deleted : **{q["msg"]}**')
    a.reverse()
    c.reverse()
    w=3
    if(len(c)>3) :
      while(True) :
        try :
          de.delete_one({"msg" : c[w]})
          w+=1
        except :
          break

    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=self.b.user.avatar.url)
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    if(len(a)==0):
      embed.description='No Messages Deleted Yet'
      await ctx.reply(embed=embed,mention_author=False)
    else:
      i=0
      while(True) :
        try : 
          self.b.d.append(a[i])
          i+=1
          if i==3 :
            break
        except :
          break
      embed=discord.Embed(title=f"Delete History",color=Colour.dark_red())
      embed.description="click the respective buttons to snipe"
      embed.set_thumbnail(url=self.b.user.avatar.url)
      n=str(self.b.user.avatar.url)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      if len(self.b.d) == 3 :
        await ctx.reply(embed=embed,view=self.delethree(self.b.d,ctx,0,n),mention_author=False)
      elif len(self.b.d) == 2 :
        await ctx.reply(embed=embed,view=self.dele2(self.b.d,ctx,0,n),mention_author=False)
      elif len(self.b.d) == 1 :
        await ctx.reply(embed=embed,view=self.dele1(self.b.d,ctx,0,n),mention_author=False)


  @commands.Cog.listener()
  async def on_message_edit(self,message_before, message_after):
    if not message_before.author.bot:
      ede.insert_one({"author" :f'{message_before.author}', "Gid" : f'{message_before.author.guild.id}', "msgb" : f'{message_before.content}',"msga" : f'{message_after.content}',"flag" : 0, "chann" : f'{message_before.channel}'})


  @commands.command()
  async def editsnipe(self,ctx) :
    
    cursor=ede.find({})
    cur=ede.find({})
    a=[]
    self.b.d=[]
    c=[]
    for p in cursor :
      if p["Gid"]==str(ctx.author.guild.id) and p["flag"]==0:
        c.append(p["msga"])
    for q in cur :
      if(q["Gid"]==str(ctx.author.guild.id) and q["flag"]==0) :
        a.append(f'Message Owner : **{q["author"]}**\nChannel : **{q["chann"]}**\nMessage Before Edit : **{q["msgb"]}**\nMessage After Edit : **{q["msga"]}**')
    a.reverse()
    c.reverse()
    w=3
    if(len(c)>3) :
      while(True) :
        try :
          ede.delete_one({"msga" : c[w]})
          w+=1
        except :
          break

    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
    embed.set_thumbnail(url=self.b.user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    if(len(a)==0):
      embed.description='No Messages Edited Yet'
      await ctx.send(embed=embed,mention_author=False)
    else:
      i=0
      while(True) :
        try : 
          self.b.d.append(a[i])
          i+=1
          if i==3 :
            break
        except :
          break
      embed=discord.Embed(title=f"Edit History",color=Colour.dark_red())
      embed.set_thumbnail(url=self.b.user.avatar.url)
      n=str(self.b.user.avatar.url)
      embed.description="click the respective buttons to Edit snipe"
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      if len(self.b.d) == 3 :
        await ctx.reply(embed=embed,view=self.delethree(self.b.d,ctx,1,n),mention_author=False)
      elif len(self.b.d) == 2 :
        await ctx.reply(embed=embed,view=self.dele2(self.b.d,ctx,1,n),mention_author=False)
      elif len(self.b.d) == 1 :
        await ctx.reply(embed=embed,view=self.dele1(self.b.d,ctx,1,n),mention_author=False)


    
  @commands.command()
  async def nitro(self,ctx) :
    
    embed=discord.Embed(title='You have been gifted a subscription',description="You have been gifted **Discord Nitro** for **3 months**\nExpires in **24 hours**\nClaim before Expiration\n**[Disclaimer](https://www.google.com/UniqueCord&DiscordBot=UniqueCord)**",color=Colour.dark_red())
    embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfkUVViOwesXss5S9jGpNWNAKpkAt7FkyEfcnOTE5ZK5vSdYonJMGLUIz7QCnUor2VSaM&usqp=CAU")
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f"Congratulations! {k}",icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://repository-images.githubusercontent.com/336227331/08ca6fc4-80b3-482e-ba9d-0e13b1fc3288")
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,view=self.nitr(ctx),mention_author=False)







def setup(b):
  b.add_cog(fun(b))