import discord
from discord.ext import commands
from random import randint
import os
import json
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix=".", intents=intents)


async def escrevendo_json(nome=None, ids=None, escrever=False, retirar=False, pegar=False, lista=False):
    if escrever: #funcionando
        completo = f'"{nome}": {ids}' + r"}" + "\n"

        conteudo = open("admins.json", "r").read()
        admins = json.loads(conteudo)
        admins = admins["admins"]
        teste = json.dumps(admins)
        teste = teste.replace("}", "")
        teste = f"{teste}, {completo}"
        json_pronto = r"""
{
    "admins": {
        hipopotamo
    }
}
"""
        teste = teste.replace(r"{", "")
        teste = teste.replace(r"}", "")
        json_pronto = json_pronto.replace("hipopotamo", teste)
        with open("admins.json", "w+") as f:
            f.write(json_pronto)
    elif pegar:
        conteudo = open("admins.json", "r").read()
        admins = json.loads(conteudo)
        admins = admins["admins"]
        try:
            hasdk = admins[nome]
        except:
            return False
        else:
            return True

    elif lista:
        conteudo = open("admins.json", "r").read()
        admins = json.loads(conteudo)
        admins = admins["admins"]
        return list(admins)

    elif retirar: #Funcionando
        if ids == 810894152795553863:
            return "Esse é o adm"
        else:
            completo = f'"{nome}": {ids}'
            conteudo = open("admins.json", "r").read()
            teste = json.loads(conteudo)
            #conteudo = conteudo.replace(completo, "")
            teste = json.dumps(teste["admins"])
            teste = teste.replace(r"}", "").replace(r"{", "")
            teste = teste.split(",")
            for c in range(0, len(teste)):
                try:
                    if teste[c][0] != '"':
                        opa = teste[c]
                        teste[c] = opa[1:]
                except:
                    pass

                if teste[c] == completo:
                    del teste[c]
                    break
            for c in range(0, len(teste)):
                if teste[c][0] != '"':
                    opa = teste[c]
                    teste[c] = opa[1:]
            teste = str(teste)[2:len(str(teste)) - 2] #Percebi mudanças
            #teste = r"{" + teste + r"}"
            cara = """
{
    "admins": {
        batata

    }
}"""
            cara = cara.replace("batata", teste).replace("'", "") #Cara é o json completo com o admin retirado.
            with open("admins.json", "w+") as f:
                f.write(cara)


@client.event
async def on_error(event):
    canal_certo = client.get_channel(864007326251745300)
    await canal_certo.send(f"Erro em {event}")


@client.event
async def on_ready():
    print(f"Entrei no servidor como {client.user}.")
    game = discord.Game(".ajuda")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_member_join(member):
    print(member)
    boas_vindas = client.get_channel(864031592012054529)
    servidor = client.get_guild(826678092470681610)
    #req = requests.get(member.avatar_url)
    #imagem = Image.open(BytesIO(req.content))
    #imagem = imagem.resize((150, 150))
    #imagem.save("avatar.png")
    #imagem = None
    embed = discord.Embed(
        title=f"🥶 Sejá bem vindo ao {servidor} @{member}!🥶",
        description="Espero que se divirta",
        color = discord.Color.blue()
    )
    embed.set_footer(text="Comprimentos do ADM")
    embed.set_author(name=f"{member.name}", icon_url=member.avatar_url)
    embed.set_image(url=member.avatar_url)
    await boas_vindas.send(embed=embed)

@client.event
async def on_member_remove(member):
    print(member) 
    tchau = client.get_channel(864031724740411442)
    servidor = client.get_guild(826678092470681610)
    embed = discord.Embed(
        title=f"😭 @{member} saiu do servidor 😭",
        description="É uma pena, espero que volte um dia.",
        color = discord.Color.red()
    )
    embed.set_footer(text="Comprimentos do ADM")
    embed.set_author(name=f"{member.name}", icon_url=member.avatar_url)
    embed.set_image(url=member.avatar_url)
    await tchau.send(embed=embed)
    #mensagem = await tchau.send(f"😭 {member.author} saiu do servidor 😭")

