import discord
import random
kit = [1,2]
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")


          
    else:
        await message.channel.send(message.content)

client.run("")

import random

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def Toplama(ctx,c:int, g:int):
    await ctx.send(f"Toplam: {c+g}")


@bot.command()
async def Toplama(ctx,c:int, g:int):
    await ctx.send(f"Carpma: {c*g}")

@bot.command()
async def Toplama(ctx,c:int, g:int):
    await ctx.send(f"Bölüm: {c/g}")

@bot.command()
async def Toplama(ctx,c:int, g:int):
    await ctx.send(f"Çikarma: {c-g}")
    
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run("")
