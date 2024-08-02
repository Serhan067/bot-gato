import discord
from discord.ext import commands
import random
import os
import requests
import time
import text
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
komutlar = ["$hello", "$heh (kaçtaneolacağınıyazın)", "$yazitura hangisini seçtiğini yaz(yazi or tura)", "$Topla sayi1(gir) sayi2(gir)","$Çarp sayi1(gir) sayi2(gir)", "$Böl sayi1(gir) sayi2(gir)" ,"$Çikart sayi1(gir) sayi2(gir)", "$Brainrot (yabanci veya Türkçe)", "$memes", "$fox", "$duck"]
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
 

@bot.command()
async def komut(ctx):
    await ctx.send(f"Geçerli komutlar : {komutlar}")  


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yazitura(ctx, secenek = "hangisi"):
    hangi = ["yazi" , "tura"]
    for i in range(3):

        secim = random.choice(hangi)
    if secim == "yazi" and secenek == "yazi":
        await ctx.send("Kazandin")
    elif secim == "tura" and secenek == "tura":
        await ctx.send("Kazandin")
    else:
        
        await ctx.send("Kaybettin")
    

@bot.command()
async def Topla(ctx, a:int , b:int):
    await ctx.send(a+b)


@bot.command()
async def Çarp(ctx, a:int , b:int):
    await ctx.send(a*b)

@bot.command()
async def Çikart(ctx, a:int , b:int):
    await ctx.send(a-b)

@bot.command()
async def Böl(ctx, a:int , b:int):
    await ctx.send(a/b)

@bot.command()
async def Brainrot(ctx, dil = "bilinmiyor"):
    if dil == "yabanci":
        yabanci = ["you are my sunshine 🏀", "Erm what the sigma 👣" , "ohio skibidi rizz", "grimace shake academy ", "English or spanish"]
        cevap = random.choice(yabanci)
        


        await ctx.send(cevap)
    elif dil == "Türkçe":
        turkce = ["Eren blackmamba", "konuş artik" , "elprimosigma" , "Cem yilmaz hayatini kaybetti", "liberya","ugandali bilim insanlari bunu bilmenizi istemiyor", "merhamet edin efendim"]
        turkce2 = random.choice(turkce)
        await ctx.send(turkce2)
    else:
        await ctx.send("hangi dilde istediğini yazmalisin dostum ,Örnek: yabanci veya Türkçe")


@bot.command()
async def image1(ctx):
    with open("images/mem1.png", "rb") as f:
        fotoraf = discord.File(f)
    await ctx.send(file = fotoraf) 
    



@bot.command()
async def image2(ctx):
    with open("images/mem2.png", "rb") as f:
        fotoraf = discord.File(f)
    await ctx.send(file = fotoraf) 
    
@bot.command()
async def image3(ctx):
    with open("images/mem3.png", "rb") as f:
        fotoraf = discord.File(f)
    await ctx.send(file = fotoraf) 
    
@bot.command()

async def resim(ctx):

    a = random.choice(os.listdir("images"))
    with open(f"images/{a}", "rb")as k:
        leon = discord.File(k)
    await ctx.send(file = leon) 
        

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def T():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = T()
    await ctx.send(image_url)


@bot.command()
async def memes(ctx): 
    
    k =random.randint(0,200)
    if k > 0 and k < 101 :
        a = "mem1.png"
        
        await ctx.send("200 içinden 100 ihtimalle")
    elif k >= 101 and k < 152:
        await ctx.send("200 içinden 50 ihtimalle")
        a = "mem2.png"
    elif k >= 152 and k < 178:
        await ctx.send("200 içinden 25 ihtimal")
        a = "mem3.png"
    elif k >= 178 and k < 186:
        await ctx.send("200 içinden 7 ihtimalle")
        a = "stonks.png"
    elif k >=186 and k < 191:
        await ctx.send("200 içinden 4 ihtimalle")
        a = "hp.png"
    elif k >=191 and k < 195:
        await ctx.send("200 içinden 3 ihtimalle nadir")
        a = "doge.png"
    elif k >=195 and k < 198:
        await ctx.send("200 içinden 2 ihtimalle baya NADİR")
        a = "amogus.png"
    elif k >=198 and k <=200:
        await ctx.send("%1 EN NADİRİ")
        a = "babapiro.png"
    time.sleep(0.1)
    with open(f"images/{a}", "rb") as f:
        fotoraf = discord.File(f)      
    await ctx.send(file = fotoraf)  
    
@bot.command()
async def pokemon(ctx, pokemon_name = "ditto"):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        image_url = data['sprites']['front_default']
        await ctx.send(image_url)
    else:
        await ctx.send(f"{pokemon_name} adında bir Pokemon bulunamadı.")  





@bot.command()
async def oyun(ctx,a):
    if a == "mobil":
        await ctx.send(text.mobil())
    elif a == "pc":
        await ctx.send(text.pc())
















bot.run("???)
