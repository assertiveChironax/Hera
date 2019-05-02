import random
from discord.ext.commands import Bot
import os

#Variables for Russian Roulette:
luck = random.randint(1,6)
bang = 6
luck = luck

#Server $$$ Bank
bank = 0

#Item list
sauce = 0
paper = 0
clout = 0
juice = 0


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
    bank = bank - 200
    await client.say(context.message.author.mention + " Bang. I have taken funds to cover your medical expenses and have placed the bullet in a new chamber.")
    return (luck)
    return (bank)
  if luck <= bang and luck != bang:
    await client.say(context.message.author.mention + " Click. Here is some cash. Whatever that means.")
    luck = luck + 1
    bank = bank + 100
    return (luck)
    return (bank)
  
#Cash
@client.command(name="bank",
                description="Displays cash earned by the server.",
                brief="Check the budget of the server.",
                aliases=[ 'money', 'cash', ],
                pass_context=True)
async def bank(context):
  global bank
  await client.say(context.message.author.mention + "The server currently has $" + str(bank) +"."

#Gacha
@client.command(name="gacha",
                description="Uses the cash of the server for one random item",
                brief="It costs $1000 for one attempt.",
                aliases=[ 'rng' ],
                pass_context=True)
async def gacha(context):
  prizes = [ "q", "w", "e", "r", ]
  global bank
  global sauce
  global paper
  global clout
  global juice
  if bank >= 1000:
    bank = bank - 1000
    await client.say(context.message.author.mention + "Rolling..."
    prize = random.choice(prizes)
    if prize == q:
      sauce = sauce + 1
      await client.say(context.message.author.mention + "Congratulations. You won sauce."
      return (sauce)
      return (bank)
    elif prize == w:
      clout = clout + 1
      await client.say(context.message.author.mention + "Congratulations. You won clout."
      return (clout)
      return (bank)
    elif prize == e:
      paper = paper + 1
      await client.say(context.message.author.mention + "Congratulations. You won paper."
      return (paper)
      return (bank)
    elif prize == r:
      juice = juice + 1
      await client.say(context.message.author.mention + "Congratulations. You won juice."
      return (juice)
      return (bank)
  elif bank != 1000:
    await client.say(context.message.author.mention + "The server currently does not have enough money to roll the gacha."
  
#Items
@client.command(name="items",
                description="Displays items collected by the server.",
                brief="What do you have?",
                aliases=[ 'itemlist' ],
                pass_context=True)
async def items(context):
  global sauce
  global clout
  global paper
  global juice       
  await client.say(context.message.author.mention + "The server currently has: /n" + "sauce: " + str(sauce) + "\n" +
                   "clout: " + str(clout) + "\n" + "paper: " + str(paper) + "\n" + "juice: " + str(juice))
                     
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

