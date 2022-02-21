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

















class help(commands.Cog) :
  def __init__(self,b) :
    self.b=b

  class Menu(discord.ui.View):
      def __init__(self,ctx,pref,name,u):
        super().__init__(timeout=None)
        self.ctx=ctx
        self.pref=pref
        self.name=name
        self.u=u
        self.add_item(self.Dropdown(ctx,pref,name,u))
      class Dropdown(discord.ui.Select):
          def __init__(self,ctx,pref,name,u):
              options = [
                  discord.SelectOption(label='Reminders', description='Set up different kinds of Reminders', emoji='🔔'),
                  discord.SelectOption(label='Custom', description='Make your own commands', emoji='🛠️'),
                  discord.SelectOption(label='Fun', description='Have fun', emoji='😄'),
                  discord.SelectOption(label='Info', description='Informative Commands', emoji='ℹ️'),
                  discord.SelectOption(label='Administrator', description='Admin-Only Commands', emoji='👤'),
                  discord.SelectOption(label='Misc', description='View crucial aspects of bot', emoji='🪃')
              ]
              super().__init__(placeholder='Please Select a Category', min_values=1, max_values=1, options=options)
              self.ctx=ctx
              self.pref=pref
              self.name=name
              self.u=u
          async def callback(self, interaction: discord.Interaction):
              for item in self.view.children:
                  item.disabled = False
              if(self.values[0]=="Reminders") :
                s=str(self.ctx.author)
                k=s[:(len(s)-5)]
                emb=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
                emb.set_thumbnail(url=self.u)
                gf=0
                for i in range(len(self.pref)) :
                  if self.pref[i]=='`' :
                    gf=1
                if self.pref == '`' or gf==1:
                 emb.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`**\n\n♦️**Basic Reminder Commands**\n`remind` : setting up a basic reminder \n`show`   : displays your basic reminders \n`cancel` : cancels a basic reminder\n\n♦️ ️**Daily Reminder Commands**\n`reminddaily` : setting up a daily reminder \n`showdaily` : displays your daily reminders \n`canceldaily` : cancels a daily reminder\n\n♦️**User Reminder Commands**\n`reminduser` : setting up a reminder for a user \n`showuser` : displays your user reminders \n`canceluser` : cancels a user reminder\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
                else :
                  emb.description=f"**My Prefix is `{self.pref}` for Server : `{self.name}`**\n\n♦️**Basic Reminder Commands**\n`remind` : setting up a basic reminder \n`show`   : displays your basic reminders \n`cancel` : cancels a basic reminder\n\n♦️ ️**Daily Reminder Commands**\n`reminddaily` : setting up a daily reminder \n`showdaily` : displays your daily reminders \n`canceldaily` : cancels a daily reminder\n\n♦️**User Reminder Commands**\n`reminduser` : setting up a reminder for a user \n`showuser` : displays your user reminders \n`canceluser` : cancels a user reminder\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
                await interaction.message.edit(embed=emb,view=self.view)
              if(self.values[0]=="Misc") :
                s=str(self.ctx.author)
                k=s[:(len(s)-5)]
                emb=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
                emb.set_thumbnail(url=self.u)
                gf=0
                for i in range(len(self.pref)) :
                  if self.pref[i]=='`' :
                    gf=1
                if self.pref == '`' or gf==1:
                 emb.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`**\n\n♦️**Misc Commands**\n`vote` : vote bot to support \n`ping` : check out bot's ping\n`uptime` : check out bot's uptime\n`invite` : invite bot to your server \n`update` : get announcement on bot's status from bot creator\n`feedback` : report an issue, if bot has any kind of bug/error\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
                else :
                  emb.description=f"**My Prefix is `{self.pref}` for Server : `{self.name}`**\n\n♦️**Misc Commands**\n`vote` : vote bot to support \n`ping` : check out bot's ping\n`uptime` : check out bot's uptime\n`invite` : invite bot to your server \n`update` : get announcement on bot's status from bot creator\n`feedback` : report an issue, if bot has any kind of bug/error\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
                await interaction.message.edit(embed=emb,view=self.view)
              if(self.values[0]=="Custom") :
                s=str(self.ctx.author)
                k=s[:(len(s)-5)]
                emb=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
                emb.set_thumbnail(url=self.u)
                gf=0
                for i in range(len(self.pref)) :
                  if self.pref[i]=='`' :
                    gf=1
                if self.pref == '`' or gf==1:
                 emb.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`**\n\n♦️**Custom Commands**\n`custom` : create a custom command \n`customshow` : displays custom commands created in your server \n`customcancel` : cancels a custom command in your server \n\n**Note** : Commands : `custom` and `customcancel` can only be used by Admins of respective servers.\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
                else :
                  emb.description=f"**My Prefix is `{self.pref}` for Server : `{self.name}`**\n\n♦️**Custom Commands**\n`custom` : create a custom command \n`customshow` : displays custom commands created in your server \n`customcancel` : cancels a custom command in your server \n\n**Note** : Commands : `custom` and `customcancel` can only be used by Admins of respective servers.\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
                await interaction.message.edit(embed=emb,view=self.view)
              if(self.values[0]=="Fun") :
                s=str(self.ctx.author)
                k=s[:(len(s)-5)]
                emb=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
                emb.set_thumbnail(url=self.u)
                gf=0
                for i in range(len(self.pref)) :
                  if self.pref[i]=='`' :
                    gf=1
                if self.pref == '`' or gf==1:
                 emb.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`**\n\n♦️**Fun Commands**\n`nitro` : get free discord nitro\n`snipe` : check out history of deleted messages, max : 3 \n`editsnipe` : check out history of edited messages, max : 3\n`secret` : check out secret fun fact about me\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)** "
                else :
                  emb.description=f"**My Prefix is `{self.pref}` for Server : `{self.name}`**\n\n♦️**Fun Commands**\n`nitro` : get free discord nitro\n`snipe` : check out history of deleted messages, max : 3 \n`editsnipe` : check out history of edited messages, max : 3\n`secret` : check out secret fun fact about me\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)** "
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
                await interaction.message.edit(embed=emb,view=self.view)
              if(self.values[0]=="Info") :
                s=str(self.ctx.author)
                k=s[:(len(s)-5)]
                emb=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
                emb.set_thumbnail(url=self.u)
                gf=0
                for i in range(len(self.pref)) :
                  if self.pref[i]=='`' :
                    gf=1
                if self.pref == '`' or gf==1:
                 emb.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`**\n\n♦️**Info Commands**\n`dict` : search for a word in urban dictionary \n`history` : displays the bot-user history for respective users\n`credits` : check out who contributed to me\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)** "
                else :
                  emb.description=f"**My Prefix is `{self.pref}` for Server : `{self.name}`**\n\n♦️**Info Commands**\n`dict` : search for a word in urban dictionary \n`history` : displays the bot-user history for respective users\n`credits` : check out who contributed to me\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)** "
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
                await interaction.message.edit(embed=emb,view=self.view)
              if(self.values[0]=="Administrator") :
                s=str(self.ctx.author)
                k=s[:(len(s)-5)]
                emb=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
                emb.set_thumbnail(url=self.u)
                gf=0
                for i in range(len(self.pref)) :
                  if self.pref[i]=='`' :
                    gf=1
                if self.pref == '`' or gf==1:
                 emb.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`**\n\n♦️**Administrator Commands**\n`changeprefix` : change prefix of UC bot for whole server \n`custom` : create a custom command \n`customcancel` : cancels a custom command in your server\n`ashow` : display basic Reminders of other users\n`ashowuser` : display user Reminders of other users\n`ashowdaily` : display daily Reminders of other users\n`acancel` : cancel basic reminders of other users\n`acanceluser` : cancel user reminders of other users\n`acanceldaily` : cancel daily reminders of other users\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
                else :
                  emb.description=f"**My Prefix is `{self.pref}` for Server : `{self.name}`**\n\n♦️**Administrator Commands**\n`changeprefix` : change prefix of UC bot for whole server \n`custom` : create a custom command \n`customcancel` : cancels a custom command in your server\n`ashow` : display basic Reminders of other users\n`ashowuser` : display user Reminders of other users\n`ashowdaily` : display daily Reminders of other users\n`acancel` : cancel basic reminders of other users\n`acanceluser` : cancel user reminders of other users\n`acanceldaily` : cancel daily reminders of other users\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)** "
                emb.timestamp = datetime.datetime.utcnow()
                emb.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
                await interaction.message.edit(embed=emb,view=self.view)




      
      @discord.ui.button(label="Home",emoji="🏠", style=discord.ButtonStyle.red,disabled=True)
      async def counter7(self, button: discord.ui.Button, interaction: discord.Interaction):
          s=str(self.ctx.author)
          k=s[:(len(s)-5)]
          embed=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
          embed.set_thumbnail(url=self.u)
          gf=0
          for i in range(len(self.pref)) :
            if self.pref[i]=='`' :
              gf=1
          if self.pref == '`' or gf==1:embed.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`\n\nMy Categories : **\n\n<:ping:930117753979957319>** • Reminders**\n🧰️** • Custom    **\n<:red:903128849053798440>** • Fun    **\n📌** • Info       **\n<:BotDeveloperRed:902629885460230164>** • Administrator**\n🍁** • Misc     **\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)** "
            
          else :
           embed.description=f"**My Prefix is** **`{self.pref}`** **for Server : `{self.name}`\n\nMy Categories : **\n\n♦️** • Reminders**\n♦️** • Custom    **\n♦️** • Fun    **\n♦️** • Info       **\n♦️** • Administrator**\n♦️** • Misc     **\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
          embed.timestamp = datetime.datetime.utcnow()
          embed.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
          for item in self.children:
              item.disabled = False
          button.disabled=True
          await interaction.message.edit(embed=embed,view=self)
      @discord.ui.button(label="All Commands",  emoji="📜", style=discord.ButtonStyle.red,disabled=False)
      async def counter8(self, button: discord.ui.Button, interaction: discord.Interaction):
          s=str(self.ctx.author)
          k=s[:(len(s)-5)]
          emb=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
          emb.set_thumbnail(url=self.u)
          gf=0
          for i in range(len(self.pref)) :
            if self.pref[i]=='`' :
              gf=1
          if self.pref == '`' or gf==1:
           emb.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`**\n\n♦️**Basic Reminder Commands**\n`remind` | `show` | `cancel`\n\n♦️ ️**Daily Reminder Commands**\n`reminddaily` | `showdaily` | `canceldaily`\n\n♦️**User Reminder Commands**\n`reminduser` | `showuser` | `canceluser`\n\n♦️**Custom Commands**\n`custom` | `customshow` | `customcancel`\n\n♦️**Fun Commands**\n`snipe` | `editsnipe` | `nitro` | `secret`\n\n♦️**Info Commands**\n`dict` | `history` | `credits`\n\n♦️**Administrator Commands**\n`changeprefix` | `custom ` | `customcancel` | `ashow` | `ashowuser` \n  `acanceldaily` | `acancel` | `acanceluser ` | `ashowdaily`\n\n♦️**Misc Commands**\n`update` | `feedback` | `invite` | `vote` | `ping` | `uptime`\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
          else :
            emb.description=f"**My Prefix is `{self.pref}` for Server : `{self.name}`**\n\n♦️**Basic Reminder Commands**\n`remind` | `show` | `cancel`\n\n♦️ ️**Daily Reminder Commands**\n`reminddaily` | `showdaily` | `canceldaily`\n\n♦️**User Reminder Commands**\n`reminduser` | `showuser` | `canceluser`\n\n♦️**Custom Commands**\n`custom` | `customshow` | `customcancel`\n\n♦️**Fun Commands**\n`snipe` | `editsnipe` | `nitro` | `secret`\n\n♦️**Info Commands**\n`dict` | `history` | `credits`\n\n♦️**Administrator Commands**\n`changeprefix` | `custom ` | `customcancel` | `ashow` | `ashowuser` \n  `acanceldaily` | `acancel` | `acanceluser ` | `ashowdaily`\n\n♦️**Misc Commands**\n`update` | `feedback` | `invite` | `vote` | `ping` | `uptime`\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
          emb.timestamp = datetime.datetime.utcnow()
          emb.set_footer(text=f'\u200bRequested by {k}',icon_url=self.ctx.author.avatar.url)
          self.children[0].disabled=False
          button.disabled=True
          await interaction.message.edit(embed=emb,view=self)
      @discord.ui.button(label="Delete Menu", emoji='🛑', style=discord.ButtonStyle.danger)
      async def counter9(self, button: discord.ui.Button, interaction: discord.Interaction):
          await interaction.message.delete()

      async def interaction_check(self,interaction) -> bool :
        if interaction.user!=self.ctx.author :
          await interaction.response.send_message("Not Yours",ephemeral=True)
          return False
        else :
          return True
  

  

  @commands.command()
  async def help(self,ctx) : 
    
    name=str(ctx.author.guild.name)
    cursor=pre.find({})
    gf=0
    for p in cursor :
      if p["Gid"] == str(ctx.guild.id) :
        gf=1
        pref= str(p["prefix"])
    if gf==0 :
        pref = "u."
    z=0
    results=co.find({})
    for result in results:
          if(str(result["author"])== str(ctx.author)):
            z=1
            break
    if(z==0):
      co.insert_one({"author" : f"{ctx.author}"}) 
    s=str(ctx.author)
    k=s[:(len(s)-5)]
    embed=discord.Embed(title=f'Help Menu for {k}',color=Colour.dark_red())
    embed.set_thumbnail(url=self.b.user.avatar.url)
    u=str(self.b.user.avatar.url)
    gf=0
    for i in range(len(pref)) :
      if pref[i]=='`' :
        gf=1
    if pref == '`' or gf==1:
     embed.description=f"**My Prefix is** **{self.pref}** **for Server : `{self.name}`\n\nMy Categories : **\n\n<:ping:930117753979957319>** • Reminders**\n🧰️** • Custom    **\n<:red:903128849053798440>** • Fun    **\n📌** • Info       **\n<:BotDeveloperRed:902629885460230164>** • Administrator**\n🍁** • Misc     **\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)  |  [Website](https://unique-cord.netlify.app)**"
    else :
      embed.description=f"**My Prefix is** **`{pref}`** **for Server : `{ctx.author.guild.name}`\n\nMy Categories : **\n\n♦️** • Reminders**\n♦️** • Custom    **\n♦️** • Fun    **\n♦️** • Info       **\n♦️** • Administrator**\n♦️** • Misc     **\n\n**[Invite UC](https://discord.com/api/oauth2/authorize?client_id=872480069430431794&permissions=414464736320&scope=bot%20applications.commands)   |   [Vote UC](https://top.gg/bot//vote)   |   [Website](https://unique-cord.netlify.app)   |   [Hosted-by-Creavite](https://game.creavite.co/)**"
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'\u200bRequested by {k}',icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed,view=self.Menu(ctx,pref,name,u),mention_author=False)
    




def setup(b):
  b.add_cog(help(b))
