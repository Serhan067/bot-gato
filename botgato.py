
import discord
import serhan
import aswd
from discord.ext import commands
import random
import requests
intents = discord.Intents.all()


bot = commands.Bot(command_prefix='$', intents=intents)
komutlar = ["$hello", "$heh (kaçtaneolacağınıyazın)", "$yazitura hangisini seçtiğini yaz(yazi or tura)", "$Topla sayi1(gir) sayi2(gir)","$Çarp sayi1(gir) sayi2(gir)", "$Böl sayi1(gir) sayi2(gir)" ,"$Çikart sayi1(gir) sayi2(gir)", "$Brainrot (yabanci veya Türkçe)"]
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='chat')
    await channel.send(f'Merhaba{member}! Sunucumuza hoşgeldin')
 

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
async def gönder(ctx):
    if ctx.message.attachments:
        for resim in ctx.message.attachments:
            await resim.save(f'./kaydetmeyeri/{resim.filename}')
            await ctx.send("Mesaj gönderildi")
            a, b = aswd.kod(f'./kaydetmeyeri/{resim.filename}')
            await ctx.send(f'bu bir{a},{b} ihtimali kadar eminim')
    else:
        await ctx.send("Herhangi bir resim göndermedin")

@bot.command()
async def ses(ctx):
    
    await ctx.send("Sesinizi dinliyorum")
    ses2 =  serhan.kontr()
    if ses2 != "Anlamadım, Tekrarla":
        await ctx.send(f"{ses2}, kelimesini söylediniz")
    else:
        await ctx.send("Anlamadım, Tekrarla")

    
@bot.command()
async def kaydet(ctx,*,c):
    with open("kayder.txt", "a", encoding="utf-8") as file:
        
        
        file.write(c)
    
    await ctx.send("Kelimenizi kaydettim")

    
@bot.command()
async def yazdir(ctx):
    with open("kayder.txt", "r", encoding="utf-8") as file:
        
        await ctx.send(file.read())
            

        
    
    await ctx.send("Kaydedilen kelimeler yazdırıldı.")

        
hayvanr = {"kedi" : "Kediler anatomik olarak güçlü, esnek bedenleriyle, hızlı refleksleriyle, keskin, geri çekilebilen pençeleriyle ve küçük avları öldürmeye uyarlanmış dişleriyle diğer kedigillere benzerler. Kediler, insan kulakları için çok zayıf ya da çok yüksek frekanstaki sesleri duyabilirler. Karanlığa yakın ortamlarda görebilirler.",
           "köpek" :"Köpek (Canis lupus familiaris[2]); köpekgiller (Canidae) familyasına ait, görünüş ve büyüklükleri farklı 400'den fazla ırkı olan, etçil bir memelidir. Bozkurt'un (C. lupus) alt türlerinden biri olan köpek, tilki ve çakallarla da yakın akrabalardır. Kedilerle birlikte dünyanın en geniş coğrafyaya yayılan ve en çok beslenen iki evcil hayvanından biridir. 2001 yılı tahminlerine göre dünyada 400 milyondan fazla köpek vardır.[3]",
           "fil": "Fil, hortumlular takımının filgiller familyasını oluşturan memeli bir hayvandır. Filler, Sahra altı Afrika ile Güney ve Güneydoğu Asya'da bulunur",
           "maymun":"Maymun, Primatlar takımındaki kimi memelileri kapsayan bir terimdir. Kimi kullanımlarda terim tüm primatları kapsarken genelde Simiiformes infra takımındaki primatlar için kullanılır. Maymunların birçok ayrı türü vardır. Bazı maymunlar dışında, genelde uzun ve sık ağaçların olduğu yerleri seçerler.",
           "kuş":"Kuş; tüyleri, dişsiz gagaları, yumurtladıkları sert kabuklu yumurtalar yoluyla üreyen, yüksek metabolizma hızına sahip, dört odacıklı kalpleri ve hafif ama güçlü bir iskelet yapısına sahip, Aves sınıfını oluşturan sıcakkanlı omurgalı hayvanlar grubudur.",
           "panda":"Dev panda veya sadece panda, ayıgiller familyasından, beyaz postu üzerinde bölge bölge siyah büyük benekleri olan, iri, nesli tehlikede olan bir ayı türü. Küçük pandadan ayrıt edebilinmesi için büyük panda veya sadece bambu ile beslendiğine dikkati çekmek için bambu ayısı da denilir.",
           "ayı":"Ayılar veya Ayıgiller, Ursidae familyasının etçil memelileridir. Ayılar Köpeğimsiler veya köpek benzeri etoburlar olarak sınıflandırılır. Her ne kadar sadece sekiz ayı türü mevcut olsa da, Kuzey yarımkürede ve kısmen Güney yarımkürede çok çeşitli habitatlarda görülürler.",
           "deve":"Deve, devegiller familyasının Camelus cinsini oluşturan iki evcil hayvan türünün ortak adı. Develer yük çeki ve binek hayvanı olarak kullanıldığı gibi, yünü, sütü, derisi ve eti için de beslenir. Yalnızca evcil türleriyle tanınan bu hayvanların yabanıl atalarından bu yana pek az değişikliğe uğradığı sanılmaktadır. ",



}

hayvanresim = {"kedi" : "kaydetmeyeri\kedi99.jpg",
           "köpek" :"kaydetmeyeri\köpke.jpg",
           "fil": "kaydetmeyeri\fil.jpg",
           "maymun":"kaydetmeyeri\maymun.jpg",
           "kuş":"kaydetmeyeri\kus.jpg",
           "panda":"kaydetmeyeri\panda.jpg",
           "ayı":"kaydetmeyeri\ayı.jpg",
           "deve":"kaydetmeyeri\deve.jpg",



}



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
async def hayvan(ctx, a):
    for k,v in hayvanr.items():
        
        if a.lower() == k:
            await ctx.send(f"{v}")
            with open(hayvanresim[k], "rb") as r:
                kb = discord.File(r)
                await ctx.send(file = kb)




bot.run(???)
