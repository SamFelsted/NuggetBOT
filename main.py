import discord
import riotsearch
from discord.ext import commands
import random
import cfg

client = discord.Client()
password = 
# noinspection PyRedeclaration
client = commands.Bot(command_prefix='$')
flames = cfg.insults


@client.event
async def on_ready():
    print("log-in good")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command()
async def lolrate(ctx, name):
    data = riotsearch.findStats(name)
    won = riotsearch.winCheck(name)
    game = 'lost'
    if won:
        game = "won"
    message = f"Ah yes {name} had a kda of {data} and {game} the game..."
    await ctx.send(message)
    if won and data >= 1.5:
        await ctx.send("Not bad...")
    elif not won and data >= 3:
        await ctx.send("Well you lost, guess you can't carry your team that hard")
    else:
        await ctx.send(flames[random.randint(0, len(flames) - 1)])

if __name__ == "__main__":
    client.run(password)
