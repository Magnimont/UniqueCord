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




class admin(commands.Cog) :
  def __init__(self,b) :
    self.b=b



  @commands.command()
  async def changeprefix(self,ctx, pref) :
    
    if ctx.message.author.guild_permissions.administrator:
      embed=discord.Embed(title="Change in Prefix",color=Colour.dark_red())
      cursor=pre.find({})
      fg=0
      for p in cursor :
        if(p["Gid"] == str(ctx.author.guild.id)) :
          fg=1
          pre.update_one(
          {"Gid": p["Gid"]},
              {
                    "$set":{
                            "prefix": f'{pref}'
                          }
              }
          )
      if fg==0 :
        pre.insert_one({"prefix" : f'{pref}', "Gid" : f'{ctx.author.guild.id}'})
      embed.description=f"**Prefix** of **UC Bot** has been successfully changed to **{pref}** for **{ctx.author.guild.name}**"
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.timestamp = datetime.datetime.utcnow()
      s=str(ctx.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    else :
      embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
      embed.description=f"You don't have enough permissions\nto use this command!"
      embed.set_thumbnail(url=self.b.user.avatar.url)
      embed.timestamp = datetime.datetime.utcnow()
      s=str(ctx.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    return
      






  @commands.command()
  async def ashow(self,ctx, m : discord.Member):
    
    if ctx.message.author.guild_permissions.administrator: 
      cnt=1
      fa=0
      h=0
      k=0
      falg=0
      al=0
      cursor=collection.find({})
      for p in cursor :
        if(p["author"]==f"{m}"):
          collection.update_one(
          {"target": p["target"]},
              {
                    "$set":{
                            "flag": floor((p["target"]-floor(time.time()))/60)
                          }
              }
          )
          k = floor((p["target"]-floor(time.time()))/60)
          if(k>=60) :
            falg=1
          if(falg==0) :
            reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {k} Minutes')
          else :
            if(k/60>=24) :
              al=1
            if(al==0) :
              reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {"{:.2f}".format(k/60)} Hours')
            else :
              reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {"{:.2f}".format(k/(60*24))} Days')
          falg=0
          al=0
      embed=discord.Embed(title=f"Upcoming Reminders for {m} : \n",color=Colour.dark_red())
      if(len(reminder)==0):
        await ctx.send(f'Upcoming Reminders for {m} : \n**No active reminders**')
      else:
        for i in range(len(reminder)):
          if(h==0):
            a.append('```')
            h=1
          if(reminder[i].find(f'{m}') != -1):
            if 1 : 
              sub_list=[f"{m}"]
              for sub in sub_list:
                  reminder[i] = reminder[i].replace(sub,'TASK     ')
              sub_list=["task"]
              for sub in sub_list:
                  reminder[i] = reminder[i].replace(sub,'')
              a.append(f'{cnt}.{reminder[i]}')
              cnt=cnt+1
              fa=1
        a.append('```')
        if(fa==0):
          await ctx.send('**No active reminders**')
        else :
          separator = "\n"
          embed.description=separator.join(map(str, a))
          #embed.add_field(name='New commands',value='```Type {pref}help to check out new commands```',inline=False)
          embed.timestamp = datetime.datetime.utcnow()
          s=str(ctx.author)
          k=s[:(len(s)-5)]
          embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
          await ctx.reply(embed=embed)
        a.clear()
        reminder.clear()
    else :
        embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
        embed.description=f"You don't have enough permissions to use this command!"
        embed.timestamp = datetime.datetime.utcnow()
        s=str(ctx.author)
        k=s[:(len(s)-5)]
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)




  @commands.command()
  async def ashowuser(self,ctx, m : discord.Member):
    
    if ctx.message.author.guild_permissions.administrator: 
      cnt=1
      fa=0
      h=0
      k=0
      falg=0
      al=0
      cursor=use.find({})
      for p in cursor :
        if(p["author"]==f"{m}"):
          use.update_one(
          {"target": p["target"]},
              {
                    "$set":{
                            "flag": floor((p["target"]-floor(time.time()))/60)
                          }
              }
          )
          k = floor((p["target"]-floor(time.time()))/60)
          if(k>=60) :
            falg=1
          if(falg==0) :
            reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {k} Minutes')
          else :
            if(k/60>=24) :
              al=1
            if(al==0) :
              reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {"{:.2f}".format(k/60)} Hours')
            else :
              reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {"{:.2f}".format(k/(60*24))} Days')
          falg=0
          al=0
      embed=discord.Embed(title=f"Upcoming User Reminders for {m} : \n",color=Colour.dark_red())
      if(len(reminder)==0):
        await ctx.send(f'Upcoming User Reminders for{m} : \n**No active user reminders**')
      else:
        for i in range(len(reminder)):
          if(h==0):
            a.append('```')
            h=1
          if(reminder[i].find(f'{m}') != -1):
            if 1 : 
              sub_list=[f"{m}"]
              for sub in sub_list:
                  reminder[i] = reminder[i].replace(sub,'TASK     ')
              sub_list=["task"]
              for sub in sub_list:
                  reminder[i] = reminder[i].replace(sub,'')
              a.append(f'{cnt}.{reminder[i]}')
              cnt=cnt+1
              fa=1
        a.append('```')
        if(fa==0):
          await ctx.send('**No active user reminders**')
        else :
          separator = "\n"
          embed.description=separator.join(map(str, a))
          #embed.add_field(name='New commands',value='```Type {pref}help to check out new commands```',inline=False)
          embed.timestamp = datetime.datetime.utcnow()
          s=str(ctx.author)
          k=s[:(len(s)-5)]
          embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
          await ctx.reply(embed=embed)
        a.clear()
        reminder.clear()
    else :
        embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
        embed.description=f"You don't have enough permissions to use this command!"
        embed.timestamp = datetime.datetime.utcnow()
        s=str(ctx.author)
        k=s[:(len(s)-5)]
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)




  @commands.command()
  async def acancel(self,ctx,m : discord.Member,c):
    
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
      cursor=collection.find({})
      for p in cursor :
        if(p["author"]==f"{m}"):
          rem.append(p["reminders"])
      if(len(rem)==0):
        await ctx.send('**No active reminders**')
      else:
        for i in range(len(rem)):
          if(1):
            if(cnt==int(c)): 
                collection.delete_one({"reminders" : rem[i]})
                his.insert_one({"author" : f'{ctx.author}', "hist" : f'Cancelled a Reminder : {rem[i]}'})
                await ctx.send(f"Reminder **{c}** has been cancelled  for **{m.mention}**")
                h=1
                rem.clear()
                return
            cnt=cnt+1
            fa=1
        if(fa==0):
          await ctx.send(f'No Previous Reminder which belongs to  {m}')
        if(h==0):
          await ctx.send(f'Number you typed is not within the range\nType {pref}ashow @user to see the range {ctx.author.mention}')
      rem.clear()
    else :
      embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
      embed.description=f"You don't have enough permissions to use this command!"
      embed.timestamp = datetime.datetime.utcnow()
      s=str(ctx.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    



  @commands.command()
  async def acanceluser(self,ctx,m : discord.Member,c):
    
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
      cursor=use.find({})
      for p in cursor :
        if(p["author"]==f"{m}"):
          rem.append(p["reminders"])
      if(len(rem)==0):
        await ctx.send('**No active user reminders**')
      else:
        for i in range(len(rem)):
          if(1):
            if(cnt==int(c)): 
                use.delete_one({"reminders" : rem[i]})
                his.insert_one({"author" : f'{ctx.author}', "hist" : f'Cancelled a User Reminder : {rem[i]}'})
                await ctx.send(f"User Reminder **{c}** has been cancelled for **{m.mention}**")
                h=1
                rem.clear()
                return
            cnt=cnt+1
            fa=1
        if(fa==0):
          await ctx.send(f'No Previous User Reminder which belongs to u {ctx.author.mention}')
        if(h==0):
          await ctx.send(f'Number you typed is not within the range\nType {pref}showuser to see the range {ctx.author.mention}')
      rem.clear()
    else :
        embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
        embed.description=f"You don't have enough permissions to use this command!"
        embed.timestamp = datetime.datetime.utcnow()
        s=str(ctx.author)
        k=s[:(len(s)-5)]
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)
      





  
  @commands.command()
  async def ashowdaily(self,ctx, m : discord.Member):
    
    if ctx.message.author.guild_permissions.administrator: 
      cnt=1
      fa=0
      h=0
      k=0
      falg=0
      al=0
      cursor=dai.find({})
      for p in cursor :
        if(p["author"]==f"{m}"):
          dai.update_one(
          {"target": p["target"]},
              {
                    "$set":{
                            "flag": floor((p["target"]-floor(time.time()))/60)
                          }
              }
          )
          k = floor((p["target"]-floor(time.time()))/60)
          if(k>=60) :
            falg=1
          if(falg==0) :
            reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {k} Minutes')
          else :
            if(k/60>=24) :
              al=1
            if(al==0) :
              reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {"{:.2f}".format(k/60)} Hours')
            else :
              reminder.append(f'{p["reminders"]}\n  TIME-LEFT  : {"{:.2f}".format(k/(60*24))} Days')
          falg=0
          al=0
      embed=discord.Embed(title=f"Daily Reminders for {m} : \n",color=Colour.dark_red())
      if(len(reminder)==0):
        await ctx.send(f'Daily Reminders for {m} : \n**No active reminders**')
      else:
        for i in range(len(reminder)):
          if(h==0):
            a.append('```')
            h=1
          if(reminder[i].find(f'{m}') != -1):
            if 1 : 
              sub_list=[f"{m}"]
              for sub in sub_list:
                  reminder[i] = reminder[i].replace(sub,'TASK     ')
              sub_list=["task"]
              for sub in sub_list:
                  reminder[i] = reminder[i].replace(sub,'')
              a.append(f'{cnt}.{reminder[i]}')
              cnt=cnt+1
              fa=1
        a.append('```')
        if(fa==0):
          await ctx.send('**No active reminders**')
        else :
          separator = "\n"
          embed.description=separator.join(map(str, a))
          #embed.add_field(name='New commands',value='```Type {pref}help to check out new commands```',inline=False)
          embed.timestamp = datetime.datetime.utcnow()
          s=str(ctx.author)
          k=s[:(len(s)-5)]
          embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
          await ctx.reply(embed=embed)
        a.clear()
        reminder.clear()
    else :
        embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
        embed.description=f"You don't have enough permissions to use this command!"
        embed.timestamp = datetime.datetime.utcnow()
        s=str(ctx.author)
        k=s[:(len(s)-5)]
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)




  @commands.command()
  async def acanceldaily(self,ctx,m : discord.Member,c):
    
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
      cursor=dai.find({})
      for p in cursor :
        if(p["author"]==f"{m}"):
          rem.append(p["reminders"])
      if(len(rem)==0):
        await ctx.send('**No active reminders**')
      else:
        for i in range(len(rem)):
          if(1):
            if(cnt==int(c)): 
                dai.delete_one({"reminders" : rem[i]})
                his.insert_one({"author" : f'{m}', "hist" : f'Cancelled a Daily Reminder : {rem[i]}'})
                await ctx.send(f"Daily Reminder **{c}** has been cancelled for **{m.mention}**")
                h=1
                rem.clear()
                return
            cnt=cnt+1
            fa=1
        if(fa==0):
          await ctx.send(f'No Previous Daily reminder which belongs to  {m}')
        if(h==0):
          await ctx.send(f'Number you typed is not within the range\nType {pref}ashowdaily @user to see the range {ctx.author.mention}')
      rem.clear()
    else :
        embed=discord.Embed(title="Permissions Required",color=Colour.dark_red())
        embed.description=f"You don't have enough permissions to use this command!"
        embed.timestamp = datetime.datetime.utcnow()
        s=str(ctx.author)
        k=s[:(len(s)-5)]
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)
      




def setup(b):
  b.add_cog(admin(b))