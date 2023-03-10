import discord 


TOKEN = 'MTA4MzMxNTA1MjM5Mzc5OTcyMA.GN8bt9.2dFCXgcNGEl9M_FhMIOGdJuCDtHmA0kjhPr-PI'

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


@client.event 
async def on_ready():
    print('logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')




client.run(TOKEN)
print("Bot has terminated")
