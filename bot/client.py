from discord.ext import commands

import os
import textwrap

token_file_path = os.environ.get('DISCORD_BOT_TOKEN')
with open(token_file_path, "r") as token_file:
  TOKEN = token_file.read()

client = commands.Bot(command_prefix=commands.when_mentioned_or('.'))

async def resurrect(message):
  if message.author == client.user:
    return

  await message.channel.send(
    textwrap.dedent('''
      {author}消さないで！
      ```
      {content}
      ```
    ''')
    .format(content=message.content, author=message.author.mention)
    .strip()
  )

@client.event
async def on_message_delete(message):
  await resurrect(message)

client.run(TOKEN)