@client.event
async def on_member_update(before, after):
    if after.name != "Lorrita" or not after.bot:
        print("Percebi mudanças")
        if before.name != after.name:
            descricao = f"Fomos de {before.name} para {after.name}."
        else:
            if after.status != "":
                descricao = after.status
            else:
                descricao = "Casada adaptada :))"
        embed = discord.Embed(
            title=f"Parece que temos mudanças em @{after}",
            description=descricao,
            color = discord.Color.green()
        )
        adm = client.get_user(810894152795553863)
        embed.set_footer(text="Comprimentos do ADM", icon_url=adm.avatar_url)
        embed.add_field(name="Foto nova", value="↓", inline=False)
        embed.set_image(url=after.avatar_url)
        canal = client.get_channel(864751303619117107)
        await canal.send(embed=embed)

@client.command()
async def carrossel(ctx):
    print(ctx.author.id)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if voice.is_connected():
            await voice.disconnect()
    except:
        pass
    finally:
        canais = client.get_all_channels()
        for c in canais:
            canal = client.get_channel(c.id)
            try:
                for membro in canal.voice_states:
                    if membro == ctx.author.id:
                        print(c)
                        print(ctx.guild.voice_channels)
                        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=str(c))
                        await voiceChannel.connect()
                        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
                        voice.play(discord.FFmpegPCMAudio("song.mp3"))
            except Exception as erro:
                print(erro)

@client.command()
async def nobru(ctx):
    print(ctx.author.id)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if voice.is_connected():
            await voice.disconnect()
    except:
        pass
    finally:
        canais = client.get_all_channels()
        for c in canais:
            canal = client.get_channel(c.id)
            try:
                for membro in canal.voice_states:
                    if membro == ctx.author.id:
                        print(c)
                        print(ctx.guild.voice_channels)
                        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=str(c))
                        await voiceChannel.connect()
                        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
                        voice.play(discord.FFmpegPCMAudio("nobru_apelao.mp3"))
            except Exception as erro:
                print(erro)

@client.command()
async def dar(ctx):
    print(ctx.author.id)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if voice.is_connected():
            await voice.disconnect()
    except:
        pass
    finally:
        canais = client.get_all_channels()
        for c in canais:
            canal = client.get_channel(c.id)
            try:
                for membro in canal.voice_states:
                    if membro == ctx.author.id:
                        print(c)
                        print(ctx.guild.voice_channels)
                        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=str(c))
                        await voiceChannel.connect()
                        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
                        voice.play(discord.FFmpegPCMAudio("nao_vou_dar_para_tras.mp3"))
            except Exception as erro:
                print(erro)

@client.command()
async def admin(ctx):
    if ".admin add" in ctx.message.content:
        print("Nome: {}, Id: {}".format(ctx.author, ctx.author.id))
        opa = await escrevendo_json(str(ctx.author), int(ctx.author.id), pegar=True) #Testa se o usario que digitou o comando é um admin
        canal = ctx.channel
        if opa:
            mensagem = ctx.message.content.replace(".admin add", "")
            try:
                ids = int(mensagem)
            except:
                await canal.send("Comando invalido, o 2° Argumento deve ser o ID do usuario.")
            else:
                usuario = client.get_user(ids)
                user_name = f"{usuario.name}#{usuario.discriminator}"
                opa2 = await escrevendo_json(str(user_name), int(ids), pegar=True)
                if opa2:
                    await canal.send(f"{usuario.name} já é um admin")
                else:
                    print("Estou adicionando {}, minha outra opção é {}".format(user_name, usuario.name))
                    opa = await escrevendo_json(str(user_name), ids, escrever=True)
                    await canal.send(f"{usuario.name} é um admin agora.")
        else:
            await canal.send(f"Não é possivel executar esse comando. {ctx.author} não é admin.")

    elif ".admin remove" in ctx.message.content:
        opa = await escrevendo_json(str(ctx.author), int(ctx.author.id), pegar=True) #Testa se o usario que digitou o comando é um admin
        canal = ctx.channel
        if opa:
            mensagem = ctx.message.content.replace(".admin remove", "")
            try:
                ids = int(mensagem)
            except:
                await canal.send("Comando invalido, o 2° Argumento deve ser o ID do usuario.")
            else:
                if ids == 810894152795553863:
                    await canal.send("Desculpe, não posso tirar meu dono. Ele é muito gostoso para isso.")
                else:
                    usuario = client.get_user(ids)
                    user_name = f"{usuario.name}#{usuario.discriminator}"
                    opa2 = await escrevendo_json(str(user_name), int(ids), pegar=True)
                    if opa2:
                        print("Estou retirando {}, minha outra opção é {}".format(user_name, usuario.name))
                        opa = await escrevendo_json(str(user_name), ids, retirar=True)
                        await canal.send(f"{usuario.name} não é mais um admin.")
                    else:
                        await canal.send(f"{usuario.name} não é um admin kkkkk, burrão")
        else:
            await canal.send(f"Não é possivel executar esse comando. {ctx.author.name} não é admin.")
    
    elif ".admin list" in ctx.message.content:
        opa = await escrevendo_json(str(ctx.author), int(ctx.author.id), pegar=True) #Testa se o usario que digitou o comando é um admin
        adm = client.get_user(810894152795553863)
        canal = ctx.channel
        if opa:
            opa2 = await escrevendo_json(lista=True)
            embed = discord.Embed(
                title=f"Lista de ADMs",
                color = discord.Color.green()
            )
            embed.set_footer(text="Comprimentos do ADM", icon_url=adm.avatar_url)
            for c in opa2:
                embed.add_field(name=c, value="🐊", inline=False)
            await canal.send(embed=embed)
        else:
            await canal.send(f"Não é possivel executar esse comando. {ctx.author.name} não é admin.")

