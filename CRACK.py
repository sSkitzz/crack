import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'HEY PLEASE BE SAFE WHILE TRADING USE A MIDDLE MAN AS YOUR CONDOM SO YOU DON UP COMPLAINING WHEN YOUR OLDER!')
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
client.run(os.getenv('TOKEN'))
