import discord
from discord.ext import commands
import random

# Get your bot token from the Discord Developer Portal
TOKEN = "DISCORD_TOKEN"  # Replace with your actual bot token or use an environment variable.

# Use commands.Bot to create the bot instance
intents = discord.Intents.default()
intents.messages = True  # Enable intents to allow message-based commands.
bot = commands.Bot(command_prefix="!", intents=intents)  # Set a command prefix like "!"

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.command(description="Sends the bot's latency.")  # Command decorator for traditional text commands
async def ping(ctx):
    await ctx.send(f"Pong! Latency is {round(bot.latency * 1000)}ms")

@bot.command(description="Seal your fate. Predicts your future assigned base.")
async def base(ctx):
    bases = [
        "Maxwell-Gunter", "Eielson", "Elmendorf", "Joint Base Elmendorf-Richardson",
        "Davis-Monthan", "Luke", "Little Rock", "Beale", "Edwards", "Los Angeles",
        "March Air Reserve Base", "Travis", "Vandenberg", "Buckley", "Colorado Springs",
        "Peterson", "Schriever", "United States Air Force Academy", "Dover",
        "Joint Base Anacostia-Bolling", "Eglin", "Hurlburt Field", "MacDill", "Patrick",
        "Pensacola Florida", "Tyndall", "Moody", "Robins", "Hickam", "Joint Base Pearl Harbor - Hickam",
        "Mountain Home", "Scott AFB Guide", "Grissom Air Reserve Base", "McConnell", "Barksdale",
        "Andrews", "Joint Base Andrews", "Hanscom", "Columbus", "Keesler", "Whiteman", "Malmstrom",
        "Offutt", "Area 51", "Creech", "Nellis", "Joint Base McGuire-Dix-Lakehurst", "Cannon",
        "Holloman", "Kirtland", "Fayetteville North Carolina", "Pope Field", "Seymour Johnson",
        "Grand Forks", "Minot", "Wright-Patterson", "Altus", "Tinker", "Vance", "Charleston",
        "Joint Base Charleston", "Shaw", "Ellsworth", "Dyess", "Goodfellow", "Joint Base San Antonio",
        "Lackland", "Laughlin", "Randolph", "Red River Army Depot", "Sheppard", "Hill", "Hampton Roads",
        "Joint Base Langley-Eustis", "Langley", "Fairchild", "Joint Base Lewis-McChord", "McChord Field",
        "F. E. Warren", "Geilenkirchen NATO", "Ramstein", "Spangdahlem", "Andersen", "Aviano", "Kadena",
        "Misawa", "Yokota", "Kunsan", "Osan", "Moron", "Incirlik", "Izmir Air Station", "RAF Alconbury",
        "RAF Croughton", "RAF Lakenheath", "RAF Mildenhall"
    ]
    base = random.choice(bases)
    await ctx.send(f"{ctx.author.name}, you're going to **{base}**!")

# Run the bot
bot.run(TOKEN)