@client.command()
async def comprimentos(ctx):
    print(ctx.message.content)
    nick = str(ctx.author).split("#")
    nick = nick[0]
    lista = (f"To comendo o cu do @{nick}", f"@{nick} é viado.", f"@{nick} me da o botico", f"Por que me acordas @{nick}?", "Comi o cu de quem ta lendo", f"{nick} me mama", f"{nick} pega no meu pau", "Vou pegar no seu pau, quer dizer... Vou pegar você no pau")
    num = randint(0, len(lista) - 1)
    await ctx.send(lista[num])
    print(f"Respondi o {ctx.author}")

@client.command()
async def ajuda(ctx):
    print(ctx.channel)
    adm = client.get_user(810894152795553863)
    print(adm)
    embed = discord.Embed(
        title="Enfim, meus comandos são esses:",
        description="Comi o cu de quem ta lendo",
        color = discord.Color.green(),
    )
    embed.set_footer(text="Comprimentos do ADM", icon_url=adm.avatar_url)

    embed.add_field(name=".ajuda", value="Abre uma tabela de ajuda.", inline=False)
    embed.add_field(name=".palavra", value="Gera uma palavra aleatoria.", inline=False)
    embed.add_field(name=".comprimentos", value="Eu te comprimento", inline=False)
    embed.add_field(name=".fala '<o que vc quer que eu fale>'.", value="Eu digo", inline=False)
    embed.add_field(name=".admin", value="Você tem permissões sobre mim? descubra.", inline=False)
    embed.add_field(name=".admin add (ID do usuario)  //ADM", value="Da permissões administradoras ao usuario", inline=False)
    embed.add_field(name=".admin remove (ID do usuario)  //ADM", value="Tira permissões administradoras do usuario", inline=False)
    embed.add_field(name=".nobru  //ADM", value="Nobru apelão estourado", inline=False)
    embed.add_field(name=".dar", value="Não vou dar para tras...", inline=False)
    embed.add_field(name=".carrossel", value="Musica do carrossel versão funk kkkk", inline=False)
    embed.add_field(name=".pausar", value="pausa a musica", inline=False)
    embed.add_field(name=".resume", value="Volta a musica", inline=False)
    embed.add_field(name=".parar", value="sai da musica", inline=False)
    embed.set_image(url="https://poltronanerd.com.br/wp-content/uploads/2020/10/Shrek-1.jpg")
    await ctx.send(embed=embed)

@client.command()
async def fala(ctx):
    mensagem = ctx.message.content
    mensagem = str(mensagem).replace(".fala", "")
    n1 = "godoy" in mensagem.lower()
    n2 = "phgodoycosta" in mensagem.lower()
    if n1 or n2 == True:
        await ctx.send("Não tenho permissão para falar do meu dono. Ele fica bravo comigo")
    else:
        await ctx.send(mensagem)

@client.command()
async def disconectar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Você é burro?! kkkkk, to nem em canal de voz")

@client.command()
async def palavra(ctx):
    req = requests.get("https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1&fs2=0&Submit=Nova+palavra")
    soup = BeautifulSoup(req.text, 'html.parser')
    tbody = soup.find("td")
    palavra = tbody.find("div")
    await ctx.send(palavra.text)

@client.command()
async def pausar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Preciso falar alguma coisa?")


@client.command()
async def parar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


client.run('Aqui estava o token do sherek_indiano :)')
