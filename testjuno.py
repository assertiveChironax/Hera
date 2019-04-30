import random
from discord.ext.commands import Bot
import os

#Variables for Russian Roulette:
luck = random.randint(1,6)
bang = 6
luck = luck
lucky = luck
bangy = bang

BOT_PREFIX = ("!")

client = Bot(command_prefix=BOT_PREFIX)

#Yes/No
@client.command(name="mom",
                description="Determine the answer to yes-or-no style questions.",
                brief="Why don't you ask your Mother?",
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
                description="Rolls a single d20 die; sorry Vee isn't smart enough to let you roll multiple dice",
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
  if luck == bang:
    await client.say(context.message.author.mention + " Bang.")
    luck = luck - 5
    return (luck)
  if luck <= bang and luck != bang:
    await client.say(context.message.author.mention + " Click.")
    luck = luck + 1
    return (luck)
                
client.run(os.getenv("TOKEN"))

