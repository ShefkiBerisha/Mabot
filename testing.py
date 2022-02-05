import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="^")

@bot.event 
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("^help"))
    print("Ready")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency: `{round(bot.latency * 1000)}ms`")
    
bot.run("OTI3MjU0NTA4MzczOTUwNDY0.YdHjDg.VTo6uzgykYs9ggxz4T3DhmXkN-M")