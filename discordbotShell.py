import discord
import subprocess
from discord.ext import commands
# to call the shell we'll use /shell args
bot = commands.Bot(command_prefix='/')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def shell(ctx,*args):
		
	
		ext=subprocess.run(list(args),capture_output=True)
		
		await ctx.send(str(ext.stdout.decode("UTF-8")))
		
#change bot.run args to your bot's token
bot.run('ODkzNTAzMjg2ODY5NjI2ODkw.YVcZyA.OvLCQJ02Z2UvRvKtfulNoCtgsgc')
