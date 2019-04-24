import random
import math
from discord.ext.commands import Bot
import os

#Variables for Russian Roulette:
luck = random.randint(0,6)
bang = 6
luck = luck
bang = bang

BOT_PREFIX = ("?")

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

#Dice Roller v2
@client.command(name="roll",
                description="Rolls a single d20 die; sorry Vee isn't smart enough to let you roll multiple dice",
                brief="Does this need explaining?",
                pass_context=True)
async def roll(context):
    number = random.randint(1,21)
    await client.say("You have rolled a " + number + ", " + context.message.author.mention)
    
#Russian Roulette
@client.command(name="roulette",
                description="There is one bullet in the cylinder. Test your luck.",
                brief="Are you feeling lucky, punk?",
                aliases=[ 'rr', 'russian', 'blyat', 'bang' ],
                pass_context=True)
async def roulette(context):
    global luck
    global bang
    luck = luck + 1
    if luck == bang:
        await client.say(message.author.mention + " Bang!")
        luck = luck - bang
        return (luck)
    elif luck <= bang and luck != bang:
        await client.say(message.author.mention + " Click!")
        return (luck)

#Reload
@client.command(name="reload",
                description="Reload the gun. One bullet into a new chamber.",
                brief="Sets the bullet in a new chamber.",
                aliases=[ 'r', 'boolet'],
                pass_context=True)
async def roulette(context):
    global bang
    bang = random.randint(0,6)
    return (bang)
    await client.say(message.author.mention + ", very well then. I have emptied the firearm and inserted one bullet into a random chamber.")
    
client.run(os.getenv("TOKEN"))
