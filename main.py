import settings
import discord 
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='#', intents=intents)

    @bot.event
    async  def on_ready():
        logger.info(f"User: {bot.user}")

    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")
        
    bot.run(settings.SECRET, root_logger=True) 





    
    







if __name__ == "__main__":
    run()
    

