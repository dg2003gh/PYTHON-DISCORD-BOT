# DG2003-BOT-02.02.23

# *IMPORTS*.
import discord
import urllib.parse
import urllib.request
import re
from time import sleep
from random import randint
from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from discord.utils import get

# *INTENTS*.
intents = discord.Intents.all()
intents.members = True

# *PREFIX*.
bot = commands.Bot(command_prefix=commands.when_mentioned_or("'"), case_insensitive=True, intents=intents)


# *EVENTOS*
@bot.event
async def on_ready():  # AVISA QUANDO O BOT ESTÁ CONECTADO.
    print("\033[1;92mEstou Online como {0.user}\033[1;92m".format(bot))
    print(f"0=0" * 11)


@bot.event
async def on_member_join(member):  # ENVIA MENSAGEM DE BOAS-VINDAS NO CANAL DO SERVIDOR.

    canal = bot.get_channel(875785063646785576)
    regrasmbv = bot.get_channel(875787092741996554)

    embed = discord.Embed(
        description=f"{member.mention}, Entrou no servidor!😃 \n Seja muito bem-vindo!😁 \n 📚Digite:'ajuda para saber os"
                    f" meus comandos.📚 \nPor favor, Leia as regras do servidor em {regrasmbv.mention}.",
        colour=16753920
    )
    embed.set_thumbnail(url="https://media3.giphy.com/media/6dSwtLb9q1UuA/giphy.gif?cid"
                            "=ecf05e47j5e7vnlawaoqa5ioi7jk13knwjdvg6dgqiykfkvx&rid=giphy.gif&ct=g")
    embed.set_image(url="https://media0.giphy.com/media/9o59Pga7BWlDrzWhhh/giphy.gif?cid"
                        "=ecf05e47i4534lt8cmk8kq911vjd9syw67sx51m26lepynh5&rid=giphy.gif&ct=g")

    await canal.send(embed=embed)


# ----------------------------------------------------------------------------------------------------

#  *COMANDOS*

@bot.command()
async def ajuda(ctx):  # O COMANDO 'AJUDA LISTA OS COMANDOS DISPONÍVEIS.
    embed = discord.Embed(
        title=f"olá,{ctx.author}! Esta é a lista de comandos:",
        description="'ajuda: Mostra os comandos disponíveis.\n"
                    "'regras: Mostra as Regras do servidor.\n"
                    "'dado: Roda um dado.lembre-se de colocar o número de lados, EX:'dado 6.\n"
                    "'oi: Chama o bot.\n"
                    "'limpar: Limpa 5 mensagens do chat em que o usuário está.\n"
                    "'abreviações: Mostra as abreviações de alguns comandos.\n"
                    "'versão: Mostra a versão do BOT,Python,YTDL,FFMPEG e Discord.py.\n"
                    "'ping: O Servidor fica nos EUA, Se ele estiver demorando para responder,Pode ser o ping! \n "
                    "---------------------------------\n"
                    "UTILIZE OS SEGUINTES COMANDOS PARA CONTROLAR A MÚSICA (VOCÊ DEVE ESTAR EM UM CANAL DE VOZ PARA "
                    "QUE FUNCIONE):\n "
                    "'buscar: Procura no youtube a música a partir do que você digitar,\n"
                    "EX:'buscar the best of beethoven,(Você também pode pôr um link).\n"
                    "'pausar: Pausa a música.\n"
                    "'retomar: Retoma a música.\n "
                    "'parar: Para a música. \n"
                    "'sair: Faz o bot sair do canal de voz. \n"
                    "---------------------------------\n"
                    "Aproveite a música;)\n "
                    "---------------------------------------------------------------\n "
                    "Algum comando quebrado? Escreva uma mensagem mencionando @DG2003 ;) \n"
                    "Dica: O Bot não vê diferença entre maiúsculo e MINÚSCULO;)!\n"
                    "USE APÓSTROFO(') ANTES DE QUALQUER COMANDO!",
        colour=16753920
    )
    embed.set_thumbnail(url="https://media1.giphy.com/media/WoWm8YzFQJg5i/giphy.gif?cid"
                            "=ecf05e47cczfx3jwu3x3pgqhurz8ybv0f8t3juw53vs2hfag&rid=giphy.gif&ct=g")
    await ctx.send(embed=embed)


