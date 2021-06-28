import discord
from discord.ext import commands
from config import settings
from random import randint
from asyncio import sleep
bot = commands.Bot(command_prefix = settings['prefix'])


@bot.event
async def on_ready():
     while True:
          await bot.change_presence(status=discord.Status.online, activity=discord.Game("Создатель Koffi#1077 | ch?helpme"))
@bot.command()
async def photo(ctx):
    randomPhotoDiscord = randint(1, 39)
    if randomPhotoDiscord == 1:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853299234685845534/Swiss_Male.webp')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 2:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853308799300927528/0aeeb700f4b6381f3b205540f9d70cde.webp')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 3:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853309060090560522/4dc9b799ec153113594571c6d4a47a8b.webp')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 4:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853309362852724766/DLKDL.png')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 5:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853309362852724766/DLKDL.png')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 6:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853309669048057886/El_Salvador_by_samy275_on_tumblr.png')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 7:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853310136202166272/Japanboi.webp')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 8:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853310277235638322/Male_Ukraine.webp')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 9:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853310582262595614/Soviet_Union.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 10:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853310762134143016/United_Kingdom.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 11:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853310891364450304/VqjcmkNfgAU.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 12:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853310902275407952/webp.png')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 13:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853312636716318730/Sanek_molodes-_BuFwfDGnBQS_-.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 14:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853340908031967282/1e80e6b1cbd1f684545aeb51e5cc10aa.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 15:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853341173673099284/25c2e3d846fb1819a0cdb6290510cd7c.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 16:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853341828190830592/66a1501a07bc1f0b671c2589b2389c34.png')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 17:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853341998164606986/b1a9dea9-b8ba-49a5-89bc-0765a4681339.png')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 18:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853342205121265685/d21785029648477b46d4dfbf86d07f80.jpg')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 19:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853342516333248532/dae9c86976656e945f8efae392c6107f.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 20:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853342717849108520/images_indexes.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 21:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853342877558898719/index_228.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 22:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853343213065338900/index_ana.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 23:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853343437969031168/index_fra.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 24:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853343783352401960/index_jpg.jpg')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 25:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853343796371390534/index_restorer.png')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 26:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853344261771493397/Norways.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 27:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853344278365601842/tumblr_0d4a57200d656f0f9bb84f1ce92ab7f1_e3d26bae_1280.png')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 28:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853569448212693062/PanamaMale.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 29:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853570131099648030/KmVHKzOQ2wo.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 30:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853570184924233748/Malaysia_.webp')
        await ctx.send(embed = embed) 
    elif randomPhotoDiscord == 31:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/832685123296034836/853570194604818432/Malta_by_kyukerns_dcvo5zy-pre.webp')
        await ctx.send(embed = embed)  
    elif randomPhotoDiscord == 32:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/858699050399301683/858713199750676540/countryhumans___australia_by_spookyspookyshark_ddlm3zh-fullview.jpg')
        await ctx.send(embed = embed)  
    elif randomPhotoDiscord == 33:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/858699050399301683/858713279937118208/Fe59dac4204791a879756f2ec9d61b7f748721b4r1-1181-1181v2_00.webp')
        await ctx.send(embed = embed)          
    elif randomPhotoDiscord == 34:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/858699050399301683/858716352248283136/imagesus.jpg')
        await ctx.send(embed = embed)        
    elif randomPhotoDiscord == 35:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/858699050399301683/858716371118194698/images_np.jpg')
        await ctx.send(embed = embed)
    elif randomPhotoDiscord == 36:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/858699050399301683/858716394467229716/index123.jpg')
        await ctx.send(embed = embed)  
    elif randomPhotoDiscord == 37:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/858699050399301683/858716404542603294/index_not.jpg')
        await ctx.send(embed = embed)  
    elif randomPhotoDiscord == 38:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/858699050399301683/858716419977642004/media_EzAaLpHWUAQG3T7.jpg_namesmall.jpg')
        await ctx.send(embed = embed)  
    elif randomPhotoDiscord == 39:
        embed = discord.Embed(color = 0xff9900, title = 'Random Photo. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/827184889337872386/859098623224447016/images_sv.jpg')
        await ctx.send(embed = embed)  
        
        
@bot.command()
async def wiki(ctx, arg1):
    if arg1 == 'russia':
        embed = discord.Embed(color = 0xff9900, title = 'CountryHumans Wiki. Contact: chdiscordbot@gmail.com ')
        embed.description = open(r'./wiki/Russia.txt', encoding='utf-8').read()
        await ctx.send(embed = embed) 
    elif arg1 == 'usa':
        embed = discord.Embed(color = 0xff9900, title = 'CountryHumans Wiki. Contact: chdiscordbot@gmail.com ')
        embed.description = open(r'./wiki/USA.txt', encoding='utf-8').read()
        await ctx.send(embed = embed) 
    elif arg1 == 'germany':
        embed = discord.Embed(color = 0xff9900, title = 'CountryHumans Wiki. Contact: chdiscordbot@gmail.com ')
        embed.description = open(r'./wiki/Germany.txt', encoding='utf-8').read()
        await ctx.send(embed = embed) 
    elif arg1 == 'poland':
        embed = discord.Embed(color = 0xff9900, title = 'CountryHumans Wiki. Contact: chdiscordbot@gmail.com ')
        embed.description = open(r'./wiki/Poland.txt', encoding='utf-8').read()
        await ctx.send(embed = embed)
@bot.command()
async def meme(ctx):
    random__ = randint(1, 13)
    if random__ == 1:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/849340636754739285/853640780711067648/f706f880be3bd8c6ae8730d387e07a7d.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 2:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641602688614412/3d98c78ac795317769cf1d598ceae8a1.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 3:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641789604888636/7e1ba3dbdce6e20a8c9bd088b8097bcb.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 4:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641803059429426/7bfca97fe71b897085709d1e23e28324f084f0b1r1-1500-1500v2_uhq.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 5:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641807619031090/8dbd694165269d7e796d4b6a60d4c9f8.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 6:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641827528605747/a4d7eb6dfcf067444a7224fd67613bd990bd666fr1-768-768v2_uhq.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 7:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641861192745009/e401129349f9ff627898151e2f5149fe.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 8:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641982982488084/YRrhSMSv.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 9:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641899633934346/f706f880be3bd8c6ae8730d387e07a7d.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 10:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641902477148160/f29f8b3fb221d9e4843981cfc657c8d6.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 11:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/727586301410410528/853641956906369074/images.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 12:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/827184889337872386/859100895319949312/belarus__countryhumans__by_dexelsarts_dedalu1-fullview.jpg')
        await ctx.send(embed = embed)   
    elif random__ == 13:
        embed = discord.Embed(color = 0xff9900, title = 'Random MEME. Contact: chdiscordbot@gmail.com ')
        embed.set_image(url='https://cdn.discordapp.com/attachments/827184889337872386/859097463641997382/4qzdyg.png')
        await ctx.send(embed = embed)   
@bot.command()
async def helpme(ctx):
    embed = discord.Embed(color = 0xff9900, title = 'Help. Contact: chdiscordbot@gmail.com ')
    embed.description = "ch?meme - Random meme \n ch?photo - Random photo \n ch?wiki [country] - CountryHumans wiki \n ch?help - Help"
    await ctx.send(embed = embed)   
bot.run(settings['token'])
    
