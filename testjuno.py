import random
from discord.ext.commands import Bot
import os

#Variables for Russian Roulette:
luck = random.randint(1,6)
bang = 6
luck = luck
lucky = luck
bangy = bang

class Help:
    """This is the list of commands currently available."""
bot.add_cog(Help())

BOT_PREFIX = ("!")

client = Bot(command_prefix=BOT_PREFIX)

#Yes/No
@client.command(name="mom",
                description="Determine the answer to yes-or-no style questions.",
                brief="Why do you not you ask your Mother?",
                aliases=[ 'mother', 'mommy', 'mama', 'ma' ],
                pass_context=True)
async def mom(context):
    possible_responses = [
        " Yes.",
        " No.",
        " Maybe.",
        " Why do you not ask me later?",
    ]
    #await client.say(random.choice(possible_responses)) for no @
    await client.say(context.message.author.mention + "," + random.choice(possible_responses))
  bot.add_cog(Help())

#Dice Roller v1
@client.command(name="roll",
                description="Rolls a single d20 die. Apologies, Vee is not smart enough to let you roll multiple dice",
                brief="Does this need explaining?",
                pass_context=True)
async def roll(context):
    number = random.randint(1, 21)
    await client.say("You have rolled a " + str(number) + ", " + context.message.author.mention + ".")
  bot.add_cog(Help())

#Russian Roulette
@client.command(name="roulette",
                description="For each use, the trigger is pulled until the gun goes off. Use the reload command after it does do or at your own leisure.",
                brief="Are you currently feeling lucky, punk?",
                aliases=[ 'rr', 'blyat', 'lucky', 'luck' ],
                pass_context=True)
async def roulette(context):
  global luck
  global bang
  if luck == bang:
    await client.say(context.message.author.mention + " Bang.")
    luck = luck - 5
    return (luck)
  if luck <= bang and luck != bang:
    await client.say(context.message.author.mention + " Click.")
    luck = luck + 1
    return (luck)
  bot.add_cog(Help())
  
#Reload
@client.command(name="reload",
                description="For each use after the gun goes off in the roulette game. Or if you would like some fresh luck.",
                brief="Reloads the gun.",
                aliases=[ 'r' ],
                pass_context=True)
async def reload(context):
  global lucky
  luck = random.randint(1,6)
  await client.say(context.message.author.mention + " I  have emptied the firearm and inserted one bullet into a random chamber.")
  return (luck)
  bot.add_cog(Help())

#Peek
@client.command(name="peek",
                description="If you are ever too nervous about pulling the trigger, you can always look through the chambers.",
                brief="Naughty, naughty.",
                pass_context=True)
async def peek(context):
  global lucky
  global bangy
  lucky = luck
  bangy = bang
  peek = (bang - luck) + 1
  if peek == 1:
    await client.say(context.message.author.mention + " Oh dear.") 
  if lucky != bangy:
    await client.say(context.message.author.mention + " how cowardly. The bullet is " + str(peek) + " chamber(s) away.")
  bot.add_cog(Help())
                
client.run(os.getenv("TOKEN"))

