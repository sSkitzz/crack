import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()
client.remove_command('help')


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'HEY PLEASE BE SAFE WHILE TRADING USE A MIDDLE MAN AS YOUR CONDOM SO YOU DO NOT WIND UP COMPLAINING WHEN YOUR OLDER!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready') 


@client.event
async def on_message(message):
    if message.content == 'youtube':
        await client.send_message(message.channel,'youtube is https://www.youtube.com/channel/UCJQtohGy955WizoaE3dWGYg/videos?view_as=subscriber')
    if message.content == 'twitter':
        await client.send_message(message.channel,'https://twitter.com/sSkitzzz')
    if ('TRADE') in message.content:
       await client.delete_message(message)
    if message.content == 'HIT OR MISS':
        await client.send_message(message.channel,'I GUESS THEY NEVER MISS HUH?')
    if message.content == 'CMD':
        await client.send_message(message.channel,'```!HIT OR MISS !YOUTUBE !TWITTER```')
    if message.content == 'hi':
        await client.send_message(message.channel,'HEY')
    if message.content.startswith('ROCK'):
        randomlist = ["ROCK","PAPER","SCISSORS "]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('PAPER'):
        randomlist = ["ROCK","PAPER","SCISSORS "]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('SCISSORS'):
        randomlist = ["ROCK","PAPER","SCISSORS "]
        await client.send_message(message.channel,(random.choice(randomlist)))
        
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
          colour = discord.Colour.blue()
    )

    embed.set_author(name="pills")
    embed.add_field(name="-ping", value="Returns Pong!", inline=False)
    embed.add_field(name="-pong", value="Returns Ping!", inline=False)
    embed.add_field(name="-join", value="joins the voice channel you are in", inline=False)
    embed.add_field(name="-leave", value="leaves the voice channel", inline=False)
    embed.add_field(name="-play [Youtube link]", value="plays the music you put in", inline=False)
    embed.add_field(name="-pause", value="pauses the music", inline=False)
    embed.add_field(name="-resume", value="resumes the music", inline=False)
    embed.add_field(name="-stop", value="stops the music completly", inline=False)

    await client.send_message(author, embed=embed)
client.run(os.getenv('TOKEN'))