# ----------------------------------------------------------------------------------------------------


@bot.command(aliases=["a", "abre"])
async def abreviações(ctx):  # LISTA ALGUMAS ABREVIAÇÕES/FORMAS DIFERENTES DE ESCREVER.
    embed = discord.Embed(
        title=f"Olá,{ctx.author}!",
        description="ESTAS SÃO AS ABREVIAÇÕES/FORMAS DIFERENTES DE ESCREVER DE ALGUNS COMANDOS: \n"
                    "---------------------------------\n"
                    "'abreviações = 'a \n"
                    "'limpar = 'l \n"
                    "'dado = 'd \n"
                    "'versão = 'ver \n"
                    "---------------------------------\n"
                    "COMANDOS DA MÚSICA: \n"
                    "'buscar = 'procurar, 'youtube, 'tocar, 'link, 'proc, 'bus, 'url, 't, 'b, 'u \n"
                    "'volume = 'vol, 'v \n"
                    "'pausar = 'pau ou 'p \n"
                    "'retomar = 'ret ou 'r \n"
                    "'parar = 'par ou 'pa \n"
                    "'sair = 'sai ou 's \n"
                    "---------------------------------------------------------------\n"
                    "Algum comando quebrado? Escreva uma mensagem mencionando @DG2003 ;)",
        colour=16753920
    )
    embed.set_thumbnail(url="https://media0.giphy.com/media/NFA61GS9qKZ68/giphy.gif?cid"
                            "=ecf05e47d17jkne8fy7e5dic2oa0uz9kvpvvj0okrt1x4nxg&rid=giphy.gif&ct=g")

    await ctx.send(embed=embed)


# ----------------------------------------------------------------------------------------------------


@bot.command()
async def regras(ctx):  # MOSTRA AS REGRAS DO SERVIDOR.
    embed = discord.Embed(
        title="😎SIGA AS SEGUINTES REGRAS E SEJA UM CARA LEGAL😎: ",
        description="1- NÃO SERÁ TOLERADO NENHUM TIPO DE DISCRIMINAÇÃO(RACISMO, SEXISMO ETC...)😡 😡 😡 "
                    ".TUDO BEM BRINCAR E "
                    "FAZER "
                    "PIADAS, MAS A PARTIR DO MOMENTO QUE O OUTRO NÃO RI E FICA TRISTE COM ISSO, DEIXA DE SER LEGAL! \n"
                    "------------------------------------------------------- \n"
                    "2- SPAMAR MENSAGENS, EMOJIS ETC... SE VOCÊ ESTIVER ANSIOSO COM ALGO E QUISER QUE TODOS SAIBAM, "
                    "MAS NINGUÉM TE DÁ ATENÇÃO, ESPERE, SPAMAR NÃO VAI FAZER COM QUE AS PESSOAS VEJAM O QUE VOCÊ QUER "
                    "MOSTRAR,APENAS VAI FAZER COM QUE ELAS TE ACHEM CHATO E INCOVENIENTE! VAI COM CALMA, AMIGÃO! \n"
                    "------------------------------------------------------- \n"
                    "3- TENTE NÃO XINGAR🤬🤬🤬! EU SEI QUE ÀS VEZES É DIFICIL(ESPECIALMENTE PARA MIM😅😅😅) E "
                    "QUE ESCAPA, "
                    "MAS É UMA BOA PRATICA!😄😄😄\n"
                    "------------------------------------------------------- \n"
                    "É SÓ ISSO! VIU COMO É FÁCIL SER LEGAL😎😎😎?",
        colour=16753920
    )
    embed.set_thumbnail(url="https://media0.giphy.com/media/WXvzV4oAjmwe6BqVHu/giphy.gif?cid"
                            "=ecf05e470pbix0o4q7bflm5671mv0xz4doxr161z3j2jbyal&rid=giphy.gif&ct=g")

    embed.set_image(url="https://media4.giphy.com/media/t6CEhjycZ0ABG/giphy.gif?cid"
                        "=ecf05e479n1owaemh0bht3q7193mfc2gm51bxi2aqzbis8tp&rid=giphy.gif&ct=g")

    await ctx.send(embed=embed)


