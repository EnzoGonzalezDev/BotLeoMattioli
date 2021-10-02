import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json
import random
import wikipedia
import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKENW = os.getenv('WIKI_TOKEN')

wikipedia.set_lang("es")

bot = commands.Bot(command_prefix='!')

@bot.command(name="wiki")
async def search(ctx,busq="",busq2="", busq3=""):
    busqF = busq +" "+ busq2 +" "+ busq3
    resultado2 = wikipedia.summary(busqF, sentences=5)
    await ctx.send("I found this for your search for "+busqF+": "+resultado2)


@bot.command(name="i")
async def img(ctx):
    album = [
        'https://d35hsl9am8s2ta.cloudfront.net/public/images/2020/08/15965092590-Leo-Mattioli-773x458.jpg',
        'https://lh3.googleusercontent.com/proxy/NeiC4m5pUP3V37cAamsSQVhvSmt2mRZlZmNlUJIqwaWM7vjB1J1JeKteLxVovOIiszbRmM3QBT3KdeXJgOUdJR0jw0DE0xUmDoFXxto4ewPq0iAlWmcBtNOlLiD4vQH2tsw',
        'https://img.discogs.com/qhnZnciiE27BwIFUFX0ETJJ_7Ks=/fit-in/500x500/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-14758565-1581022462-7678.jpeg.jpg',
        'https://i1.sndcdn.com/artworks-000112054838-wb7h4f-t500x500.jpg',
        'https://www.cmtv.com.ar/imagenes_artistas/1540.jpg',
        'https://www.cmtv.com.ar/tapas-cd/leomattioliamor.jpg'
    ]
    frase = [
        'El rey del amor',
        'Hasta morir de placer',
        'Lo más bueno del amor',
        'El ultimo romantico',
        'Un seductor',
        'Amor a mi manera!'
    ]
    response = random.choice(album)
    respons = random.choice(frase)
    await ctx.send(respons)
    await ctx.send(response)



@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('p o n g!')


@bot.command(name='info')
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="VirgoGang, un servidor activo desde 12/06/2020!", timestamp=datetime.datetime.utcnow(), color=discord.Color.blurple())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://d35hsl9am8s2ta.cloudfront.net/public/images/2020/08/15965092590-Leo-Mattioli-773x458.jpg")
    await ctx.send(embed=embed)



@bot.command(name='f')
async def fras(ctx):
    response = random.choice (["Es como estar con un angel que te abraza con sus alas...",
    "Si te cansaste de andar en amoríos, no me enojo si quieres quedarte conmigo !",
    "Otro día más aquí en mi vida, esperando tu llamada para vernos a escondidas...",
    "Y en la habitación, ya no se escucharan esos gritos de placeeeer !",
    "Y deja el orgullo a un costado, ponte la mano en el corazón y vuelve a mi lado...",
    "Y poder mirarte a los ojos y decirte AY AMOR !",
    "Necesito verte hoy y confesarte mi amor, necesito oír tu voz, me hace falta estar con vos...",
    "Es tiempo y es hora de cambiar,  nunca es tarde para empezar,  es hora de que me olvide de ti,  es hora de que piense un poco en mi...",
    "Que nos revolcábamos en el amor la noche entera...y te gustaba como lo hacia yo, de mil maneras...",
    "Y se que lloraras...",
    "Y aun te estaba esperando, pero bueno...CHAU !",
    "Creo que es mejor seguir solo esta vez...",
    "Me enamore como un adolescente...",
    "Que fue mi culpa ya lo se, que no te supe aprovechar..."])
    await ctx.send(response)


@bot.event
async def on_ready():
    print('My Ready is Body')

bot.run(TOKEN)