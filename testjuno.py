import random
import math
from discord.ext.commands import Bot
import os

#Variables for Russian Roulette:
luck = random.randint(1,6)
bang = 6
luck = luck

BOT_PREFIX = ("!")

client = Bot(command_prefix=BOT_PREFIX)

#Yes/No
@client.command(name="mom",
                description="Determine the answer to yes-or-no style questions.",
                brief="Why do you not ask your Mother?",
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

#Dice Roller v1
@client.command(name="roll",
                description="Rolls a single d20 die. Apologies, Vee is not smart enough to let you roll multiple dice",
                brief="Does this need explaining?",
                pass_context=True)
async def roll(context):
    number = random.randint(1, 21)
    await client.say("You have rolled a " + str(number) + ", " + context.message.author.mention + ".")

#Russian Roulette
@client.command(name="roulette",
                description="For each use, the trigger is pulled until the gun goes off. Use the reload command after it does do or at your own leisure.",
                brief="Are you currently feeling lucky, punk?",
                aliases=[ 'rr', 'blyat', 'lucky', 'luck' ],
                pass_context=True)
async def roulette(context):
  global luck
  global bang
  global bank
  if luck == bang:
    luck = random.randint(1,6)
    await client.say(context.message.author.mention + " Bang. I have placed the bullet in a new chamber.")
    return (luck)
  if luck <= bang and luck != bang:
    await client.say(context.message.author.mention + " Click.")
    luck = luck + 1
    return (luck)
  
#Reload
@client.command(name="reload",
                description="For each use after the gun goes off in the roulette game. Or if you would like some fresh luck.",
                brief="Reloads the gun.",
                aliases=[ 'r' ],
                pass_context=True)
async def reload(context):
  global luck
  luck = random.randint(1,6)
  await client.say(context.message.author.mention + " I  have emptied the firearm and inserted one bullet into a random chamber.")
  return (luck)

#Peek
@client.command(name="peek",
                description="If you are ever too nervous about pulling the trigger, you can always look through the chambers.",
                brief="Naughty, naughty.",
                pass_context=True)
async def peek(context):
  global luck
  global bang
  peek = (bang - luck) + 1
  if peek == 1:
    await client.say(context.message.author.mention + " Oh dear.") 
  else:
    await client.say(context.message.author.mention + " how cowardly. The bullet is " + str(peek) + " chamber(s) away.")
                
client.run(os.getenv("TOKEN"))

