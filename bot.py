import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("ODE2MTMxOTUwOTg5Mjc5MjMy.YD2gHA.8lfXIIt7K8IvBvmo-zG8pzY2-wA")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


client.run(token)
