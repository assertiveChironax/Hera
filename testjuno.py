import random
import math
from discord.ext.commands import Bot
import os

#Variables for Russian Roulette:
luck = random.randint(1,6)
bang = 6
luck = luck

#Bank Variables
cashmoney = 0
cashmoney = cashmoney

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
    global cashmoney
    if luck == bang:
        cashmoney = cashmoney - 200
        luck = random.randint(1,6)
        await client.say(context.message.author.mention + " Bang." +
                         "\n You have lost $200. I have emptied the firearm and placed a bullet in a new chamber.")
        return (luck)
        return (cashmoney)
    if luck <= bang and luck != bang:
        luck = luck + 1
        cashmoney = cashmoney + 100
        await client.say(context.message.author.mention + " Click." +
                         "\n You have won $100.")
        return (luck)
        return (cashmoney)
  
#Money
@client.command(name="money",
                description="Displays the amount of money earned by the server.",
                brief="Would you like to check your balance?",
                aliases=[ 'cash', 'bank' ],
                pass_context=True)
async def money(context):
  global cashmoney
  await client.say(context.message.author.mention + "The server currently has $" + cashmoney + ".")
  
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
        await client.say(context.message.author.mention + " How cowardly. The bullet is " + str(peek) + " chamber(s) away.")
    
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
             
client.run(os.getenv("TOKEN"))

