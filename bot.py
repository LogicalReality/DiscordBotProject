import discord
import os
#import twint_config.py
from discord.ext import commands

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! --> {round(client.latency * 1000)}ms")
client.run(os.environ.get("token"))