# ----------------------------------------------------------------------------------------------------

@bot.command()
async def oi(ctx):  # DIZ OI?  ¯ \ _ (ツ) _ / ¯
    embed = discord.Embed(
        title=f"oi,{ctx.author}!😄",
        color=16753920
    )
    await ctx.send(embed=embed)


@bot.command(aliases=["l"])
async def limpar(ctx, amount=5):  # LIMPA O CHAT DO USUÁRIO(APENAS 5 MENSAGENS DE UMA VEZ):
    await ctx.channel.purge(limit=amount)


@bot.command(alises=["d"])
async def dado(ctx, numero):  # RODA UM DADO ALEATÓRIO PARA O USUÁRIO!
    variavel = randint(1, int(numero))
    embed = discord.Embed(
        title="🎲Balançando os dados...🎲",
        color=16753920
    )
    embed2 = discord.Embed(
        title=f"🎲 O número do seu dado é {variavel}!",
        color=16753920
    )

    await ctx.send(embed=embed)
    sleep(3)
    await ctx.send(embed=embed2)


@bot.command()
async def hello(ctx):  # MANDA UMA PIADINHA COM HELLO WORLD KKKKKKK.
    embed = discord.Embed(
        title="worlddddddddddddddddddd!🗺️ programmed to work and not to feel ... not even sure that this is "
              "real...🤖🤖\n"
              "Foi mal \n"
              "me empolguei😂😂",
        color=16753920
    )

    await ctx.send(embed=embed)


@bot.command(aliases=["ver"])
async def versão(ctx):
    embed = discord.Embed(
        title="🤖 Versão: 02.02.23 \n"
              "------------------------\n"
              "📑 Discord.py: 1.7.3 \n"
              "🎞️ FFMPEG: 4.4.1 \n"
              "🐍 Python: 3.10 \n"
              "📹 YTDL: 2021.12.17 \n",
        color=16753920
    )
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    embed = discord.Embed(
     title=f"🏓 Pong!🤣🤣 Desculpa... Não resisti! \n"
           f"O Ping do servidor está em {round(bot.latency * 1000)}ms!",
     color=16753920

    )
    await ctx.send(embed=embed)

# ----------------------------------------------------------------------------------------------------


# *PARTE "DJ" DO BOT*

