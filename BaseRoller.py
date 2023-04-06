import discord
import random

# Get your bot token from the Discord Developer Portal
TOKEN = "DISCORD_TOKEN"


bot = discord.Bot()

# we need to limit the guilds for testing purposes
# so other users wouldn't see the command that we're testing

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="Seal your fate. Predicts your future assigned base.") # this decorator makes a slash command
async def base(ctx):
    bases = ["Maxwell-Gunter", "Eielson", "Elmendorf", "Joint Base Elmendorf-Richardson", "Davis-Monthan", "Luke", "Little Rock", "Beale", "Edwards", "Los Angeles", "March Air Reserve Base", "Travis", "Vandenberg", "Buckley", "Colorado Springs", "Peterson", "Schriever", "United States Air Force Academy", "Dover", "Joint Base Anacostia-Bolling", "Eglin", "Hurlburt Field", "MacDill", "Patrick", "Pensacola Florida", "Tyndall", "Moody", "Robins", "Hickam", "Joint Base Pearl Harbor - Hickam", "Mountain Home", "Scott AFB Guide", "Grissom Air Reserve Base", "McConnell", "Barksdale", "Andrews", "Joint Base Andrews", "Hanscom", "Columbus", "Keesler", "Whiteman", "Malmstrom", "Offutt", "Area 51", "Creech", "Nellis", "Joint Base McGuire-Dix-Lakehurst", "Cannon", "Holloman", "Kirtland", "Fayetteville North Carolina", "Pope Field", "Seymour Johnson", "Grand Forks", "Minot", "Wright-Patterson", "Altus", "Tinker", "Vance", "Charleston", "Joint Base Charleston", "Shaw", "Ellsworth", "Dyess", "Goodfellow", "Joint Base San Antonio", "Lackland", "Laughlin", "Randolph", "Red River Army Depot", "Sheppard", "Hill", "Hampton Roads", "Joint Base Langley-Eustis", "Langley", "Fairchild", "Joint Base Lewis-McChord", "McChord Field", "F. E. Warren", "Geilenkirchen NATO", "Ramstein", "Spangdahlem", "Andersen", "Aviano", "Kadena", "Misawa", "Yokota", "Kunsan", "Osan", "Moron", "Incirlik", "Izmir Air Station", "RAF Alconbury", "RAF Croughton", "RAF Lakenheath", "RAF Mildenhall"]
    base = random.choice(bases)
    await ctx.respond(f"{ctx.author.name}, you're going to **{base}")

async def on_ready():
    print(f"{bot.user.name} is ready!")

bot.run(TOKEN)