# Importing the modules that are needed for the bot to work.
import decouple
import os
import discord
from discord.ext import commands, tasks
import time


token = decouple.config("token")
prefix = decouple.config("prefix")

client = commands.Bot(command_prefix=(prefix), description="", intents=discord.Intents.all())

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game('Oxy'))
  print("\n Ready !")



@client.event
async def on_member_join(member):
  print(f'\n {member} has joined the server!')
  
@client.event
async def on_member_remove(member):
  print(f'\n {member} has left the server.')



@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Missing required argument.')



#Commands

@client.command()
async def ping(ctx):
  await ctx.send(f'**pong** {round(client.latency * 1000 )} ms ')




@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount + 1)
  await ctx.send(f'Cleared {amount} mesages!')
  print(f'Cleared {amount} mesages!')
  time.sleep(4)
  await ctx.channel.purge(limit=1)



@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Member : {member} has been kicked.')
  print(f'Member : {member} has been kicked.')
  time.sleep(5)
  await ctx.channel.purge(limit=1)



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Member : {member} has been banned.')
  print(f' Member : {member} has been banned.')
  time.sleep(5)
  await ctx.channel.purge(limit=1)



@client.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, arg1):
  argument1 = (arg1)
  await ctx.channel.purge(limit=1)
  await ctx.send(argument1)
  pass





@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member, *,reason):
  await ctx.channel.purge(limit=1)
  await ctx.send('Member has been warned \n - ')
  await ctx.send(f'{member} you have been warned for,\n **{reason}**.')

client.run(token)

