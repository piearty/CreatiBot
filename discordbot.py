#discord bot time!
import discord
#imports the palette and prompts info
import palettegenerator
import prompts
#import userprompts
#to join paths
import os
#to use commands easily
from discord.ext import commands
#defines command as $
bot = commands.Bot(command_prefix='$')
#error handler to let me know what's wrong with my code!!
import traceback

#discord bot token
TOKEN = os.environ.get('TOKEN')

#defines filepath again
filepath = os.getcwd()

#discord client instance
client = discord.Client()

#help instructions
help_instructions = "- $palette to generate a random palette from colormind.io\n- $prompt to get a random prompt (out of the newest 50) from r/writingprompt"

#when bot boots up, print "Ready!!!!!" to the command line
#the playing status is "$help for both help
@bot.event
async def on_ready():
        print("Ready!!!!!")
        game = discord.Game("$info for bot info")
        await bot.change_presence(status=discord.Status.online, activity=game)
        
#on message $palette, runs palettegen() from the palette.py file, and sends the image to the channel
#where command was sent
@bot.command()
async def palette(ctx):
    print("Trying to send palette...")
    try:
        palettegenerator.palettegen()
        await ctx.send(file=discord.File(os.path.join(filepath, "palette.png")))
        print("Palette sent!!!!!")
    except:
        traceback.print_exc()
        print("Couldn't send palette! :(")
        await ctx.send("Couldn't send palette :pensive:")
    

#on message $prompt, runs promptgen from the prompts.py file and sends the prompt the channel
#where command was sent
@bot.command()
async def prompt(ctx):
    prompt = prompts.promptgen()
    await ctx.send(prompt)
    print("Prompt sent!!!!!")

#on message $help, gives help_instructions
@bot.command()
async def info(ctx):
    await ctx.send(help_instructions)
    print("Help sent!!!!!")

#on message $saveprompt, input prompt into google sheets
#@bot.command()
#async def saveprompt(ctx, *, content: str):
#    userprompts.saveprompt(content)
#    await ctx.send("Prompt, '" + content + "' saved!")
#    print("Userprompt saved!")

#@bot.command()
#async def getprompt(ctx):
 #   await ctx.send(userprompts.getprompt())
  #  print("Userprompt sent!")

#runs the bot
bot.run(TOKEN)