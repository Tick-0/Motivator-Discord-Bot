import discord
from discord.ext import commands

import random
from random import choice

client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Use /motivate to call me :)"))
    print("Bot is ready")

#@client.event
#async def on_member_join(member):
#    print(f"{member} hase joined a server.")

#@client.event
#async def on_member_remove(member):
#    print(f"{member} has left a server.")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! ~~{round(client.latency * 1000)}ms~~")

@client.command(aliases=["motivateme","imsad"])
async def motivate(ctx):
    answers = [f"You know what {ctx.message.author}? Its all gonna be just fine and if you just try hard enough I'm certain it will work out for you!",
               f"JUST DO IT! {ctx.message.author}! MAKE YOUR DREAMS COME TRUE!",
               f"Learn from yesterday {ctx.message.author}, live for today and have hope for tomorrow.",
               f"If you're still looking for that one person who will change your life {ctx.message.author}... Take a look in the mirror.",
               f"We can't help everyone {ctx.message.author}, but everyone can help someone.",
               f"Don't let your worries get the best of you {ctx.message.author}; remember, Moses started out in a basket case.",
               f"{ctx.message.author} improve your memory by thinking of the unforgettable things you have already done. However insignificant they might seem, they are yours.",
               f"It's just a bad day {ctx.message.author}, not a bad life.",
               f"{ctx.message.author}... The road to success is always under construction.",
               f"Dont be afraid to stand for what you believe in, even if that means standing alone.",
               f"If you're going through Hell, keep going {ctx.message.author}. Keep going untill the mountain of solved problems is high enough for you to climb to Heaven!",
               f"Anyone who has never made a mistake has never tried anything new.",
               f"Sometimes the best helping hand you can give is a good, firm push.",
               f"The deeper the pit you're falling into, the more chance you have to learn how to fly.",
               f"Your life doesn't get better by chance. It gets better by choice.",
               f"Failure is not falling down, it is not getting up again.",
               f"Everything always ends well. If not – it's probably not the end.",
               f"Whatever you do always give 100 %. Unless you are donating blood.",
               f"The only knowledge that can hurt you is the knowledge you don't have.",
               f"Whenever someone calls me ugly, I get super sad and hug them, because I know how tough life is for the visually impaired.",
               f"When everything's coming your way, you're in the wrong lane and going the wrong way.",
               f"Dream carefully, because dreams come true.",
               f"If you think you are nobody {ctx.message.author},remember, nobody is perfect, therefore you are perfect.",
               f"If the elevator to success is out of order. You'll have to use the stairs... one step at a time.",
               f"Some people say \"If you can't beat them, join them\". I say \"If you can't beat them, beat them\", because they will be expecting you to join them, so you will have the element of surprise.",
               f"Seek knowledge from cradle to the grave.",
               f"If you put your left shoe on the wrong foot... it's on the right foot... Ehhh what I mean by that {ctx.message.author} is that a mistake might end up being a good thing!",
               f"I got called pretty yesterday and it felt good! Actually, the full sentence was \"You're pretty annoying.\" but I'm choosing to focus on the positive.",
               f"Don't be nervous if someone is driving ahead of you- the world is round, just think that you're driving first!",
               f"You can only be wrong in one case {ctx.message.author}, and that's when you think you are wrong. Well except you are just factually wrong... like when you think that birds actually exist... Damn government drones!",
               f"However lonely you feel, you're never alone. There are literally millions of bugs, mites and bacteria living in your house. Goodnight",
               f"Next time you think you’re doing a bad job, just remember that you don’t work for YouTube creator support",
               f"Being a slow walker isn’t what’s important, what matters is that you never walk back",
               f"You may end up missing a deadline, but you might as well enjoy the wooshing noise it makes as it flies by.",
               f"A learning experience is one of those things that says, 'You know that thing you just did? Don't do that.",
               f"There's no such thing as quitting. Just sometimes there's a longer pause between relapses, right?",
               f"What wonderful thing didn’t start out scary?",
               f"We are where we are, however we got here. What matters is where we go next.",
               f"It’s more important to master the cards you’re holding than to complain about the ones your opponent was dealt.",
               f"I see now that the circumstances of one’s birth are irrelevant. It is what you do with the gift of life that determines who you are.",
               f"Video games are bad for you? That's what they said about rock n' roll.",
               f"Failure is always an option, whether or not you learn from it is a choice."]


    
    await ctx.send(f"{random.choice(answers)}")

@client.command(aliases=["Senate","Credit","easteregg"])
async def maker(ctx):
    await ctx.send("This automaton comes courtesy of your Senator of the entire Universe; Ticko.\nIt comes without saying that it is expected from anyone who uses this bot to feel the utmost inspiration! \nNot feeling inspired after the use of this oh-so generously gifted automaton will be considered as treason and will be punised severely!")

client.run("Bot Token Here")