@bot.command(aliases=["proc", "youtube", "bus", "tocar", "procurar", "t", "b", "url", "u", "link"])
async def buscar(ctx, *, search):  # BUSCA MÚSICA NO YOUTUBE.

    ydl_opcs = {"format": "bestaudio", "noplaylist": False, "default_search": "auto"}
    ffmpeg_opcs = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
    voz = get(bot.voice_clients, guild=ctx.guild)
    canal = ctx.message.author.voice.channel

    embed = discord.Embed(
        title="😄Um segundo...😄 \n"
              "🔎Procurando a melhor versão pra você...🔍 \n"
              "✨Achei!✨",
        colour=16753920
    )

    query_string = urllib.parse.urlencode({
        "search_query": search
    })
    html = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    resultados = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    urlb = f"http://www.youtube.com/watch?v={resultados[0]}"  # FORMA A URL QUE SERÁ ULTILIZADA PRA REPRODUZIR A MÚSICA.

    if voz and voz.is_connected():  # ENTRA NO CANAL EM QUE O USUÁRIO ESTÁ.
        await voz.move_to(canal)
    else:
        voz = await canal.connect()

    await ctx.send(embed=embed)

    # TOCA A MÚSICA ATRÁVES DE UMA URL GERADA A PARTIR DE FRASE OU PALAVRA QUE O USUÁRIO
    # DIGITA(TAMBÉM FUNCIONA COM URL(LINK)).  ↓↓↓
    if not voz.is_playing():
        with YoutubeDL(ydl_opcs) as ydl:
            info = ydl.extract_info(urlb, download=False)
            url = info["url"]
            titulo = info.get("title", None)
            capa = info.get("thumbnail", None)
            duração = info.get("duration", None)
            data = info.get("upload_date", None)
            # visualizações = info.get("view_count", None)
            du = str(duração / 61.6)
            d = str(data)

        voz.play(FFmpegPCMAudio(url, **ffmpeg_opcs))
        voz.is_playing()
        voz.source = discord.PCMVolumeTransformer(voz.source, volume=0.50)

        embed = discord.Embed(
            title=f"🎶Tocando: {titulo}",
            description=f"📅 Data: {d[6:8]}/{d[4:6]}/{d[0:4]} ------ 🕛 Duração: {du[0:1]}:{du[2:4]} Min",
            color=16753920
        )
        embed.set_image(url=capa)

        await ctx.send(embed=embed)


@bot.command(aliases=["vol", "v"])
async def volume(ctx, _volume: int):  # MUDA O VOLUME.
    ctx.voice_client.source.volume = _volume / 100
    embed = discord.Embed(
        title=f"🔉 Volume em {_volume}% 🎚️",
        colour=16753920
    )
    embed2 = discord.Embed(
        title=f"🔊 Volume em {_volume}% 🎚️",
        colour=16753920

    )

    if _volume <= 50:
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=embed2)


@bot.command(aliases=["pau", "p"])
async def pausar(ctx):  # PAUSA A MÚSICA.
    voz = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    embed = discord.Embed(
        title="⏸A música está pausada!",
        color=16753920
    )
    embed2 = discord.Embed(
        title="🔇Nenhuma música está tocando.",
        color=16753920

    )
    if voz.is_playing():
        voz.pause()
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=embed2)


@bot.command(aliases=["ret", "r"])
async def retomar(ctx):  # RETOMA A MÚSICA.
    voz = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    embed = discord.Embed(
        title="🔊A música foi retomada!",
        color=16753920
    )
    embed2 = discord.Embed(
        title="🚫A música não está pausada, Uma vez que foi removida da lista de reprodução através do comando 'parar.",
        color=16753920

    )
    if voz.is_paused():
        voz.resume()
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=embed2)


@bot.command(aliases=["par", "pa"])
async def parar(ctx):  # PARA A MÚSICA.
    voz = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    embed = discord.Embed(
        title="⏹️ Alguém tirou a música!",
        color=16753920
    )
    voz.stop()
    await ctx.send(embed=embed)


@bot.command(aliases=["sai", "s"])
async def sair(ctx):  # SAI DO CANAL DE VOZ.
    voz = get(bot.voice_clients, guild=ctx.guild)
    canal = ctx.message.author.voice.channel
    embed = discord.Embed(
        title=f"️Fui desconectado do canal de voz  {canal}!  👋👋👋",
        color=16753920
    )
    embed2 = discord.Embed(
        title="🚫Não estou em um canal de voz para ser desconectado!",
        color=16753920
    )
    if voz.is_connected():
        await voz.disconnect()
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=embed2)


# ----------------------------------------------------------------------------------------------------


# *TOKEN DO BOT*
bot.run("MTA1MzIwMjM1Mzk1Nzg5NjMyMw.Gm9NEI.yH9XxvXsNWBmNwXbcr70m4D12uFxFyVz41Kqn0")
