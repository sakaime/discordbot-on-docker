from discord.ext import commands

import os

token_file_path = os.environ.get('DISCORD_BOT_TOKEN')
with open(token_file_path, "r") as token_file:
  TOKEN = token_file.read()

client = commands.Bot(command_prefix=commands.when_mentioned_or('.'))

@client.event
async def on_ready():
    print("I'm ready")

client.run(TOKEN)