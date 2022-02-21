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




class reminders(commands.Cog) :
  def __init__(self,b) :
    self.b=b

  
  @commands.command()
  async def remind(self,ctx, tm, *, task):
    
      cursor=pre.find({})
      gf=0
      for p in cursor :
        if p["Gid"] == str(ctx.guild.id) :
          gf=1
          pref= str(p["prefix"])
      if gf==0 :
          pref = "u."
      def convert(tm):
        pos = ['s', 'm', 'h', 'd']
        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}
        unit = tm[-1]
        if unit not in pos:
          return -1
        try:
         val = int(tm[:-1])
        except:
         return -2
        return val * time_dict[unit]
      converted_time=convert(tm)
      if converted_time==-1 or converted_time==-2 :
        await ctx.reply(f'Wrong command, type {pref}remind to verify the format')
        return
      try :
        ta = f'{task}'
        list3=[]
        list3[:0]=ta
        gap=''
        list4=[]
        list4[:0]=gap
        orgin =[]
        i=0
        while i<len(list3): 
            orgin.append(list3[i])
            i+=1
            j=0
            if i%38==0 :
                while j<len(list4): 
                  orgin.append(list4[j])
                  j+=1

        separator = ''
        vi=separator.join(map(str,orgin))
        embed=discord.Embed(title=f'Reminder has been set for {ctx.author}',color=Colour.dark_red())
        embed.add_field(name='Task',value=f'{vi}',inline=True)
        embed.add_field(name='Time Left',value=f'{tm}',inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        s=str(ctx.author)
        k=s[:(len(s)-5)]
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)
        tas = f'{task}'
        list1=[]
        list1[:0]=tas
        gap='\n               '
        list2=[]
        list2[:0]=gap
        org =[]
        i=0
        while i<len(list1): 
              org.append(list1[i])
              i+=1
              j=0
              if i%45==0 :
                  while j<len(list2): 
                    org.append(list2[j])
                    j+=1

        separator = ''
        v=separator.join(map(str,org))
        collection.insert_one({"target": converted_time+floor(time.time()),"output": f"{ctx.author.mention} Your Reminder : **{task}**" ,"expireAt":datetime.datetime.fromtimestamp(converted_time + floor(time.time())),"author": f"{ctx.author}","reminders":f"{ctx.author} task : {v}", "chann" : ctx.channel.id, "flag" : converted_time/60})
        his.insert_one({"author" : f'{ctx.author}', "hist" : f'Set a reminder for {task}'})
      except :
        embed=discord.Embed(title='No Permission For Bot To Send Reminder' ,color=Colour.dark_red())
        embed.description=f'Ask an Admin/Moderator in your server to give\n PERMISSIONS to bot by [clicking here](https://discord.com/api/oauth2/authorize?&permissions=274878295104&scope=bot)\n\n**NOTE** : You DO NOT need to kick the bot\n       You can directly click on the above link to give permissions.'
        await ctx.reply(embed=embed)
      





  @commands.command()
  async def reminduser(self,ctx,m : discord.Member, tm, *, task):
    
      cursor=pre.find({})
      gf=0
      for p in cursor :
        if p["Gid"] == str(ctx.guild.id) :
          gf=1
          pref= str(p["prefix"])
      if gf==0 :
          pref = "u."
      def convert(tm):
        pos = ['s', 'm', 'h', 'd']
        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}
        unit = tm[-1]
        if unit not in pos:
          return -1
        try:
         val = int(tm[:-1])
        except:
         return -2
        return val * time_dict[unit]
      converted_time=convert(tm)
      if converted_time==-1 or converted_time==-2 :
        await ctx.reply(f'Wrong command, type {pref}reminduser to verify the format')
        return
      try :
        ta = f'{task}'
        list3=[]
        list3[:0]=ta
        gap=''
        list4=[]
        list4[:0]=gap
        orgin =[]
        i=0
        while i<len(list3): 
            orgin.append(list3[i])
            i+=1
            j=0
            if i%38==0 :
                while j<len(list4): 
                  orgin.append(list4[j])
                  j+=1

        separator = ''
        vi=separator.join(map(str,orgin))
        embed=discord.Embed(title=f'User Reminder has been set for {m}',color=Colour.dark_red())
        embed.add_field(name='Task',value=f'{vi}',inline=True)
        embed.add_field(name='Time Left',value=f'{tm}',inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        s=str(ctx.author)
        q=str(m)
        k=s[:(len(s)-5)]
        z=q[:(len(q)-5)]
        embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)
        tas = f'{task}'
        list1=[]
        list1[:0]=tas
        gap='\n               '
        list2=[]
        list2[:0]=gap
        org =[]
        i=0
        while i<len(list1): 
              org.append(list1[i])
              i+=1
              j=0
              if i%45==0 :
                  while j<len(list2): 
                    org.append(list2[j])
                    j+=1

        separator = ''
        v=separator.join(map(str,org))
        use.insert_one({"target": converted_time+floor(time.time()),"output": f"{m.mention} Your Reminder : **{task}**\n                                                                                                                     **- {ctx.author}**" ,"expireAt":datetime.datetime.fromtimestamp(converted_time + floor(time.time())),"author": f"{ctx.author}","reminders":f"{ctx.author} task : {v}\n  USER       : {z}", "chann" : ctx.channel.id, "flag" : converted_time/60})
        his.insert_one({"author" : f'{ctx.author}', "hist" : f'Set a reminder for {task} to User : {z}'})
      except :
        embed=discord.Embed(title='No Permission For Bot To Send Reminder' ,color=Colour.dark_red())
        embed.description=f'Ask an Admin/Moderator in your server to give\n PERMISSIONS to bot by [clicking here](https://discord.com/api/oauth2/authorize?&permissions=274878295104&scope=bot)\n\n**NOTE** : You DO NOT need to kick the bot\n       You can directly click on the above link to give permissions.'
        await ctx.reply(embed=embed)
      
      







  @commands.command()
  async def show(self,ctx):
    
    cnt=1
    fa=0
    h=0
    k=0
    falg=0
    al=0
    cursor=collection.find({})
    for p in cursor :
      if(p["author"]==f"{ctx.author}"):
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
    embed=discord.Embed(title=f"Upcoming Reminders for {ctx.author} : \n",color=Colour.dark_red())
    if(len(reminder)==0):
      await ctx.send(f'Upcoming Reminders for {ctx.author.mention} : \n**No active reminders**')
    else:
      for i in range(len(reminder)):
        if(h==0):
          a.append('```')
          h=1
        if(reminder[i].find(f'{ctx.author}') != -1):
          if 1 : 
            sub_list=[f"{ctx.author}"]
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


  @commands.command()
  async def showuser(self,ctx):
    
    cnt=1
    fa=0
    h=0
    k=0
    falg=0
    al=0
    cursor=use.find({})
    for p in cursor :
      if(p["author"]==f"{ctx.author}"):
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
    embed=discord.Embed(title=f"Upcoming User Reminders for {ctx.author} : \n",color=Colour.dark_red())
    if(len(reminder)==0):
      await ctx.send(f'Upcoming User Reminders for {ctx.author.mention} : \n**No active user reminders**')
    else:
      for i in range(len(reminder)):
        if(h==0):
          a.append('```')
          h=1
        if(reminder[i].find(f'{ctx.author}') != -1):
          if 1 : 
            sub_list=[f"{ctx.author}"]
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


  @commands.command()
  async def cancel(self,ctx,c):
    
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
      if(p["author"]==f"{ctx.author}"):
        rem.append(p["reminders"])
    if(len(rem)==0):
      await ctx.send('**No active reminders**')
    else:
      for i in range(len(rem)):
        if(1):
          if(cnt==int(c)): 
              collection.delete_one({"reminders" : rem[i]})
              his.insert_one({"author" : f'{ctx.author}', "hist" : f'Cancelled a Reminder : {rem[i]}'})
              await ctx.send(f"Reminder **{c}** has been cancelled  **{ctx.author.mention}**")
              h=1
              rem.clear()
              return
          cnt=cnt+1
          fa=1
      if(fa==0):
        await ctx.send(f'No Previous Reminder which belongs to u {ctx.author.mention}')
      if(h==0):
        await ctx.send(f'Number you typed is not within the range\nType {pref}show to see the range {ctx.author.mention}')
    rem.clear()


    
  @commands.command()
  async def canceluser(self,ctx,c):
    
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
      if(p["author"]==f"{ctx.author}"):
        rem.append(p["reminders"])
    if(len(rem)==0):
      await ctx.send('**No active user reminders**')
    else:
      for i in range(len(rem)):
        if(1):
          if(cnt==int(c)): 
              use.delete_one({"reminders" : rem[i]})
              his.insert_one({"author" : f'{ctx.author}', "hist" : f'Cancelled a User Reminder : {rem[i]}'})
              await ctx.send(f"User Reminder **{c}** has been cancelled  **{ctx.author.mention}**")
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




    

  @commands.command()
  async def reminddaily(self,ctx, tm, *, task):
    
      cursor=pre.find({})
      gf=0
      for p in cursor :
        if p["Gid"] == str(ctx.guild.id) :
          gf=1
          pref= str(p["prefix"])
      if gf==0 :
          pref = "u."
      def convert(tm):
        pos = ['s', 'm', 'h', 'd']
        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}
        unit = tm[-1]
        if unit not in pos:
          return -1
        try:
         val = int(tm[:-1])
        except:
         return -2
        return val * time_dict[unit]
      converted_time=convert(tm)
      if converted_time==-1 or converted_time==-2 :
        await ctx.reply(f'Wrong command, type {pref}reminddaily to verify the format')
        return
      ta = f'{task}'
      list3=[]
      list3[:0]=ta
      gap=''
      list4=[]
      list4[:0]=gap
      orgin =[]
      i=0
      while i<len(list3): 
          orgin.append(list3[i])
          i+=1
          j=0
          if i%38==0 :
              while j<len(list4): 
                orgin.append(list4[j])
                j+=1

      separator = ''
      vi=separator.join(map(str,orgin))
      embed=discord.Embed(title=f'Daily Reminder has been set for {ctx.author}',color=Colour.dark_red())
      embed.add_field(name='Task',value=f'{vi}',inline=True)
      embed.add_field(name='Time Left',value=f'{tm}',inline=True)
      embed.timestamp = datetime.datetime.utcnow()
      s=str(ctx.author)
      k=s[:(len(s)-5)]
      embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      tas = f'{task}'
      list1=[]
      list1[:0]=tas
      gap='\n               '
      list2=[]
      list2[:0]=gap
      org =[]
      i=0
      while i<len(list1): 
          org.append(list1[i])
          i+=1
          j=0
          if i%45==0 :
              while j<len(list2): 
                org.append(list2[j])
                j+=1

      separator = ''
      v=separator.join(map(str,org))
      dai.insert_one({"target": converted_time+floor(time.time()),"output": f"{ctx.author.mention} Your Daily Reminder : **{task}**" ,"expireAt":datetime.datetime.fromtimestamp(converted_time + floor(time.time())),"author": f"{ctx.author}","reminders":f"{ctx.author} task : {v}", "chann" : ctx.channel.id, "flag" : converted_time/60})
      his.insert_one({"author" : f'{ctx.author}', "hist" : f'Set a Daily reminder for {task}'})





  @commands.command()
  async def showdaily(self,ctx):
    
    cnt=1
    fa=0
    h=0
    k=0
    falg=0
    al=0
    cursor=dai.find({})
    for p in cursor :
      if(p["author"]==f"{ctx.author}"):
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
    embed=discord.Embed(title=f"Daily Reminders for {ctx.author} : \n",color=Colour.dark_red())
    if(len(reminder)==0):
      await ctx.send(f'Daily Reminders for {ctx.author.mention} : \n**No active reminders**')
    else:
      for i in range(len(reminder)):
        if(h==0):
          a.append('```')
          h=1
        if(reminder[i].find(f'{ctx.author}') != -1):
          if 1 : 
            sub_list=[f"{ctx.author}"]
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


  

  @commands.command()
  async def canceldaily(self,ctx,c):
    
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
      if(p["author"]==f"{ctx.author}"):
        rem.append(p["reminders"])
    if(len(rem)==0):
      await ctx.send('**No active reminders**')
    else:
      for i in range(len(rem)):
        if(1):
          if(cnt==int(c)): 
              dai.delete_one({"reminders" : rem[i]})
              his.insert_one({"author" : f'{ctx.author}', "hist" : f'Cancelled a Daily Reminder : {rem[i]}'})
              await ctx.send(f"Daily Reminder **{c}** has been cancelled  **{ctx.author.mention}**")
              h=1
              rem.clear()
              return
          cnt=cnt+1
          fa=1
      if(fa==0):
        await ctx.send(f'No Previous Daily reminder which belongs to you {ctx.author.mention}')
      if(h==0):
        await ctx.send(f'Number you typed is not within the range\nType {pref}showdaily to see the range {ctx.author.mention}')
    rem.clear()
    

def setup(b) :
  b.add_cog(reminders(b))
  


  


  
