import discord 
from discord.ext import commands
bot = commands.Bot(command_prefix= '.')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('type .help'))
    print("Bot is online")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
bot.run('Your token goes here')
