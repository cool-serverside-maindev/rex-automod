import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('mod!'))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("swear be gone"))
    print("Ready")

        
@bot.event
async def on_message(message):
    bad_words = ["fuck", "arschloch", "https://discord.gg", "http://disord.gg", "discord.gg", "fick", "arsch", "Arschgesicht", "arschgesicht", "Arschloch", "Asshole", "asshole", "Fotze", "fotze", "Miststück", "miststück", "Bitch", "bitch", "Schlampe", "schlampe", "Sheisse", "sheisse", "Shit", "shit", "Fick", "huren", "Verpiss", "verpiss", "masturbiert", "Idiot", "idiot", "depp", "Depp", "Dumm", "dumm", "jude", "Bastard", "bastard", "Wichser", "wichser", "wixxer", "Wixxer", "Hurensohn" "Wixer", "Pisser", "Arschgesicht", "huso", "hure", "Hure", "verreck" "Verreck", "fehlgeburt", "Fehlgeburt", "ficken", "adhs", "ADHS", "Btch", "faggot", "fck", "f4ck", "nigga", "Nutted", "flaschengeburt", "penis", "pusse", "pusse", "pussy", "pussys", "nigger", "kacke", "fuucker"]
    for word in bad_words:
        if message.content.count(word) > 0:
            await message.channel.purge(limit=1)
            await message.channel.send(f"stop swearing in my server BITCH! {message.author.mention}")

                          
bot.run(NzQ4NTkxODc0MDcxMTk5ODY2.X0fqgg.aEIFyxRb6jNWVi4CT-_T47Laqb0)
