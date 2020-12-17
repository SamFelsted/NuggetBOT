import discord
import riotsearch
from discord.ext import commands
import random
import cfg


client = discord.Client()

client = commands.Bot(command_prefix='$')
flames = cfg.insults
good = cfg.good
anime = cfg.violations
gif = cfg.gifs

@client.event
async def on_ready():
    print("log-in good")
    activity = discord.Activity(name='you all fail at league', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Welcome to the NugBot Backend!")


@client.event
async def on_message(message):
    if any(bad_word in message.content.strip().lower() for bad_word in anime)  and message.author.id != 691479754980982805:
        ms = message
        await message.delete()
        await ms.channel.send("https://cdn.discordapp.com/attachments/738265138079072280/751277876527235132/image0.png")
        await ms.channel.send(f"That is an anime violation! {message.author.mention}")

    elif any(bad_word in message.content.strip().lower() for bad_word in gif):
        ms = message
        await message.delete()
        await ms.channel.send(f"There will be NO gifs here! {message.author.mention}")

    else:
        await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command()
async def talk(ctx):
    if ctx.author.id == 672959705672581161:
        message = input('What do you want to send? ')
        await ctx.send(message)
        resp = input('again? y/n ')
        if resp == 'y':
            await talk(ctx)
        else:
            print("Chat ended")
    else:
        print("Hey some idiot tried to use me")


@client.command()
async def lolrate(ctx, name):
    activity = discord.Activity(name='you all fail at league', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    data = riotsearch.findStats(name)
    if data != "No data":
        won = riotsearch.winCheck(name)
        game = 'lost'
        if won:
            game = "won"
        message = f"Ah yes {name} had a kda of {data} and {game} the game..."
        await ctx.send(message)
        if won and data >= 1.5:
            await ctx.send(good[random.randint(0, len(good) - 1)])
        elif not won and data >= 3:
            await ctx.send("Well you lost, guess you can't carry your team that hard")
        else:
            await ctx.send(flames[random.randint(0, len(flames) - 1)])
            activity = discord.Activity(name=(name + ' fail'), type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
    if data == "No data":
        print("Not found")
        await ctx.send(f"No Data for {name}")
    else:
        print("An error has happened")
if __name__ == "__main__":
    client.run(cfg.token)
