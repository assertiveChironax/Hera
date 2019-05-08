import random
import math
from discord.ext.commands import Bot
import os

#Variables for Russian Roulette:
luck = random.randint(1,6)
bang = 6
luck = luck

#Gacha Variables
prizepool = []
prizepool = prizepool

#Cash Variables
dollars = 0
dollars = dollars

BOT_PREFIX = ("!")

client = Bot(command_prefix=BOT_PREFIX)

#Add Prize
@client.command(name='addprize',
                description="Adds a prize to the pool.",
                brief="I suppose we need more prizes.",
                pass_context=True)
async def addprize(context, prize):
  global prizepool
  if len(prize) > 1:
    await client.say(context.message.author.mention + " You may only add one prize at a time."
  else:
    prizepool.append(prize)
    await client.say(context.message.author.mention + " I have added " + (prize) + " to the pool."
    return (prizepool)

#Allowance
@client.command(name='allowance',
                description="Either gives or takes money from the server.",
                brief="Are you going to ask me for currency again?"
                aliases=[ 'mompls', 'mommypls', 'mamapls', 'mapls', 'motherpls' ],
                pass_context=True)
async def allowance(context):
  global dollars
  mercy = random.randint(1,3)
  if mercy == 1:
    dollars = dollars + 100
    await client.say(context.message.author.mention + " Very well then. Here is $100."
    return (dollars)
  if mercy == 2:
    dollars = dollars - 25
    await client.say(context.message.author.mention + " You have asked for too much. I will be taking $25 back."
    return (dollars)
  if mercy == 3:
    await client.say(context.message.author.mention + " Perhaps another time."

#Bank
@client.command(name='bank',
                description="Checks the amount of money earned by the server.",
                brief="Would you like to check your balance?",
                aliases=[ 'money', 'cash' ],
                pass_context=True)
async def bank(context):
  global dollars
  await client.say(context.message.author.mention + " The server currently has $" + str(dollars) + ".")
  
#Choose
@client.command(name="choose",
                description="Picks something out of a pool of somethings.",
                brief="Would you like Mother to choose for you?",
                aliases=[ 'pick', 'select' ],
                pass_context=True)
async def choose(context, *choices):
    if len(choices) < 2:
        await client.say(context.message.author.mention + " There are not enough choices.") 
    else:
        await client.say(context.message.author.mention + " I choose " + random.choice(choices) + ".")

#Clear Prizes
@client.command(name='clearprizes',
                description="Clears the prize pool.",
                brief="New prizes are needed?",
                pass_context=True)
async def clearprizes(context):
  global prizepool
  prizepool = []
  await client.say(context.message.author.mention + " I have cleared the pool." )
  return (prizepool)

#Dice Roller v1
@client.command(name="roll",
                description="Rolls a single d20 die. Apologies, Vee is not smart enough to let you roll multiple dice",
                brief="Does this need explaining?",
                pass_context=True)
async def roll(context):
    number = random.randint(1, 21)
    await client.say(context.message.author.mention + " You have rolled a " + str(number) + ".")

#Gacha
@client.command(name='gacha',
                description="Uses $1000 to roll in the server gacha machine.",
                brief="What will you win?",
                pass_context=True)
async def gacha(context):
  global dollars
  global prizepool
  if dollars < 1000:
    await client.say(context.message.author.mention + " The server currently does not have enough money to roll.")
  if dollars >= 1000:
    dollars = dollars - 1000
    await client.say(context.message.author.mention + " Rolling. You won " + random.choice(prizepool) + ".")
    return (dollars)
  
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
        await client.say(context.message.author.mention + " How cowardly. The bullet is " + str(peek) + " chamber(s) away.")
      
#Prizes
@client.command(name='prizes',
                description="Displays the currently available prizes.",
                brief="What can you win?",
                pass_context=True)
async def prizes(context):
  global prizepool
  await client.say(context.message.author.mention + " The prizes currently available are " + (prizepool) + ".")
  
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
        luck = random.randint(1,6)
        await client.say(context.message.author.mention + " Bang." +
                         "\n I have emptied the firearm and placed a bullet in a new chamber.")
        return (luck)
    if luck <= bang and luck != bang:
        luck = luck + 1
        await client.say(context.message.author.mention + " Click.")
        return (luck)

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
    await client.say(context.message.author.mention + random.choice(possible_responses))

client.run(os.getenv("TOKEN"))

