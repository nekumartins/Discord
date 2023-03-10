import discord 
import random 

TOKEN ='MTA4MzMxNTA1MjM5Mzc5OTcyMA.GNDhqk.Rhtc3mnycWIycNU1ra42BkfPD2wi79FCpqqpDQ'

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event 
async def on_ready():
    print('Bot is online')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello there, did you wash your ass today')
        print(f"Message received: {message.content}")




client.run(TOKEN)