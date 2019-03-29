import random
from discord.ext.commands import Bot
import os

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
    number = ["1", "2", "3", "4", "5",
              "6", "7", "8", "9", "10",
              "11", "12", "13", "14", "15",
              "16", "17", "18", "19", "20",]
    await client.say("You have rolled a " + random.choice(number) + ", " + context.message.author.mention)
                
client.run(os.getenv("TOKEN"))

