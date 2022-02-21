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







class info(commands.Cog) :
  def __init__(self,b) :
    self.b=b

  

  class histo(discord.ui.View):
      def __init__(self,list,ctx,k):
        super().__init__(timeout=None)
        self.list=list
        self.ctx=ctx
        self.k=k
      @discord.ui.button(label="Access History", style=discord.ButtonStyle.red,disabled=False)
      async def counter(self, button: discord.ui.Button, interaction: discord.Interaction):
        s=str(self.ctx.author)
        k=s[:(len(s)-5)]
        embed=discord.Embed(title=f"Bot-User History",color=Colour.dark_red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=self.k)
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
        separator = "\n"
        embed.description=separator.join(map(str, self.list))
        await interaction.response.send_message(embed=embed,ephemeral=True)

      async def interaction_check(self,interaction) -> bool :
        if interaction.user!=self.ctx.author :
          await interaction.response.send_message("You can't check others History",ephemeral=True)
          return False
        else :
          return True

  

  class Paginator(discord.ui.View):
      def __init__(self,list,current,ctx):
        super().__init__(timeout=None)
        self.list=list
        self.current=current
        self.ctx=ctx
      async def dis(self) :
        print('Hello')
        await asyncio.sleep(10)
        for item in self.children:
                item.disabled = True
      @discord.ui.button(label="First", style=discord.ButtonStyle.red,disabled=True)
      async def counte(self, button: discord.ui.Button, interaction: discord.Interaction):
          self.current = 0
          for item in self.children:
              item.disabled = False
          button.disabled=True
          self.children[1].disabled = True
          await interaction.message.edit(embed=self.list[self.current],view=self)
      @discord.ui.button(label="Previous", style=discord.ButtonStyle.red,disabled=True)
      async def counte1(self, button: discord.ui.Button, interaction: discord.Interaction):
          if self.current-1 == 0 :
            for item in self.children:
              item.disabled = False
            button.disabled = True  
            self.current -= 1
            self.children[0].disabled = True
          elif self.current > 0:
            for item in self.children:
              item.disabled = False
            self.current -= 1
          await interaction.message.edit(embed=self.list[self.current],view=self)
      @discord.ui.button(label="Next", style=discord.ButtonStyle.red)
      async def count2(self, button: discord.ui.Button, interaction: discord.Interaction):
          if self.current+1 == len(self.list)-1:
            for item in self.children:
              item.disabled = False
            button.disabled = True  
            self.children[3].disabled = True
            self.current += 1
          elif self.current < len(self.list)-1:
            for item in self.children:
              item.disabled = False
            self.current += 1
          await interaction.message.edit(embed=self.list[self.current],view=self)
      @discord.ui.button(label="Last", style=discord.ButtonStyle.red)
      async def counte3(self, button: discord.ui.Button, interaction: discord.Interaction):
          self.current = len(self.list)-1
          for item in self.children:
              item.disabled = False
          button.disabled=True
          self.children[2].disabled = True
          await interaction.message.edit(embed=self.list[self.current],view=self)

      # async def interaction_check(self,interaction) -> bool :
      #   if interaction.user!=self.ctx.author :
      #     await interaction.response.send_message("Not Yours",ephemeral=True)
      #     return False
      #   else :
      #     return True



  
  @commands.command()
  async def credits(self,ctx) :
    
    embed=discord.Embed(title='**Made with Love by . . .**',color=Colour.dark_red())
    embed.add_field(name='**GoViper#6777 and Provided By Saizuo**', value='**:)**')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=self.b.user.avatar.url)
    # em.set_thumbnail(url=ctx.author.avatar_url)
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,mention_author=False)






  @commands.command()
  async def history(self,ctx) :
    
    cursor=his.find({})
    cur=his.find({})
    a=[]
    d=[]
    cnt=0
    cn=0
    for p in cursor :
      if(p["author"]==str(ctx.author)) :
        
        cnt+=1
    for q in cur :
      if(q["author"]==str(ctx.author)) :
        a.append(f'{cnt-cn}. {q["hist"]}')
        cn+=1
    a.reverse()
    w=10
    if(len(a)>10) :
      while(True) :
        try :
          his.delete_one({"hist" : a[w]})
          w+=1
        except :
          break

    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed=discord.Embed(title=f"Bot-User History",color=Colour.dark_red())
    embed.set_thumbnail(url=self.b.user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    if(len(a)==0):
      embed.description='No History Yet'
      await ctx.reply(embed=embed,mention_author=False)
    else:
      i=0
      while(True) :
        try : 
          d.append(a[i])
          i+=1
          if i==10 :
            break
        except :
          break
      embed=discord.Embed(title=f"Accessing Bot-User History for {k}",color=Colour.dark_red())
      embed.description="Only you can click the button below\nand access history"
      embed.set_thumbnail(url=self.b.user.avatar.url)
      l=str(self.b.user.avatar.url)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      await ctx.reply(embed=embed,view=self.histo(d,ctx,l))
    a.clear()




  

  @commands.command()
  
  async def dict(self,ctx, word) :
      def rmbc(stg):
       stg = stg.replace('[', '')
       stg = stg.replace(']', '')    
       return stg

      self.b.embeds = []
      mesg = word
      url = 'https://api.urbandictionary.com/v0/define'
      prms = {"term" : mesg};
      res = requests.get(url, params = prms);
      defs = res.json()
      for i in range (len(defs['list'])):
            embed=discord.Embed(title=f"Meaning of {mesg}", color=discord.Color.dark_red())
            embed.set_thumbnail(url=self.b.user.avatar.url)
            embed.add_field(name="Definition", value=f"```{rmbc(defs['list'][i]['definition'])}```", inline=False)
            embed.add_field(name="Example", value=f"```{rmbc(defs['list'][i]['example'])}```", inline=False)
            embed.add_field(name="Link", value=rmbc(defs['list'][i]['permalink']), inline=False)
            embed.set_footer(text=f"Page {i+1}/{len(defs['list'])}")
            self.b.embeds.append(embed);
      try :
        await ctx.reply(embed=self.b.embeds[0], view = self.Paginator(self.b.embeds,0,ctx),mention_author=False)
      except :
        await ctx.reply(f"Unable to find the word : **{word}**",mention_author=False)



def setup(b):
  b.add_cog(info(b))