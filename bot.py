import discord
import os
from discord.ext import commands
import io
import aiohttp

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("===== Bot is ready =====")
    print(f"Latency {round(client.latency * 1000)}ms")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! --> {round(client.latency * 1000)}ms")

@client.command()
async def precio(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://monitordolarweb.com/gen_imagen/mdw.jpg") as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'mdw.jpg'))

client.run(os.environ.get("token"))

#Need to update URL, since the main website it gets the image from isn't working anymore
