import settings
import discord 
import random as rd
from discord.ext import commands
import sqlite3 as sql

con = sql.connect("peaches.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS questions(question TEXT)")
con.commit()
con.close()

logger = settings.logging.getLogger("bot")

numbers = [1,2,3,4,5,6,7,8,9,10]
coin = ["Heads", "Tail"]

questions = "truths.txt"

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='#', intents=intents)


	
    @bot.event
    async  def on_ready():
        logger.info(f"User: {bot.user}")

    @bot.command()
    async def ping(ctx):
        """Sends a pong response"""
        await ctx.send("pong")

    @bot.command()
    async def hello(ctx):
        """This is a test feature"""
        await ctx.send("Good day, Have you washed your ass today ")

    @bot.command()
    async def echo(ctx, *what):
        await ctx.send(" " .join(what))

    @bot.command()
    async def riley(ctx):
        """supreme commander riley"""
        await ctx.send("What do you know about the supreme leader of the peaches guild") 

    @bot.command()
    async def random(ctx):
        """Supposedly sends you a random number from answers""" 
        num = rd.choice(numbers)
        await ctx.send(f"Your lucky number is {num}")
		
    

    bot.run(settings.SECRET, root_logger=True) 





    
    







if __name__ == "__main__":
    run()
    


