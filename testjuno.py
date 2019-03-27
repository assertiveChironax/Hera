import random
from discord.ext.commands import Bot

BOT_PREFIX = ("!")

client = Bot(command_prefix=BOT_PREFIX)

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
    
client.run(config.py)

